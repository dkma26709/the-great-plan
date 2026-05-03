# The Great Plan

*A custom Warhammer ruleset combining Age of Sigmar design philosophy with WAP / Old World stat granularity.*

---

> *In the temple-cities of Lustria, the Slann record the cosmic blueprint on stone plaques. Every motion of every star, every echo of every battle, fitted into the Plan that orders reality. The Plan is not theirs alone — every faction in the Warhammer world exists within it, whether they know it or not. The Lizardmen are simply the only ones who follow it deliberately.*

---

## What this is

A custom tabletop wargame ruleset. WFB / WAP stat granularity, modernised combat flow, and a morale system that accumulates pressure instead of gambling on single-roll break tests.

If WHFB 8th felt like the right skeleton wearing the wrong skin, this is an attempt to put better muscle on the same bones.

## Five mechanical hooks

### Strength and Armour Penetration are decoupled

Strength affects to-wound only. Armour penetration is a weapon characteristic, not a derived statistic. A strong creature with blunt natural weapons wounds reliably but cannot force its way through plate. A weaker fighter with an enchanted blade cuts clean through but wounds less often. The "S7 monster pierces plate just by being big" problem is gone.

### No Leadership tests. Stress accumulates.

Every unit tracks a stress counter. Triggers — losing combat, taking casualties, being shot at, spells landing, being charged — add stress. Thresholds tied to Leadership turn into Shaken → Wavering → Broken states. No more "rolled double-six on the crucial Ld test, entire unit gone." Pressure builds, builds, then breaks.

### Free-form movement with real formation trade-offs

No mandatory rank-and-file, but a formation geometry system — Formed / Loose / Disordered — with genuine mechanical consequences.

- **Formed** (every model in base contact with 2+ others, shared facing): +1 Ld, absorb 2 CR before stress, charge resistance on the front arc.
- **Loose** (every model with no base contact, within coherency): extended charge, terrain immunity, harder to shoot at.
- **Disordered** (neither): no benefits.

### Combat drives positional outcomes, not routs

Losing a combat makes you fall back along a calculated path. The combat difference determines how far. No instant flee-and-pursue loops; no combats that evaporate a unit in one round from a single failed test. You lose ground, you take stress, and the fight continues on a new line next turn.

### Magic is per-wizard, not dice-pool roulette

Each wizard has its own magic profile — separate **Cast** and **Dispel** pools (dice contributed each Magic phase), **Channelling** for extra flexible dice on 5+s, **Cast / Dispel Bonus** modifiers capped at **+5**, **Dispel Range**, and tier-gated **Lore Access** (1-4: Basic / Intermediate / Advanced / Master).

Wizards roll from their own pools — no shared army-wide power dice, no dice-pool spam. Players alternate activations (cast / dispel) until both sides pass. A defensive Light wizard built around dispel is a genuinely different statline from an aggressive Vampire Lord built around offensive casts. Spells are tier-gated by Lore Access; a Level 1 caster cannot reach Master-tier capstones, structurally.

## Where to find what

- **[Rules](rules/index.md)** — core mechanics, stat lines, comparative tables, special rules glossary, magic system, points framework
- **[Armies](armies/index.md)** — faction rosters and unit profiles
    - [Lizardmen](armies/lizardmen/index.md) — proof-of-concept army; the most heavily iterated faction
    - More in progress: Empire, Ogre Kingdoms, Vampire Counts

## Status

**Working draft.** Foundational rules locked. Four factions partially drafted. Pre-playtest.

This is an evolving document, designed to be edited collaboratively as feedback comes in. Issues, comments, and PRs welcome on the [GitHub repository](https://github.com/dkma26709/the-great-plan).

---

*The Plan is older than memory. The plaques are weathered. The Slann do not write quickly.*
