"""挑戦回数の制限を設定する機能。"""


def ask_attempt_limit():
    """プレイヤーに最大挑戦回数を入力してもらう。"""
    while True:
        value = input("挑戦できる回数を指定してください > ").strip()

        if not value.isdigit():
            print("1以上の整数を入力してね")
            continue

        limit = int(value)

        if limit < 1:
            print("1以上の整数を入力してね")
            continue

        return limit
