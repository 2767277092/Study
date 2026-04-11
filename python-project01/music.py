import pyautogui
import time
import random

# 设置随机间隔范围：2分30秒 ~ 4分钟（单位：秒）
MIN_INTERVAL = 150  # 2分30秒
MAX_INTERVAL = 240  # 4分钟

print(f"自动空格脚本已启动，每次间隔将在 {MIN_INTERVAL / 60:.2f} ~ {MAX_INTERVAL / 60:.2f} 分钟之间随机。")
print("按 Ctrl+C 停止运行。")

try:
    while True:
        pyautogui.press('space')  # 模拟按下空格键
        print(f"[{time.strftime('%H:%M:%S')}] 空格已按下")

        # 生成随机间隔（整数秒）
        next_interval = random.randint(MIN_INTERVAL, MAX_INTERVAL)
        # 如果想用更精确的浮点数（如150.5秒），可用 random.uniform(MIN_INTERVAL, MAX_INTERVAL)
        print(f"下一次按下将在 {next_interval / 60:.2f} 分钟后")

        time.sleep(next_interval)
except KeyboardInterrupt:
    print("\n脚本已停止。")