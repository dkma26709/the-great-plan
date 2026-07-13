# Frostheart Phoenix

> The aged form of Asuryan's firebird. "As a Flamespyre Phoenix ages, its body cools, and even begins to sap heat from its surroundings. Finally, the plumage that once blazed with fire grows heavy with frost and ice. Once this occurs, the Phoenix must leave the Flamespyres." The Frostheart is the *same biology* as the Flamespyre Phoenix, but transformed by age — instead of burning, it freezes; instead of radiating heat, it draws heat *out* of the world around it. Where Flamespyre fights via *active flame damage* (Wildfire AoE), Frostheart fights via *passive cold debuff* (enemies in range strike slower and less accurately). Both are sacred to Asuryan; both have the Fiery Rebirth resurrection mechanic (despite the cold-aspected aura — the rebirth-flame is the Phoenix's *core* magical essence, not its current elemental expression). The lore signature is twofold: **Cold Aura** *(passive debuff — enemies within 6\" strike at -1 to-Hit and -1 I in melee, modelling the chilling presence)* and **Fiery Rebirth** *(shared with Flamespyre — when slain, roll D6, on 4+ the Phoenix returns at half W)*. Drafted here as the **Hero-tier Monster Mount profile** for High Elf Anointed of Asuryan characters (same canonical rider as the Flamespyre; the rider can ride either variant). Sister-piece: Flamespyre Phoenix. The High Elf battlefield read: where a Flamespyre Phoenix-mounted Anointed presses an offensive aura, a Frostheart Phoenix-mounted Anointed *enables* the Anointed's own ASF strikes and disrupts enemy retaliation across a 6" radius — pure defensive-debuff Hero-mount.

## Profile

**Frostheart Phoenix (Mount profile):**
| M | MA | MD | BS | S | T | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|----|-----|----|
| 1 | 5 | 5 | 0 | 4 | 6 | 7 | 4 | 8 | 4 | =W |

**Points:** +140 added to the rider's base cost (Frostheart Phoenix + Rider combined per Rider and Mount Profiles §1). *(Framework derivation under §13: stat-baseline 18.5 + rules 16.5 + equipment 5.0 = 40.0 raw × wound factor 4.36 (W 7) × 0.8 scaling = 139.5 → +140. **Pass 2 (2026-05-18):** T 5 → T 6 (aged Phoenix biology more durable, +1.5 raw); I 6 → I 4 (cold-slowed reflexes, -1.0 raw); Cold Aura significantly buffed (-2 MA / -2 MD / -2 I in 6", -4 I vs Cold-Blooded; +3.0 raw); Attuned to the Winds variable Ward added (+1.5 raw). Pass 1 reported +105 due to an arithmetic error — corrected to +122 in Pass 2 baseline, then +140 with the user's buffs. Frostheart is the heaviest debuff Phoenix in the codebase. See `design.md` for full working)*

**Unit size:** 1 (combined model — Anointed of Asuryan Hero rider + Frostheart Phoenix mount)

**Unit type:** Monster Mount (single model combining Frostheart Phoenix + Rider — see §1 Rider and Mount Profiles)

**Natural Armour:** 5+ (Phoenix plumage — *frost-rimed* and hardened with age; the cold has thickened the feathers into ice-touched armour. **Contrast:** Flamespyre has no NA (young plumage burns rather than armours); Arcane has no NA (blazing feathers turn arrows via magical means, not via armour). The Frostheart is the only Phoenix variant with a fixed Natural Armour, reflecting the aged-cold biology specifically)

**Fly:** 8" (per §8)

**Base Size:** 50mm × 100mm

**Keywords:** High Elves, Asur, Phoenix, Frostheart, Monster, Character Mount, Magical Creature

## Equipment

- **Equipment:** Talons-and-Beak (natural — apex Phoenix talons + frost-touched beak) + Cold Aura (passive aura — see Special Rules). No worn armour, no shield, no rider weapons.

## Special Rules

- **Terror** *(Psychology — per §8)* — at LiS 4, the Terror aura projects to **(6 + 4)" = 10"**. A frost-rimed sacred firebird of Asuryan registers as terror — the icy chill that precedes it amplifies the morale impact.
- **Fly (8")** *(per §8)*.
- **Magical Attacks** *(per §8 — Phoenix biology intrinsic)* — all of the Frostheart Phoenix's attacks (Talons-and-Beak; the Cold Aura is a debuff, not an attack) count as Magical Attacks.
- **Cold Aura** *(Frostheart Phoenix unit identity rule — Pass 2: heavy debuff aura)* — All enemy units with any model **within 6"** of the Frostheart Phoenix suffer the following melee penalties:

  - **-2 to MA** (their melee strikes hit on worse rolls — e.g., MA 5 → effective MA 3)
  - **-2 to MD** (they're easier to hit in return — e.g., MD 5 → effective MD 3)
  - **-2 to Initiative** (their strikes resolve later — e.g., I 5 → effective I 3)
  - **Additional -2 Initiative if the target unit has the Cold-Blooded keyword** *(Lizardmen-specific counter — total -4 I on Cold-Blooded units, neutralising the slow-reaction biology with even worse cold)*

  **Lore-direct:** "the Phoenix begins to sap heat from its surroundings" — the cold *drains* battlefield-energy, freezes muscle reflexes, and dulls every blow. The -4 I vs Cold-Blooded captures the Frostheart Phoenix as the *definitive* anti-Lizardmen mount — Cold-Blooded biology is already slow-reacting, and the Frostheart's cold compounds the deficit to crippling levels.

  **Range:** 6" from the Phoenix's base. Applies to **all** enemy units in range, not just the one in base contact. Multiple enemy units within 6" all suffer the full penalty package.

  **Tactical implication:** the Frostheart Phoenix swings the combat math 2 steps in its favour on both offence AND defence per attack. Most enemy units within 6" effectively gain "Phoenix-targeted" status — their accuracy halved, their defence halved, their reflexes slowed. The Frostheart-mounted Anointed of Asuryan in a 6"-radius melee swirl is one of the most *durable and dominant* combat configurations in the codebase.

- **Attuned to the Winds** *(Phoenix-shared identity rule — variable Ward save scaling with the Magic phase)* — At the start of each **Magic phase**, after both Power and Dispel pools are determined, roll a **D6**. The result determines the Frostheart Phoenix's Ward Save for the rest of this turn:

  | D6 | Ward this turn |
  |---|---|
  | **1-2** | None (the winds are still) |
  | **3-4** | **Ward 6+** |
  | **5** | **Ward 5+** |
  | **6** | **Ward 4+** |

  Shared with the Flamespyre and Arcane Phoenix. The Ward applies to all incoming wounds.

- **Fiery Rebirth** *(Frostheart Phoenix unit identity rule — once-per-battle resurrection)* — Identical to the Flamespyre Phoenix's Fiery Rebirth rule. When this model is reduced to 0 W, **immediately roll a D6 before the model is removed**. On a **4+**, the Phoenix is *not* removed — instead:

  1. The Phoenix is restored to **half its starting Wounds, rounded up** (W 7 → 4 W remaining).
  2. The model stays at its current position.
  3. **If the rider was attached**, the rider is removed from play permanently — only the Phoenix returns.
  4. **Fiery Rebirth may trigger only ONCE per battle**.

  On a **1-3**, the Phoenix is removed normally.

  **Lore note for Frostheart specifically:** despite the Frostheart's cold-aspected biology, the Fiery Rebirth retains the *fire* keyword — the rebirth-flame is the Phoenix's *core* magical essence, not its current elemental expression. A Frostheart that rebirths emerges briefly as a fire-touched chick before re-cooling into its aged ice-aspect form.

## Weapon Profiles

### Close Combat

- **Talons-and-Beak** *(natural — apex Phoenix talons + frost-touched beak)* — **1" reach** | **A 3** | **S 4** | **AP -1** | **D 1** | **Magical Attacks** — three frost-touched strikes per Combat round. Identical to the Flamespyre's Talons-and-Beak profile (same biology). The Phoenix's direct melee output is modest; its real value comes from the Cold Aura debuff. `[Natural, Magical]`
