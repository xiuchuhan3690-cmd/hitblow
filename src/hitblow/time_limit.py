"""ゲームの制限時間を管理する機能。"""

import time


def ask_time_limit():
    """制限時間を秒単位で入力してもらう。"""
    while True:
        value = input("制限時間を秒で指定してください > ").strip()

        if not value.isdigit():
            print("1以上の整数を入力してね")
            continue

        time_limit = int(value)

        if time_limit < 1:
            print("1以上の整数を入力してね")
            continue

        return time_limit


def start_timer():
    """現在時刻をゲーム開始時刻として返す。"""
    return time.monotonic()


def remaining_time(start_time, time_limit):
    """残り時間を秒単位で返す。"""
    elapsed_time = time.monotonic() - start_time
    return max(0, time_limit - elapsed_time)


def is_time_up(start_time, time_limit):
    """制限時間を過ぎたか判定する。"""
    return remaining_time(start_time, time_limit) <= 0
