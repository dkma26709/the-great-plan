#!/usr/bin/env python3
"""
Split the monolithic core-rules-draft.md into per-page MkDocs files.

Sources (post 2026-05-05 master shrink):
- core-rules-draft.md — rules, faction overviews, AoI tables, faction
  mechanics, and (in faction tier sub-sections) bullet links of the form
  `- [Name](units/<Faction>/<Name>/profile.md)` pointing at per-unit cards.
- units/<Faction>/<Unit>/profile.md — structured per-unit card files; the
  source of truth for unit profile content.

For each tier-section bullet, the splitter copies the corresponding
profile.md into the public site as armies/<faction>/<tier>/<slug>.md
(stripping the H1 and References section). §18 cross-faction reference
units are inlined into a single misc page.
"""

import re
import shutil
import urllib.parse
from pathlib import Path

PRIVATE_ROOT = Path("C:/PersonalRepos/Warhammer Hybrid Ruleset")
SOURCE_FILE = PRIVATE_ROOT / "core-rules-draft.md"
UNITS_DIR = PRIVATE_ROOT / "units"
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
    "10": "armies/lizardmen",
    "14": "armies/empire",
    "15": "armies/ogre-kingdoms",
    "16": "armies/vampire-counts",
    "17": "armies/bretonnia",
}

GENERAL_LORES = {"Heavens", "Beasts", "Fire", "Light", "Life", "Death", "Shadow", "Metal"}
FACTION_LORES = {"Geomancy", "Cosmic Architecture", "Necromancy", "the Lady"}

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
    "armies/lizardmen",
    "armies/empire",
    "armies/ogre-kingdoms",
    "armies/vampire-counts",
    "armies/bretonnia",
    "misc",
]


# Bullet-link pattern used inside faction tier subsections (Core / Special /
# Rare / Characters / Character Mounts) and §18. Format produced by the
# 2026-05-05 master shrink:
#   - [Saurus Warriors](units/Lizardmen/Saurus%20Warriors/profile.md)
UNIT_BULLET_RE = re.compile(
    r"^- \[([^\]]+)\]\(units/([^/]+)/([^/]+)/profile\.md\)\s*$"
)


def slurp_profile(faction_dir_name: str, unit_dir_name: str) -> str | None:
    """Read a unit profile.md from the private repo and prep it for MkDocs.

    Strips the H1 title (MkDocs derives it from the page) and the
    `## References` section (links to design.md / lore source files that
    don't exist in the public tree).
    """
    src = UNITS_DIR / faction_dir_name / unit_dir_name / "profile.md"
    if not src.exists():
        return None
    text = src.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Strip leading H1 + following blank
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        if lines and lines[0].strip() == "":
            lines = lines[1:]

    # Strip `## References` section to end-of-file (or until next ## header)
    out = []
    skipping = False
    for ln in lines:
        if ln.startswith("## References"):
            skipping = True
            continue
        if skipping and ln.startswith("## "):
            skipping = False
        if not skipping:
            out.append(ln)

    while out and out[-1].strip() == "":
        out.pop()

    return "\n".join(out) + "\n"


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
    skipping_diary = False

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
        # Strip private "Design diary" blockquotes — staging-only design rationale,
        # not for the public site. Skip the marker line, all contiguous blockquote
        # lines, and the single trailing blank that separates the block from
        # whatever follows.
        if skipping_diary:
            if line.startswith(">"):
                continue
            if line.strip() == "":
                skipping_diary = False
                continue
            skipping_diary = False
            # fall through to process this non-blockquote line normally

        if line.startswith("> **Design diary:**"):
            skipping_diary = True
            continue

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

        # Unit-bullet line inside a tier subsection — copy the corresponding
        # profile.md from the private units/ tree into the public site.
        if (
            section in FACTION_DIR
            and subsection in {"core", "special", "rare", "characters", "mounts"}
        ):
            mb = UNIT_BULLET_RE.match(line)
            if mb:
                unit_name = mb.group(1).strip()
                faction_dir_name = urllib.parse.unquote(mb.group(2))
                unit_dir_name = urllib.parse.unquote(mb.group(3))
                slug = slugify(unit_name)
                fac = FACTION_DIR[section]
                page_path = f"{fac}/{subsection}/{slug}.md"
                profile_body = slurp_profile(faction_dir_name, unit_dir_name)
                if profile_body is None:
                    print(f"  [warn] missing profile.md for {unit_name} "
                          f"(looked in units/{faction_dir_name}/{unit_dir_name}/)")
                    continue
                open_page(page_path, unit_name)
                for ln in profile_body.splitlines():
                    append(ln)
                continue

        # §18 cross-faction reference — inline each unit's profile (no per-unit
        # pages — keep all 7 reference units on a single misc page since they
        # are calibration data, not a faction commitment).
        if section == "18":
            mb = UNIT_BULLET_RE.match(line)
            if mb:
                unit_name = mb.group(1).strip()
                faction_dir_name = urllib.parse.unquote(mb.group(2))
                unit_dir_name = urllib.parse.unquote(mb.group(3))
                profile_body = slurp_profile(faction_dir_name, unit_dir_name)
                if profile_body is None:
                    print(f"  [warn] missing profile.md for {unit_name} "
                          f"(§18, looked in units/{faction_dir_name}/{unit_dir_name}/)")
                    continue
                # Demote inlined `## ` headers to `### ` (and `### ` to `#### `)
                # so each reference unit sits as a `## ` block under the misc H1.
                append(f"## {unit_name} *({faction_dir_name})*")
                append("")
                for ln in profile_body.splitlines():
                    if ln.startswith("## "):
                        append("#" + ln)
                    elif ln.startswith("### "):
                        append("#" + ln)
                    else:
                        append(ln)
                append("")
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
