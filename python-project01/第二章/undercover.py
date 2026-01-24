from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_123456'
socketio = SocketIO(app, cors_allowed_origins="*")  # 允许跨域，部署时可限定域名

# 全局游戏状态管理
game_state = {
    "players": {},  # 玩家字典：{player_id: {"ready": False, "vote": None, "word": "", "number": 0}}
    "total_players": 6,  # 固定6人
    "game_started": False,
    "votes": {str(i): 0 for i in range(1, 7)},  # 1-6号得票数
    "same_vote_players": [],  # 同票玩家列表（加赛用）
    "undercover_number": 0,  # 卧底的编号（空白词汇）
    "voting_round": 1,  # 投票轮次（1=正常投票，2=加赛投票）
    "all_voted": False  # 是否所有玩家已投票
}

# 预设词汇库（可自行扩展）
WORD_POOL = [
    "手机", "电脑", "水杯", "雨伞", "书包", "手表",
    "口罩", "纸巾", "耳机", "充电宝", "钥匙", "眼镜"
]


@app.route('/')
def index():
    """游戏主页面"""
    return render_template('index.html')


@socketio.on('join_game')
def handle_join():
    """玩家进入游戏，分配1-6号编号"""
    # 分配未被占用的编号
    used_numbers = [p["number"] for p in game_state["players"].values()]
    available_numbers = [i for i in range(1, 7) if i not in used_numbers]

    if not available_numbers:
        emit('join_result', {"success": False, "msg": "游戏人数已满（6人）！"})
        return

    player_id = request.sid  # 用SocketID作为玩家唯一标识
    player_number = available_numbers[0]
    game_state["players"][player_id] = {
        "ready": False,
        "vote": None,
        "word": "",
        "number": player_number
    }

    # 广播所有玩家的编号和状态（同步到所有客户端）
    emit('player_list_update', {
        "players": {k: {"number": v["number"], "ready": v["ready"]} for k, v in game_state["players"].items()},
        "your_number": player_number
    }, broadcast=True)
    emit('join_result', {"success": True, "msg": f"成功加入游戏！你的编号是：{player_number}"})


@socketio.on('player_ready')
def handle_ready():
    """玩家点击准备按钮"""
    player_id = request.sid
    if player_id not in game_state["players"]:
        emit('ready_result', {"success": False, "msg": "你还未加入游戏！"})
        return

    game_state["players"][player_id]["ready"] = True
    # 检查是否所有6人都已准备
    ready_players = [p for p in game_state["players"].values() if p["ready"]]
    all_ready = len(ready_players) == game_state["total_players"]

    # 广播准备状态
    emit('ready_update', {
        "players": {k: {"number": v["number"], "ready": v["ready"]} for k, v in game_state["players"].items()},
        "all_ready": all_ready
    }, broadcast=True)

    # 所有玩家准备完成，启动游戏
    if all_ready and not game_state["game_started"]:
        start_game()


def start_game():
    """游戏启动：分配词汇（1人空白=卧底）"""
    game_state["game_started"] = True
    # 随机选一个基础词汇
    base_word = random.choice(WORD_POOL)
    # 随机选卧底编号（1-6）
    undercover_number = random.randint(1, 6)
    game_state["undercover_number"] = undercover_number

    # 为每个玩家分配词汇
    for player_id, player in game_state["players"].items():
        if player["number"] == undercover_number:
            player["word"] = "空白"  # 卧底是空白
        else:
            player["word"] = base_word

    # 广播词汇和游戏启动状态
    player_words = {p["number"]: p["word"] for p in game_state["players"].values()}
    emit('game_start', {
        "player_words": player_words,
        "undercover_number": undercover_number  # 前端仅展示当前玩家自己的词汇，不暴露卧底
    }, broadcast=True)


@socketio.on('submit_vote')
def handle_vote(data):
    """处理玩家投票"""
    player_id = request.sid
    voted_number = str(data["number"])  # 投票给的编号（1-6）
    voting_round = data["round"]  # 投票轮次（1/2）

    if player_id not in game_state["players"]:
        emit('vote_result', {"success": False, "msg": "你还未加入游戏！"})
        return
    if game_state["players"][player_id]["vote"] is not None:
        emit('vote_result', {"success": False, "msg": "你已投票，不可重复投票！"})
        return

    # 记录投票（加赛轮仅允许投给同票玩家）
    if voting_round == 2 and voted_number not in game_state["same_vote_players"]:
        emit('vote_result', {"success": False, "msg": "加赛轮仅可投给同票玩家！"})
        return

    game_state["players"][player_id]["vote"] = voted_number
    game_state["votes"][voted_number] += 1

    # 检查是否所有玩家已投票
    voted_players = [p for p in game_state["players"].values() if p["vote"] is not None]
    game_state["all_voted"] = len(voted_players) == game_state["total_players"]

    emit('vote_result', {"success": True, "msg": "投票成功！"}, broadcast=True)

    # 所有玩家投票完成，统计结果
    if game_state["all_voted"]:
        count_votes()


def count_votes():
    """统计票数，处理同票/出局逻辑"""
    votes = game_state["votes"]
    max_vote = max(votes.values())
    # 得票最多的玩家列表
    max_vote_players = [num for num, cnt in votes.items() if cnt == max_vote]

    if len(max_vote_players) > 1:
        # 同票，触发加赛
        game_state["same_vote_players"] = max_vote_players
        game_state["voting_round"] = 2
        # 重置票数和投票状态
        game_state["votes"] = {str(i): 0 for i in range(1, 7)}
        for player in game_state["players"].values():
            player["vote"] = None
        game_state["all_voted"] = False
        emit('vote_result', {
            "type": "same_vote",
            "players": max_vote_players,
            "msg": f"同票！加赛轮仅可投票给：{','.join(max_vote_players)}号"
        }, broadcast=True)
    else:
        # 有唯一出局者，判断是否是卧底
        out_player = max_vote_players[0]
        is_undercover = out_player == str(game_state["undercover_number"])
        game_result = "游戏结束" if is_undercover else "游戏继续"
        emit('vote_result', {
            "type": "result",
            "out_player": out_player,
            "votes": votes,
            "result": game_result,
            "msg": f"{out_player}号出局！{game_result}（{'卧底出局' if is_undercover else '平民出局'}）"
        }, broadcast=True)
        # 重置游戏状态（可根据需求调整，比如继续下一轮）
        reset_game()


def reset_game():
    """重置游戏状态（准备下一轮）"""
    game_state["game_started"] = False
    game_state["votes"] = {str(i): 0 for i in range(1, 7)}
    game_state["same_vote_players"] = []
    game_state["voting_round"] = 1
    game_state["all_voted"] = False
    for player in game_state["players"].values():
        player["ready"] = False
        player["vote"] = None
        player["word"] = ""


@socketio.on('reset_all')
def handle_reset():
    """手动重置游戏（可选功能）"""
    reset_game()
    emit('game_reset', {"msg": "游戏已重置，请重新准备！"}, broadcast=True)


if __name__ == '__main__':
    # 运行服务，host=0.0.0.0 允许外网访问
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)