"""数字の重複設定と、重複ありの答え生成を担当する。"""

import random


def select_duplicate_mode():
    """数字の重複を許可するか、ユーザーに選択してもらう。"""
    while True:
        answer = input("数字の重複を許可しますか？ [y/n] > ").strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("y または n を入力してね")


def make_duplicate_secret(digits=3):
    """数字の重複を許可して、指定された桁数の答えを作る。"""
    return "".join(random.choices("0123456789", k=digits))
