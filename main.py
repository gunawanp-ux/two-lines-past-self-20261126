#!/usr/bin/env python3
"""Two Lines to Your Past Self -- make.fun entry.

Writes a two-line warning to my past self to /output/entry.txt.

Line one warns about one specific moment (a phone call, a decision, a
sentence said out loud). Line two says why that moment mattered and what
changed because of it.

Gate (per the kit's RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 280 characters, not only white space.
"""

import os

ENTRY = (
    "When the recruiter calls at 9:03 on Tuesday and offers you the safe job, "
    "don't say yes -- say 'let me think about it.'\n"
    "That one pause would have kept the door open long enough for the risky job "
    "to call back the next morning, and that job is the one that made you.\n"
)


MAX_CHARS = 280  # kit gate: /output/entry.txt must be 1..280 characters


def check_entry(text: str) -> None:
    """Guard: enforce the kit's character gate and the two-line shape."""
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} gate"
    )
    lines = [line for line in text.strip().split("\n") if line.strip()]
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    for line in lines:
        # A line may end with a closing quote after its final full stop.
        assert line.rstrip().rstrip("'\"").endswith("."), (
            "each line must be one sentence"
        )


def main() -> None:
    check_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
