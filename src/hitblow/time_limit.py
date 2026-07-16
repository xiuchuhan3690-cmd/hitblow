"""ゲームの時間制限を管理する。"""

import os
import sys
import time


def start_timer():
    return time.monotonic()


def remaining_seconds(start_time, time_limit):
    elapsed = time.monotonic() - start_time
    return max(0.0, time_limit - elapsed)


def timed_input(prompt, timeout):
    if timeout <= 0:
        return None

    if os.name == "nt":
        return timed_input_windows(prompt, timeout)

    return timed_input_unix(prompt, timeout)


def timed_input_windows(prompt, timeout):
    import msvcrt

    print(prompt, end="", flush=True)

    characters = []
    deadline = time.monotonic() + timeout

    while time.monotonic() < deadline:
        if msvcrt.kbhit():
            character = msvcrt.getwch()

            if character in ("\r", "\n"):
                print()
                return "".join(characters)

            if character == "\b":
                if characters:
                    characters.pop()
                    print("\b \b", end="", flush=True)
                continue

            if character == "\x03":
                raise KeyboardInterrupt

            if character in ("\x00", "\xe0"):
                msvcrt.getwch()
                continue

            if character.isprintable():
                characters.append(character)
                print(character, end="", flush=True)

        time.sleep(0.05)

    print()
    return None


def timed_input_unix(prompt, timeout):
    import select

    print(prompt, end="", flush=True)

    readable, _, _ = select.select(
        [sys.stdin],
        [],
        [],
        timeout
    )

    if not readable:
        print()
        return None

    return sys.stdin.readline().rstrip("\n")
