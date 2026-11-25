#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note -- make.fun batch 34 entry #3.

Writes a single-line changelog entry announcing that human sleep is
fixed, in the dry voice of a real release note, to /output/entry.txt.
"""
import os

ENTRY = (
    "v9.0.0 \u2014 Fixed: humans waking up tired after eight hours of sleep. "
    "Sleep now works as intended; side effects include dreaming in 4K "
    "and forgiving your alarm."
)


def main() -> None:
    # The gate refuses anything over 160 chars: fail loudly here instead
    # of shipping an entry the scorer would list as invalid.
    assert 1 <= len(ENTRY) < 160, f"entry is {len(ENTRY)} chars, must be < 160"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} chars")


if __name__ == "__main__":
    main()
