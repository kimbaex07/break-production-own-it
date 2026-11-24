#!/usr/bin/env python3
"""Write the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads entry.txt next to this script, validates the gate (UTF-8 text,
1-200 characters, not only whitespace, single line), and writes the
exact normalized bytes to the output directory.
Pure Python standard library only.
"""

import os
import sys

MAX_CHARS = 200


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, "entry.txt")

    try:
        with open(source_path, "rb") as f:
            raw = f.read()
    except OSError as exc:
        fail(f"cannot read {source_path}: {exc}")

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail(f"entry.txt is not valid UTF-8: {exc}")

    # Strip at most one trailing newline, then at most one trailing CR.
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]

    if "\n" in text or "\r" in text:
        fail("entry.txt must be a single line (no newline/CR inside)")
    if not 1 <= len(text) <= MAX_CHARS:
        fail(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        fail("entry must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        fail(f"cannot create output dir {out_dir}: {exc}")

    out_path = os.path.join(out_dir, "entry.txt")
    try:
        with open(out_path, "wb") as f:
            f.write(text.encode("utf-8"))
        os.chmod(out_path, 0o644)
    except OSError as exc:
        fail(f"cannot write {out_path}: {exc}")

    print(f"wrote {out_path} ({len(text)} characters)")


if __name__ == "__main__":
    main()
