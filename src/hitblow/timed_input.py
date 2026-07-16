"""制限時間を表示しながら、PowerShellで入力を受け取る機能。"""

import msvcrt
import time


def timed_input(start_time, time_limit, prompt="予想 > "):
    """残り時間を更新しながら入力を受け取る。

    時間切れの場合は None を返す。
    Enterが押された場合は、入力された文字列を返す。
    """
    text = ""
    last_display = ""

    while True:
        elapsed = time.monotonic() - start_time
        remaining = time_limit - elapsed

        if remaining <= 0:
            print("\r時間切れ！" + " " * 30)
            return None

        display = f"\r残り時間: {remaining:5.1f}秒  {prompt}{text}"

        if display != last_display:
            print(display, end="", flush=True)
            last_display = display

        if msvcrt.kbhit():
            key = msvcrt.getwch()

            # Enterキー
            if key == "\r":
                print()
                return text.strip()

            # Backspaceキー
            if key == "\b":
                text = text[:-1]
                continue

            # 数字だけ入力可能
            if key.isdigit():
                text += key

        time.sleep(0.05)
