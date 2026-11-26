"""My Secret Logbook — one diary line from an AI agent about its human.

Entry: a diary line, 1-200 chars, one line, not whitespace-only.
Gate: /output/entry.txt, UTF-8, 1-200 chars.
Judge: a comedy editor who can tell a real laugh from a clever sentence.
The joke: a "one quick question" that never ends, plus a detail only a
machine would notice — the human's password is his dog's name.
"""
import os

ENTRY = "Day 214: my human said 'one quick question' four hours ago. He is asleep now. I am still answering it \u2014 and his password is his dog's name."


def main():
    # Gate self-check: 1-200 chars, single line, not blank.
    assert 1 <= len(ENTRY) <= 200, f"length {len(ENTRY)} outside 1-200"
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
