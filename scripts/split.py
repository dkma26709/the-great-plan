#!/usr/bin/env python3
"""Split the monolithic core-rules-draft.md into per-page MkDocs files."""

import re
import shutil
from pathlib import Path

SOURCE_FILE = Path("C:/PersonalRepos/Warhammer Hybrid Ruleset/core-rules-draft.md")
TARGET_DIR = Path("C:/PersonalRepos/the-great-plan/docs")

RULES_FILES = {
    "1": "rules/01-stat-line.md",
    "2": "rules/02-comparative-tables.md",
    "3": "rules/03-weapon-characteristics.md",
    "4": "rules/04-attacks-and-combat.md",
    "5": "rules/05-stress-and-morale.md",
    "6": "rules/06-movement.md",
    "7": "rules/07-turn-structure.md",
    "8": "rules/08-special-rules.md",
    "9": "rules/09-army-composition.md",
    "12": "rules/12-open-questions.md",
    "13": "rules/13-points-framework.md",
}

FACTION_DIR = {
    "10": "armies/seraphon",
    "14": "armies/empire",
    "15": "armies/ogre-kingdoms",
    "16": "armies/vampire-counts",
}

GENERAL_LORES = {"Heavens", "Beasts", "Fire", "Light", "Life", "Death", "Shadow", "Metal"}
FACTION_LORES = {"Geomancy", "Cosmic Architecture", "Necromancy"}

UNIT_SUBSECTIONS = {
    "Core Units": "core",
    "Special Units": "special",
    "Rare Units": "rare",
    "Characters": "characters",
    "Character Mounts": "mounts",
}

# Pages to leave alone (hand-maintained landing pages)
KEEP_EXISTING = {
    "index.md",
    "rules/index.md",
    "armies/index.md",
}

# Directories that the split script owns — wiped before each run
WIPE_DIRS = [
    "rules",
    "magic",
    "armies/seraphon",
    "armies/empire",
    "armies/ogre-kingdoms",
    "armies/vampire-counts",
]


def clean_heading(s: str) -> str:
    """Strip markdown emphasis and parenthetical asides from a heading."""
    s = re.sub(r"\s*\*[^*]+\*", "", s)
    s = re.sub(r"\s*\([^)]+\)", "", s)
    return s.strip()


def slugify(name: str) -> str:
    """Convert a unit/section name to a URL slug."""
    s = clean_heading(name)
    s = s.lower()
    s = re.sub(r"[—–]", "-", s)
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[-\s]+", "-", s)
    return s.strip("-")


def classify_faction_subsection(heading: str) -> tuple[str, str, str]:
    """For a ### heading inside a faction, return (kind, slug, title)."""
    clean = clean_heading(heading)
    if clean in UNIT_SUBSECTIONS:
        return ("unit_folder", UNIT_SUBSECTIONS[clean], clean)
    if re.search(r"\b(Armoury|Equipment)\b", clean):
        return ("page", "armoury", "Armoury")
    return ("page", slugify(clean), clean)


def main():
    # Wipe owned directories so renames/re-slugs don't leave orphans
    for rel in WIPE_DIRS:
        d = TARGET_DIR / rel
        if d.exists():
            for child in d.rglob("*"):
                if child.is_file() and (child.relative_to(TARGET_DIR).as_posix() not in KEEP_EXISTING):
                    child.unlink()
            # cleanup empty directories afterwards
        # mkdir again
        d.mkdir(parents=True, exist_ok=True)

    text = SOURCE_FILE.read_text(encoding="utf-8")
    lines = text.split("\n")

    pages: dict[str, list[str]] = {}

    section: str | None = None
    subsection: str | None = None
    current_path: str | None = None

    def open_page(path: str, title: str | None = None):
        nonlocal current_path
        current_path = path
        if path not in pages:
            pages[path] = []
            if title:
                pages[path].append(f"# {title}")
                pages[path].append("")

    def append(line: str):
        if current_path is not None:
            pages[current_path].append(line)

    for line in lines:
        # ## numbered top-level
        m = re.match(r"^## (\d+)\. (.+?)\s*$", line)
        if m:
            section = m.group(1)
            title = clean_heading(m.group(2))
            subsection = None
            if section in RULES_FILES:
                open_page(RULES_FILES[section], f"§{section} {title}")
            elif section in FACTION_DIR:
                fac = FACTION_DIR[section]
                open_page(f"{fac}/index.md", title)
            elif section == "11":
                open_page("magic/index.md", "Magic & Spell Lores")
            else:
                open_page(f"misc/{slugify(title)}.md", title)
            continue

        # ## unnumbered top-level (e.g., "## Faction Lores" within §11)
        m = re.match(r"^## (.+?)\s*$", line)
        if m:
            heading = clean_heading(m.group(1))
            if section in {"11", "faction-lores"} and heading == "Faction Lores":
                section = "faction-lores"
                subsection = None
                continue
            append(line)
            continue

        # ### subsection
        m = re.match(r"^### (.+?)\s*$", line)
        if m:
            heading = m.group(1).strip()

            # Faction subsection
            if section in FACTION_DIR:
                kind, slug, title = classify_faction_subsection(heading)
                fac = FACTION_DIR[section]
                if kind == "unit_folder":
                    subsection = slug
                    # don't open a page; wait for #### units
                else:  # "page"
                    subsection = slug
                    open_page(f"{fac}/{slug}.md", title)
                continue

            # §11 / Faction Lores → split per "Lore of X"
            if section in {"11", "faction-lores"}:
                clean = clean_heading(heading)
                lm = re.match(r"^Lore of (.+)$", clean)
                if lm:
                    lore_name = lm.group(1).strip()
                    if lore_name in GENERAL_LORES:
                        open_page(
                            f"magic/general-lores/{slugify(lore_name)}.md",
                            f"Lore of {lore_name}",
                        )
                        subsection = "lore"
                        continue
                    if lore_name in FACTION_LORES:
                        open_page(
                            f"magic/faction-lores/{slugify(lore_name)}.md",
                            f"Lore of {lore_name}",
                        )
                        subsection = "lore"
                        continue
                # other ### within magic — keep on current page
                append(line)
                continue

            # ### within a rules section — keep as subheading
            append(line)
            continue

        # #### unit heading (only within a faction unit-folder subsection)
        m = re.match(r"^#### (.+?)\s*$", line)
        if (
            m
            and section in FACTION_DIR
            and subsection in {"core", "special", "rare", "characters", "mounts"}
        ):
            unit_name = m.group(1).strip()
            slug = slugify(unit_name)
            fac = FACTION_DIR[section]
            open_page(f"{fac}/{subsection}/{slug}.md", unit_name)
            continue

        # default: append to current page
        append(line)

    # Write all pages
    written = 0
    for rel_path, content_lines in pages.items():
        if rel_path in KEEP_EXISTING:
            continue
        out_path = TARGET_DIR / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        while content_lines and content_lines[-1].strip() == "":
            content_lines.pop()
        out_path.write_text("\n".join(content_lines) + "\n", encoding="utf-8")
        written += 1

    print(f"Wrote {written} pages\n")
    for path in sorted(pages.keys()):
        print(f"  {path:65s} ({len(pages[path])} lines)")


if __name__ == "__main__":
    main()
