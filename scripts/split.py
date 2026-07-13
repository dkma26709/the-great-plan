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
# (armies/index.md survives via KEEP_EXISTING)
WIPE_DIRS = [
    "rules",
    "magic",
    "armies",
    "misc",
]

# Factions whose public pages come from their master-file section (§10, §14-§17).
# Every other units/<Faction> folder is a reference roster, rendered by
# reference_faction_pass() from FACTION.md + per-unit profile.md files.
MASTER_SECTION_FACTIONS = {
    "Lizardmen", "Empire", "Ogre Kingdoms", "Vampire Counts", "Bretonnia",
}


# Bullet-link pattern used inside faction tier subsections (Core / Special /
# Rare / Characters / Character Mounts) and §18. Format produced by the
# 2026-05-05 master shrink, optionally followed by an italic annotation:
#   - [Saurus Warriors](units/Lizardmen/Saurus%20Warriors/profile.md)
#   - [The Fay Enchantress](units/Bretonnia/The%20Fay%20Enchantress/profile.md) *(named, Unique — …)*
UNIT_BULLET_RE = re.compile(
    r"^- \[([^\]]+)\]\(units/([^/]+)/([^/]+)/profile\.md\)(?:\s+.*)?$"
)


# Relative .md links inside profile bodies point at the private tree
# (./design.md, ../<Unit>/profile.md, ../FACTION.md, lore files) — unwrap
# them to plain text on the public site.
RELATIVE_MD_LINK_RE = re.compile(
    r"\[([^\]]+)\]\((?!https?://|#)[^)]*\.md(?:#[^)]*)?\)"
)


def slurp_profile(faction_dir_name: str, unit_dir_name: str) -> str | None:
    """Read a unit profile.md from the private repo and prep it for MkDocs.

    Strips the H1 title (MkDocs derives it from the page) and the
    `## References` section (links to design.md / lore source files that
    don't exist in the public tree). Unwraps private-tree relative links.
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

    out = [RELATIVE_MD_LINK_RE.sub(r"\1", ln) for ln in out]

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


# Relative profile.md links inside FACTION.md files:
#   [Orc Boyz](Orc%20Boyz/profile.md)          — same-faction
#   [War Lions](../High%20Elves/War%20Lions/profile.md) — cross-faction
FACTION_MD_LINK_RE = re.compile(r"\]\(((?:\.\./)?[^)]*?)/profile\.md\)")


def rewrite_faction_md_links(line: str) -> str:
    """Rewrite FACTION.md-relative profile.md links to public unit pages."""
    def repl(m):
        target = urllib.parse.unquote(m.group(1))
        if target.startswith("../"):
            parts = target[3:].split("/")
            if len(parts) == 2:
                other_faction, unit = parts
                return f"](../{slugify(other_faction)}/units/{slugify(unit)}.md)"
            return m.group(0)
        return f"](units/{slugify(target)}.md)"
    return FACTION_MD_LINK_RE.sub(repl, line)


def sanitize_faction_md(text: str, faction_name: str) -> list[str]:
    """Prep a FACTION.md for the public site.

    - H1 replaced with the plain faction name (nav title)
    - `## Anchors` section stripped (references private file paths)
    - `> **Design diary:**` blockquotes stripped
    - relative profile.md links rewritten to public unit pages
    """
    out = [f"# {faction_name}", ""]
    skipping_section = False
    skipping_diary = False
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    for ln in lines:
        if skipping_diary:
            if ln.startswith(">"):
                continue
            skipping_diary = False
            if ln.strip() == "":
                continue
        if ln.startswith("> **Design diary:**"):
            skipping_diary = True
            continue
        if ln.startswith("## "):
            skipping_section = ln.startswith("## Anchors")
            if skipping_section:
                continue
        if skipping_section:
            continue
        ln = rewrite_faction_md_links(ln)
        # Unwrap any remaining private-tree links (design.md, FACTION.md, …)
        ln = re.sub(
            r"\[([^\]]+)\]\([^)]*(?:design|FACTION|Lore)[^)]*\.md(?:#[^)]*)?\)",
            r"\1", ln)
        out.append(ln)
    while out and out[-1].strip() == "":
        out.pop()
    return out


def reference_faction_pass(pages: dict[str, list[str]]):
    """Render units/<Faction> folders not covered by a master-file section.

    Each becomes armies/<faction-slug>/ with an index.md (sanitized FACTION.md,
    or a minimal auto-index when absent) and units/<slug>.md per profile.md.
    The folder scan is the source of truth — a unit ships as soon as its
    profile.md exists, regardless of §18 bullets or FACTION.md link lists.
    """
    for fdir in sorted(UNITS_DIR.iterdir()):
        if not fdir.is_dir() or fdir.name in MASTER_SECTION_FACTIONS:
            continue
        unit_dirs = [d for d in sorted(fdir.iterdir())
                     if d.is_dir() and (d / "profile.md").exists()]
        if not unit_dirs:
            continue
        fslug = slugify(fdir.name)
        base = f"armies/{fslug}"

        faction_md = fdir / "FACTION.md"
        if faction_md.exists():
            pages[f"{base}/index.md"] = sanitize_faction_md(
                faction_md.read_text(encoding="utf-8"), fdir.name)
        else:
            body = [
                f"# {fdir.name}", "",
                "> Reference roster — units drafted for cross-faction "
                "calibration (§18); full-faction promotion pending.", "",
                "**Drafted units:**", "",
            ]
            body += [f"- [{d.name}](units/{slugify(d.name)}.md)"
                     for d in unit_dirs]
            pages[f"{base}/index.md"] = body

        for d in unit_dirs:
            profile_body = slurp_profile(fdir.name, d.name)
            if profile_body is None:
                continue
            page = [f"# {d.name}", ""]
            page += profile_body.splitlines()
            pages[f"{base}/units/{slugify(d.name)}.md"] = page


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

        # §18 cross-faction reference — reference units now have real pages
        # under armies/<faction>/units/ (reference_faction_pass), so the misc
        # page links to them instead of inlining duplicates.
        if section == "18":
            mb = UNIT_BULLET_RE.match(line)
            if mb:
                unit_name = mb.group(1).strip()
                faction_dir_name = urllib.parse.unquote(mb.group(2))
                unit_dir_name = urllib.parse.unquote(mb.group(3))
                fslug = slugify(faction_dir_name)
                uslug = slugify(unit_dir_name)
                append(f"- **[{unit_name}](../armies/{fslug}/units/{uslug}.md)** "
                       f"*({faction_dir_name})*")
                continue

        # default: append to current page
        append(line)

    # Reference rosters — units/<Faction> folders without a master section
    reference_faction_pass(pages)

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
