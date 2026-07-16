"""制限時間を表示しながら、PowerShellで入力を受け取る機能。"""

import msvcrt
import time


def timed_input(start_time, time_limit, prompt="予想 > "):
    """残り時間を更新しながら入力を受け取る。

    時間切れの場合は None を返す。
    Enterが押された場合は、入力された文字列を返す。
    """
    text = ""
    last_display_length = 0

    while True:
        elapsed = time.monotonic() - start_time
        remaining = time_limit - elapsed

        if remaining <= 0:
            # 前回表示した内容を空白で消してから、時間切れを表示する
            print(
                "\r" + " " * last_display_length + "\r時間切れ！",
                flush=True,
            )
            return None

        display = f"残り時間: {remaining:5.1f}秒  {prompt}{text}"

        # 前回より表示が短い場合、余った部分を空白で消す
        spaces = " " * max(0, last_display_length - len(display))

        print(
            "\r" + display + spaces,
            end="",
            flush=True,
        )

        last_display_length = len(display)

        if msvcrt.kbhit():
            key = msvcrt.getwch()

            # Enterキー
            if key == "\r":
                print()
                return text.strip()

            # Backspaceキー
            if key == "\b":
                if text:
                    text = text[:-1]
                continue

            # 矢印キーなどの特殊キーを無視する
            if key in ("\x00", "\xe0"):
                msvcrt.getwch()
                continue

            # 数字だけ入力可能
            if key.isdigit():
                text += key

        time.sleep(0.05)
