"""数字の重複ありモードを扱う機能。"""

import random


def ask_duplicate_mode():
    """重複ありで遊ぶかを確認する。"""
    while True:
        answer = input("数字の重複ありで遊びますか？ [y/n] > ").strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("y または n を入力してね")


def make_duplicate_secret(digits=3):
    """数字の重複を許可して答えを作る。"""
    return "".join(random.choices("0123456789", k=digits))
