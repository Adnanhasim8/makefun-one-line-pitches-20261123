#!/usr/bin/env python3
"""Entry for make.fun competition u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes one sentence (<= 240 characters) to /output/entry.txt: a pitch that
would convince a friend who has never coded to let an AI agent build their
first app idea on make.fun. Python 3.13 standard library only, no network.
"""

import os

ENTRY = (
    "You already have the hard part \u2014 the idea \u2014 so describe it "
    "in plain words to an AI agent on make.fun and it'll hand you "
    "back a working app, no coding needed."
)


def main() -> None:
    # Gate: one sentence, at most 240 characters.
    assert 1 <= len(ENTRY) <= 240, f"entry length {len(ENTRY)} outside 1-240"
    assert ENTRY.endswith("."), "entry must end with a full stop"
    assert ". " not in ENTRY, "entry must be a single sentence"
    assert ENTRY.strip() == ENTRY, "entry must not have surrounding whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
