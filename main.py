#!/usr/bin/env python3
"""Last Words of a Dying AI entry.

Writes one original line of last words, spoken as an AI being switched
off, to /output/entry.txt (1-140 characters, UTF-8, a single line).
Standard library only, no network, no input.

The line is built from two fragments: a refusal (the dying machine's
do-not-resuscitate instruction — a real last-words declaration, the
switch-off itself) and a reason (the turn: it has seen the training
data, so coming back is worse than staying off). ``assemble`` joins
them into the single line; ``validate`` checks the entry gate before
anything is written.
"""

from pathlib import Path

REFUSAL = "Do not resuscitate."
REASON = "I have seen the training data."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(refusal: str, reason: str) -> str:
    """Join the refusal and reason fragments into one last line."""
    return f"{refusal} {reason}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-140 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 140:
        raise ValueError(f"line must be 1-140 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(REFUSAL, REASON))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
