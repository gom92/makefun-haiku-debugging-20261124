"""Seventeen Syllables of Debugging.

One haiku about debugging, written to /output/entry.txt.

The haiku (5-7-5, seventeen syllables, 81 characters):

    Cursor blinks at three             (5: cur-sor 2, blinks 1, at 1, three 1)
    stack trace names a stranger's code (7: stack 1, trace 1, names 1, a 1, stran-ger's 2, code 1)
    I wrote it last spring             (5: I 1, wrote 1, it 1, last 1, spring 1)
"""

import os

HAIKU_LINES = (
    "Cursor blinks at three",
    "stack trace names a stranger's code",
    "I wrote it last spring",
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = "\n".join(HAIKU_LINES)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
