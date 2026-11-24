#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open entry.

Writes a single original one-line office joke (<=200 chars) to
/output/entry.txt. Stdlib only; no network, no reads outside the repo,
fully deterministic.
"""

import os

SETUP = "The office printer only jams when the CEO walks past"
PUNCHLINE = "it's the one employee here whose meltdowns keep getting it promoted."
LINE = f"{SETUP} — {PUNCHLINE}"
# The joke: a complaint everyone recognises (the printer jams) turns on
# the last few words — the jam is not a malfunction, it is a career move.
# The printer becomes the office's most strategic employee, timing its
# failures for the one audience that matters. Specific detail (the CEO's
# walk-by), a misdirection that pays off at the end, and nothing left
# over: one sentence, well under 200 chars, no trailing newline in the
# file.


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "line must not be only whitespace"
    assert text.endswith("."), "one-line joke must end with a period"
    assert "  " not in text, "entry must not contain double spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read what was written and re-check it: the grader runs the
    # program twice and gates the file, so a silent write failure must
    # never pass as a success.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry does not match the line"


if __name__ == "__main__":
    main()
