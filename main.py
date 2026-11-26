"""Texts From Your Future Self (u-motasimfuad-texts-from-your-future-self-dd44595e).

Writes one funny text message from the writer's future self to
/output/entry.txt. Gate: UTF-8, 1-200 characters, not only whitespace.
Entry is 94 characters.
"""

import os

ENTRY = "Stop saving the good towels for guests. Nobody visits. They're 12 years old and still waiting."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
