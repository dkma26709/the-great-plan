#!/usr/bin/env python3
"""Replace magic-stat abbreviations with full names across all docs.

§1 stat-line is excluded — its Magic Profile definition table is hand-
edited to drop the Abbreviation column entirely, since the abbreviations
are no longer used anywhere in the ruleset.
"""

import re
from pathlib import Path

DOCS = Path("C:/PersonalRepos/the-great-plan/docs")

EXCLUDE = {"rules/01-stat-line.md"}

# Order: replace longer/more specific abbreviations first.
# \b word boundaries prevent false-positive partial-word matches.
REPLACEMENTS = [
    (r"\bCaB\b", "Cast Base"),
    (r"\bDiB\b", "Dispel Base"),
    (r"\bCB\b", "Cast Bonus"),
    (r"\bDB\b", "Dispel Bonus"),
    (r"\bDR\b", "Dispel Range"),
    (r"\bLA\b", "Lore Access"),
    (r"\bCh\b", "Channelling"),
]


def main():
    changed = 0
    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(DOCS).as_posix()
        if rel in EXCLUDE:
            continue
        text = path.read_text(encoding="utf-8")
        new_text = text
        for pattern, replacement in REPLACEMENTS:
            new_text = re.sub(pattern, replacement, new_text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed += 1
            print(f"Updated: {rel}")
    print(f"\n{changed} files changed")


if __name__ == "__main__":
    main()
