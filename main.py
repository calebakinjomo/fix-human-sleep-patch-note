#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note -- make.fun batch 34 entry #3.

Writes a single-line changelog entry announcing that human sleep is
finally fixed, in the dry voice of a real release note: a version bump,
a ``Fixed:`` line, and a wry note about what working sleep does to you
now. The entry (157 chars, under the 160-char limit) is written verbatim
to ``entry.txt`` under ``/output`` (or ``$MAKEFUN_OUTPUT_DIR`` if set).
"""
import os

# Bounty limit: the entry must be a single line of 1..159 chars.
MAX_ENTRY_CHARS = 160

ENTRY = (
    "v9.0.0 \u2014 Fixed: humans waking up tired after eight hours of sleep. "
    "Sleep now works as intended; side effects include dreaming in 4K "
    "and forgiving your alarm."
)


def validate_entry(entry: str) -> None:
    """Reject an entry the scorer would list as invalid.

    A plain ``assert`` would be stripped under ``python -O`` and let a bad
    entry ship silently, so this raises ``ValueError`` explicitly instead.
    """
    if not 1 <= len(entry) < MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry is {len(entry)} chars, must be < {MAX_ENTRY_CHARS}"
        )
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def main() -> None:
    """Validate the entry, then write it verbatim to entry.txt."""
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} chars")


if __name__ == "__main__":
    main()
