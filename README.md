# The Great Plan

A custom Warhammer ruleset combining Age of Sigmar design philosophy with WAP / Old World stat granularity.

**Site:** [https://dkma26709.github.io/the-great-plan/](https://dkma26709.github.io/the-great-plan/)

## Status

Working draft. Pre-playtest. Open for comment.

The site is built from the Markdown files in `docs/` using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deployed automatically via GitHub Actions on every push to `main`.

## Local development

```bash
pip install mkdocs-material
mkdocs serve
```

Open [http://localhost:8000](http://localhost:8000) to preview.

## Contributing

Feedback, comments, and PRs welcome. Open an issue on this repository to discuss rules, balance, or design questions.

## Repository structure

```
docs/                       # Source content
├── index.md                # Front page (elevator pitch)
├── rules/                  # Core rules sections
└── armies/                 # Per-faction rosters and unit pages
    └── lizardmen/          # Lizardmen — proof-of-concept army

mkdocs.yml                  # Site configuration and navigation
.github/workflows/          # GH Actions deploy workflow
```
