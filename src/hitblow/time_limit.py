"""ゲームの時間制限を管理する。"""

import time


def ask_time_limit():
    """制限時間を入力してもらう。"""
    while True:
        value = input("制限時間を秒で入力してください（例：30）> ").strip()

        if value.isdigit() and int(value) > 0:
            return int(value)

        print("1以上の数字を入力してください")


def start_timer():
    """ゲーム開始時刻を返す。"""
    return time.monotonic()


def is_time_up(start_time, time_limit):
    """制限時間を過ぎたか判定する。"""
    elapsed = time.monotonic() - start_time
    return elapsed >= time_limit


def remaining_time(start_time, time_limit):
    """残り時間を返す。"""
    elapsed = time.monotonic() - start_time
    return max(0, time_limit - elapsed)
