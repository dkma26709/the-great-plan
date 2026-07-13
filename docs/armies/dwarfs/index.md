# Dwarfs


> The Dawi of the Karaz Ankor. Short, stocky, tough, slow. Three centuries' lifespan, master-craftsmen of the great underground holds and mountain fastnesses. **Stubborn**, **grudge-bearing**, **naturally magic-resistant**. Where Asur channel the Winds, dwarfs *deny* magic — runic engineering and gunpowder stand in for traditional spellcraft. The cultural fingerprint: the *patient anvil* — slow to march, slower to forgive, but once committed, immovable. Every adult dwarf is drilled in axe and shield from boyhood; warrior-and-craftsman is the species baseline, with units distinguishing themselves through equipment-tier, oath, and inheritance rather than tactical doctrine.

## Status

**Currently classed as §18 Cross-Faction Reference** — a single representative unit (Dwarf Warriors) at present, with full-faction promotion deferred until the roster is broader. This document is the design reference for future Dwarf unit drafts: it captures the philosophy, sub-cult axes, and constraints that should hold across the faction so each unit's design loop starts from a shared baseline.

**Drafted units:** [Dwarf Warriors](units/dwarf-warriors.md), [Slayers](units/slayers.md), [Hammerers](units/hammerers.md).

## Cultural identity — the patient anvil

The Dwarf cultural axis is **anvil-defensive**, in productive contrast to the offensive valences of other factions:

| Faction | Cultural axis | Combat valence |
|---|---|---|
| **Asur** (High Elves) | Disciplined skill | Defensive precision |
| **Druchii** (Dark Elves) | Khainite lethality | Offensive frenzy |
| **Greenskins** | Love the fight, unreliable | Offensive chaos |
| **Lizardmen** (Saurus) | Spawn-bred warrior-cult | Offensive cascade |
| **Dwarfs (Dawi)** | **Patient anvil, grudge-keeper** | **Defensive immovable, anti-magic resilient** |

Dwarfs don't *charge* — they *receive* and *hold*. They don't *evade* — they *grind*. They don't *cast* — they *engineer*. Every mechanical decision should reinforce these axes.

### Dwarf MA < MD — the patient-anvil cultural axis (locked 2026-05-15)

**Dwarfs have higher MD than MA at every tier except the explicit Slayer cult exception.** This is the codebase's first explicit MA < MD cultural-axis lock — the patient-anvil identity made stat-mechanical. The Dwarf doesn't *strike* first; he *blocks* first (HW + shield Parry), then strikes back. MD > MA expresses this directly:

- **Dwarf Warriors:** MA 4 / MD 5
- **Hammerers:** MA 5 / MD 6 (King's Guard apex — best at both, but MD still leads)
- **Slayers:** MA 5 / MD 3 (the cult exception — Slayers *shed* defence for offence; their cult-rule signature is the inversion of the Dwarf axis, which makes them the explicit *anti-Dwarf* on this dimension)
- **Pending (Ironbreakers / Longbeards):** project MA 4 / MD 6 (apex-defensive specialist) and MA 4 / MD 5 (veteran-elder) per the cultural axis baseline

No other faction has this MD-leaning default — it is uniquely Dwarven. Greenskins are MA > MD (Boyz 4/3, frenzied offence-leaning), Druchii MA > MD at the cult tier (Witch Elves 5/3), Asur balanced (MA ≈ MD), Asrai projected skirmisher-evader (MA ≤ MD but with low T fragility, not Dwarven anvil-toughness). The Dwarven anvil-fingerprint is the lore-iconic "we hold, you break upon us" expressed at the stat-axis level.

## Stat patterns

**Dwarf baseline** (per §13, with the MA < MD axis locked 2026-05-15):

| M | MA | MD | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 3 | 4 | **5** | 3 | 3 | 4 | 1 | 2 | 1 | 10 | — |

**Cross-faction +1 Res convention applied** — Dwarfs at Res 10 sit at the rank-and-file morale cap, parity with Saurus Warriors, reflecting the iron stoicism that defines dwarf identity. Per the disciplined-faction convention (Empire State Troops at Res 8-9, Asur at Res 9, Druchii at Res 9, Bretonnia Knights at Res 9-10, Dwarfs at Res 10).

**Stat ladder for Dwarf units** (drafted or expected):

| Tier | Indicative M | MA | MD | S | T | W | I | Res | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Core rank-and-file** | 3 | 4 | 4 | 3 | 4 | 1 | 2 | 10 | Dwarf Warriors *(drafted, 13 pts)* |
| **Longbeards (veteran elite)** | 3 | 4 | 5 | 4 | 4 | 1 | 2 | 10 | Older / more experienced; +1 S, extended grudge bonuses. Pending. MD 5 per the Dwarf MA < MD axis |
| **Hammerers (King's Guard)** | 3 | 5 | 6 | 4 | 4 | 1 | 2 | 10 | Hammerers *(drafted, 22 pts — heavy armour + Great Hammer (A 2 / S+2 / AP -2 / D 1 / -1 I), Personal Oath (conditional Unbreakable when joined by or within 6" of a friendly Dwarf Character), no Killing Blow)*. Royal bodyguard sub-cult — apex defensive-offensive on the Dwarf MA < MD axis (MA 5 / MD 6: best at both, MD leading) |
| **Ironbreakers (subterranean elite)** | 3 | 4 | 6 | 3 | 4 | 1 | 2 | 10 | Apex defensive — 3+ baseline save + gromril plate; cave-fighter mechanics. Pending. MD 6 per the Dwarf MA < MD axis (the *defensive specialist* sub-cult — Hammerers and Ironbreakers both at MD 6 but with offensive (Hammerers MA 5) vs defensive (Ironbreakers MA 4) sub-tier separation) |
| **Slayer Cult (death-seekers)** | 3 | 5 | 3 | 4 | 4 | 1 | 3 | 10 | Slayers *(drafted, 17 pts — no armour, Death Oath (Unbreakable + Permanent Frenzy), Slayer Strike (KB Large 2 + +1 to-Wound vs Large), paired Slayer Axes)*. **The cult exception to the Dwarf MA < MD axis** — Slayers *shed defence for offence* (MA 5 / MD 3), inverting the Dwarven anvil signature; their cult identity is the explicit inversion of the faction's cultural axis |
| **Thunderers (handgunners)** | 3 | 4 | 5 | 3 | 4 | 1 | 2 | 10 | Drilled handgun infantry; Empire State Trooper parallel. Pending. MD 5 per the Dwarf MA < MD axis |
| **Quarrellers (crossbow infantry)** | 3 | 4 | 5 | 3 | 4 | 1 | 2 | 10 | Crossbow loadout, low-tech volley fire. Pending. MD 5 per the Dwarf MA < MD axis |
| **War machines** | — | — | — | varies | — | varies | — | — | Cannons, Grudge Throwers, Organ Guns, Flame Cannons; engineered firepower. Pending |
| **Gyrocopters / Gyrobombers** | varies (Fly) | 4 | 4 | varies | 4 | varies | varies | 10 | The *only* "flight" available to the species — steam-powered engineering. Pending |
| **Hero characters** | 3 | 5-6 | 5-6 | 4-5 | 4 | 2-3 | 2-3 | 10 | Thanes, Runesmiths, Engineers. Pending |
| **Lord characters** | 3 | 6-7 | 6-7 | 5-6 | 4 | 4-5 | 3-4 | 10 | Kings, Runelords, Slayer Kings. Pending |
| **Anvil of Doom (Lord-tier shrine)** | — | — | — | — | — | 4-5 | — | 10 | Runelord-borne battlefield rune-magic platform. Pending |

## Biological constraints

The shared Dwarf-species ceiling (per §13) is hard:

- **M 3 baseline** — dwarfs are slow; **no species-wide M-bump option**. The slowest M of any major-faction species. Hard-coded biological.
- **I 2 baseline at rank-and-file** — apex Black Orcs reach I 3 (the Karaz Ankor's "fastest" Dwarfs are *still* slower than most species).
- **W 1 rank-and-file**, **W 2-3 Hero-tier**, **W 4-5 Lord-tier** — modest scaling. Dwarfs are not Saurus / Ogre bulk.
- **No traditional Wind magic** — Dwarfs do not channel the Winds. Dwarf magic comes exclusively from **runic engineering, Anvil-of-Doom rituals, and gunpowder**, not spell lores. A Dwarf "Wizard" character does not exist; Runelords / Runesmiths use bound-rune magic items, not lore-cast spells. Runic magic is a deferred design space per §11 (pending dedicated treatment).
- **No flight, no aquatic specialisation** at the biological level. Gyrocopters / Gyrobombers (steam engineering) are the *only* flight in the Dwarf roster.
- **Cultural disinclination toward magic items** beyond runic-engineered equivalents — no scrolls, no traditional wizard tools.

## Faction-wide rules

All Dwarf units carry the following at minimum (species-biological + cultural):

- **Stubborn** *(faction-wide, per §8 Psychology)* — ignores Shaken / Wavering state effects. Iconic Dwarf stoicism universal across the roster; every clan-warrior holds the line at the same base steadiness. Only Broken state effects fully degrade Dwarf units.
- **Ancestral Grudge** *(faction-wide — see §8 Hatred)* — **Hatred against Greenskins, Skaven, Trolls, Beastmen.** The Book of Grudges manifests; reroll failed to-Hit in first round of combat against the four traditional Dwarf enemies. Lore-deep; mechanically narrow-target.
- **Resolute** *(faction-wide morale trait)* — combat-resolution-loss-to-stress conversion reduced by 1 (minimum 0). The "iron stoicism" extended into combat morale — Dwarfs absorb post-combat stress at a discounted rate.
- **Magic Resistance (1)** *(faction-wide species trait, per §8 Defence)* — **-1 to enemy cast rolls** targeting any Dwarf unit. The dwarven body and soul reject the Winds; spells skip off them more readily than they would mortal humans. *Biological*, not equipment-based — every Dwarf inherits it.
- **Disciplined** *(typical, not universal)* — most rank-and-file and elite Dwarfs are drilled veterans. +1 to Recovery rolls. **Exception: Slayer Cult units are NOT Disciplined** — the death-seeking berserk identity supersedes the cult-trained discipline.
- **Heavy armour standard at rank-and-file** — Dwarfs are the only species in the ruleset where Heavy armour is the *default*, not an upgrade. **Exceptions: Slayer Cult (forsake all armour as part of the Oath); Thunderers / Quarrellers (light or medium armour to balance ranged kit weight).**

## Sub-cult scaling rules

Dwarf units scale above the rank-and-file baseline along multiple axes, each named for a culture-clan-or-oath:

**Longbeards (veteran rank-and-file):**
1. +1 S (S 3 → 4) — old Dwarf brawn from centuries of training.
2. Extended Ancestral Grudge — reroll failed to-Wound in addition to to-Hit (the Old Grudges have *teeth*).
3. Optional Longbeard-only Magic Standards.

**Hammerers (King's Guard — *drafted*):**
1. +1 MA (MA 4 → 5) — apex Dwarf melee skill.
2. **Personal Oath** — conditional **Unbreakable** when joined by or within 6" of a friendly **Dwarf Character** (King / Thane / Runelord / Runesmith). Reverts to baseline Stubborn when no Character is in range. Forward-compatible with future Dwarf-character drafts; synthesises pre-8e "Stubborn only with the King" with 8e "Stubborn unconditional" — Stubborn is the faction-wide floor, Personal Oath is the conditional cap.
3. Two-handed Great Hammer — S+2 AP -2 D 1, -1 I, A 2 (the cult's drilled-veteran offensive fingerprint per WHFB 8e canon). **No Killing Blow** in the v1 draft — the raw S 6 / AP -2 / A 2 profile is the entire offensive identity; KB vs Cavalry held for cross-roster consistency pass.
4. **Heavy armour standard** — full-kit King's-Guard loadout; no shield (great hammer is 2H), no kit-options.
5. Tier role: defensive-offensive apex on the disciplined-anvil axis. Slayers break the anvil pattern (no armour, Permanent Frenzy); Hammerers *double down on it* (heavy armour, Oath morale-floor, drilled veteran melee).

**Ironbreakers (subterranean elite):**
1. +1 MD (MD 4 → 5) — gromril plate + cave-fighter discipline.
2. **3+ baseline save** — Heavy armour + Heavy Shield + gromril upgrade (uniquely available to Ironbreakers).
3. Subterranean Pursuit — better in tight-corridor / building / underground terrain.

**Slayer Cult (death-seekers — *drafted*):**
1. **Forsake all armour** — no save baseline; the Oath is the protection.
2. **No Disciplined / No Stubborn** — replaced by **Death Oath** (Unbreakable + Permanent Frenzy). Unbreakable strictly supersedes Stubborn (full no-stress + no-state-effects + Imm Psych); Permanent Frenzy guarantees the F4 fingerprint from deployment to death.
3. **Slayer Strike** — anti-Large Killing Blow + to-Wound bonus.
4. +1 MA, +1 S over rank-and-file (berserk warrior-skill).
5. Tier progression by combat tally: Trollslayer (rank-and-file) → Giant Slayer (Veteran/Champion) → Dragon Slayer / Daemon Slayer (Hero/Lord characters).

**Thunderers / Quarrellers (ranged infantry):**
1. Handgun or Crossbow as primary; melee kit secondary.
2. Light or Medium armour (to balance the weight of the ranged weapon).
3. Identity rule probably "Drilled Volley" or similar — Dwarfs are the *steadiest shooters* in the codebase.

## Equipment patterns

- **Dwarf Axe** *(rank-and-file 1H baseline)* — AP -1 (Dwarf craft baseline matches Orc Choppa); the iconic weapon.
- **Hammers / Mauls / Great Weapons** — 2H S+2 AP -1 typically; sometimes with Killing Blow (Cavalry) for Hammerers.
- **Crossbows / Handguns** — Quarreller / Thunderer ranged loadout. Drilled-volley shooters at S 4 (crossbow) or S 4 AP -1 (handgun).
- **Cannons / Grudge Throwers / Organ Guns / Flame Cannons** — Dwarf war machines, every one with engineering runes inscribed. Pending §10-style faction-mechanics treatment.
- **Heavy armour standard at rank-and-file** — uniquely in the codebase, this is the *default* not an *upgrade*.
- **Gromril plate** — Ironbreaker-exclusive upgrade; 3+ baseline. **Pending — first non-existing dwarf armour tier per the ruleset.**
- **Slayer's nothing** — Slayers carry only axes, no armour at all. Lore-explicit.

## Magic — Runic Engineering, not Lore-casting

**Dwarf magic is not channelled from the Winds.** Instead, **Runesmiths** and **Runelords** inscribe runes onto weapons, armour, standards, and equipment, capturing arcane effects in *engineered* form. Five rune categories per §13:

- **Weapon Runes** (offensive)
- **Armour Runes** (defensive)
- **Runic Standards** (banner-borne battlefield effects)
- **Runic Talismans** (character-borne wards / utility)
- **Engineering Runes** (war-machine-specific)

The **Anvil of Doom** is the highest-tier Runelord platform — a battlefield rune-magic device powered by direct dwarven ancestor-link. Rune-magic is *bound at forging*, not cast per turn — a dwarven army's magical depth is entirely list-build dependent. **Pending dedicated §11 Runic Magic treatment.** When drafted, the Runic system replaces the Wind-of-Magic Lore subsystem entirely for Dwarf armies.

**Master Engineers** (pending) — non-magical Hero characters; provide war-machine bonuses, gun-line modifiers, and engineering-rune access.

## Mounts and monsters

**No biological mounts.** Dwarfs reject biological monsters as allies; their cultural disinclination is total. No riding-beasts, no Cavalry-tier biology, no Monster mounts. The closest dwarven equivalents are **engineered**:

- **Gyrocopters / Gyrobombers** — steam-powered flying machines. The *only* "flight" available to a species with no biological flying biology. Single-Dwarf-piloted craft with rotor-blade rapid descent + Steam Gun ranged attack + bombing-run mechanics.
- **Steam Tanks** — note: lore-canonically the Empire fields the Steam Tank, but it was engineered with significant Imperial-Dwarven cooperation. Mechanically Empire-aligned, but the dwarven contribution is acknowledged in lore.
- **Anvil of Doom** — Runelord-borne shrine. Battlefield rune-magic platform.
- **No mounted character options** — Dwarf Lords / Thanes / Runelords fight on foot. The Anvil of Doom is the only "platform" a Dwarf Lord uses.

The faction expression of "monster-tier asset" is *engineered*, not *biological*. Dwarfs answer the Druchii War Hydra with the Cannon; answer the Bretonnian Lord on Pegasus with the Gyrocopter; answer the Carnosaur charge with massed Crossbow volleys.

## Pricing notes

**Pass 8 framework (0.8× scaling).** Sample anchors:

- **Dwarf Warriors 13 pts/model** (drafted). T 4 / Res 10 / 4+ save / Stubborn + Ancestral Grudge + Resolute + MR(1) + Disciplined + Grudgebearer.
- **Slayers 17 pts/model** *(drafted — T 4 / no save / Unbreakable + Permanent Frenzy + Slayer Strike + Dwarf faction-wide rules; paired Slayer Axes)*.

**Expected Dwarf ladder for undrafted units:** Longbeards ~16-18 / Ironbreakers ~18-22 (3+ save) / Thunderers ~14-16 / Quarrellers ~13-15 / Cannon team ~125-150 / Gyrocopter ~85-110 / Anvil of Doom + Runelord ~250-300.

**Drafted Special-tier ladder:** Slayers 17 pts (no save / Unbreakable + Permanent Frenzy + Slayer Strike) / Hammerers 21 pts (4+ save / Personal Oath conditional Unbreakable + Great Hammer A 2). Same Special tier, opposite tactical fingerprints (glass-cannon attacker vs defensive-offensive elite).

**Apply at draft:** trust the framework re-derivation. Dwarfs' faction-wide rule stack is rule-dense (5 rules at baseline: Stubborn / Ancestral Grudge / Resolute / MR(1) / Disciplined for most units) — the pricing reflects this baseline rule load, then layers unit-specific identity rules on top.

## Cross-faction comparators

Useful anchors when drafting a Dwarf unit:

| Comparator | Why it's useful |
|---|---|
| **Saurus Warriors (Lizardmen Core)** | The kin-comparator in the "stoic-tank biology" category. Both T 4 / W 1-3, both Res 10, both Disciplined + Stubborn. Saurus add Predatory Fighter + Cold-Blooded + Pack Cohesion + Locked Jaws + Fear; Dwarfs add Ancestral Grudge + Resolute + MR(1) + heavy armour 4+ standard. Different design valences (Saurus cohort-bred fury vs Dwarf engineered grudge), same defensive tier |
| **Bretonnian Knights of the Realm (Bretonnia Core cavalry)** | The cross-faction "chivalric-mountain-fortress" comparator. Both heavily armoured, both grudge-bearing (Bretonnia's Crusader's Vow vs Dwarf Ancestral Grudge). Different scales: Knights are M 10 mounted apex; Dwarfs are M 3 foot phalanx. Useful when calibrating Hammerers (King's Guard) against Reiksguard or Bretonnia Lord on warhorse |
| **Chaos Warriors (Mortal Chaos baseline)** | The non-elf elite ceiling. Both T 4 / 4+ save, both deeply disciplined. Chaos has Will of Chaos (Imm Psych + reroll Recovery); Dwarfs have Stubborn (state-effect immunity) + Resolute (CR-to-stress -1). Different morale tools, comparable cost tier |
| **Orc Boyz (Greenskin Core)** | The faction-enemy comparator. Dwarf Warriors hold the line vs the Orc charge: Stubborn + 4+ save vs Loves a Scrap + Choppa AP-1 charge. The Ancestral Grudge fires here (Dwarfs reroll to-Hit vs Greenskins) |
| **Witch Elves (Druchii frenzied cult)** | The contra-axis cult comparator for the upcoming Slayers draft. Both T 3-4 / W 1, both no-armour-by-cult-design, both Frenzy-based. Witch Elves go fragile-glass-cannon; Slayers go anti-Large death-seeker. Same "no save" identity, different fingerprint |

## Drafting hooks

Open Dwarf design questions, captured here for future unit passes:

- **Runic Magic system** — pending §11 dedicated lore-and-rune treatment. The Runesmith / Runelord / Anvil of Doom subsystem replaces traditional Wind-of-Magic Lores for Dwarf armies. Should be drafted before Runesmith/Runelord characters.
- **Resolute rule §8 promotion** — currently inlined on Dwarf Warriors profile; should be lifted to §8 when the next Dwarf unit (Slayers) is drafted. Following the Cold-Blooded / Disciplined / Elven Grace pattern.
- **Gromril armour tier** — Ironbreakers-exclusive 3+ baseline save (heavier than standard heavy armour). Needs system-wide treatment of "uniquely-Dwarf armour materials" — gromril is one canonical material, but mithril (elven) and others may need parallel treatment.
- **Slayer Cult sub-tier ladder** — Trollslayer (rank-and-file, drafting next) → Giant Slayer (champion / veteran) → Dragon Slayer / Daemon Slayer (Hero / Lord characters). The cult is a vertical tier rather than a horizontal sub-tribe. Future drafts should fill in the upper tiers.
- **Gyrocopters / Gyrobombers** — the *only* flight in the Dwarf roster. Steam-powered engineering aircraft. Pending future Cavalry-equivalent draft (treated as Flying Cavalry rather than Monster, despite the engineering basis).
- **Anvil of Doom** — Lord-tier shrine platform. Held for Runelord character draft + Runic Magic system.
- **Master Engineer character** — Hero-tier non-magical character; provides war-machine bonuses. Pending.
- **Dwarfen handgun / crossbow design** — Thunderers and Quarrellers need ranged-weapon profiles that distinguish them from Empire Handgunners / Crossbowmen. Dwarven craft = slightly better stats (AP -1 vs Empire AP 0?) or specialised mechanics (Move-or-Fire vs Quick-to-Fire trade-offs).
- **Slayer King (Ungrim Ironfist)** — apex named Lord-tier Slayer. Pending future character draft.
- **Gotrek Gurnisson** — apex named Slayer (one half of Gotrek and Felix). Held for named-character pass.
