# 导入必需的库
import random
import time
import pyautogui

# ====================== 【自定义配置】修改这里即可 ======================
# 随机等待时间区间（单位：秒），可自由修改
MIN_WAIT = 10   # 最小等待时间（比如10秒）
MAX_WAIT = 60   # 最大等待时间（比如60秒）
# =====================================================================

# 1. 生成区间内的随机等待时间
wait_seconds = random.randint(MIN_WAIT, MAX_WAIT)

# 2. 提示用户并开始倒计时
print("="*50)
print(f"🎵 网易云自动暂停工具已启动")
print(f"⏱️ 随机等待时间：{wait_seconds} 秒")
print(f"⌛ 倒计时中...（请勿锁屏/休眠）")
print("="*50)

# 倒计时显示（每秒刷新）
for i in range(wait_seconds, 0, -1):
    print(f"剩余时间：{i:02d} 秒", end="\r")  # \r 让文字原地刷新
    time.sleep(1)

# 3. 时间到！触发快捷键 Ctrl+Alt+W
pyautogui.hotkey("ctrl", "alt", "w")

# 4. 完成提示
print("\n" + "="*50)
print("✅ 成功触发 Ctrl+Alt+W，网易云音乐已暂停！")
print("="*50)