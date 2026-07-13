# Clanrats

> *"When a Warlord gathers his might for war, the Clanrats are front and centre, occupying a key place in the battle-line."* The Clanrats are the rank-and-file warriors of the Skaven Under-Empire — generic clan-soldiery of the **Clan Mors** mould (black-and-red painted shields, the iconic Skaven look) and the equivalent across every Greater Clan. Individually, a Clanrat is a cowardly thing: lean-furred, sharp-toothed, treacherous, and quick to flee at the first sign of personal danger. **Banded together in great blocks of infantry**, however, the Clanrat becomes *ferocious* — attacking without hesitation against obviously superior enemies, secure in the knowledge that the rat next to him will probably die first. The species lore: *"banded together in large numbers, they are ferocious warriors, attacking without hesitation."* The fingerprint: **mass-bravery** (Verminous Valour grants the unit Shaken-immunity while at 75%+ strength, but the unit takes *compounded* stress when reduced below 50%); **Strength in Numbers** (deep formation grants a +1 CR bonus per 15-model rank-cluster, capping at +2 for 25+ models); **Backstabbing** (when this unit Breaks, the panic *spreads* — friendly Skaven units within 6" take +1 stress beyond the standard panic-cascade); **Undisciplined** (the species recovery penalty). The unit's role: throw bodies forward, win combats by mass and rank-bonus, and trust that the next clanrat-block will be moving up before this one disintegrates. The Skaven army doctrine is **attrition-by-Skaven** — the Warlord doesn't expect any one Clanrat unit to survive; he expects the army to *win* via the inexhaustible breeding of the warrens behind the line.

## Profile

| M | MA | MD | BS | S | T | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|----|-----|----|
| 5 | 3 | 3 | 3 | 3 | 3 | 1 | 4 | 5 | 1 | 1 |

**Points:** 4 per model *(framework derivation under §13: stat-baseline 5.0 + rules ~0.0 (net: Verminous Valour +1.0, Strength in Numbers +0.5, Backstabbing 0 (externality cost to allies, not this unit), Undisciplined -1.5) + equipment 0 (light armour matches §13.2 baseline 6+ save) = 5.0 raw × wound factor 1.0 (W 1) × 0.8 scaling = 4.0 → 4 pts; see `design.md` for full working)*

**Unit size:** 20+ (Skaven lore-canonical regiment size — Clanrats fight as massed blocks, not skirmish-units)

**Unit type:** Infantry

**Natural Armour:** —

**Base Size:** 25mm × 25mm

**Keywords:** Skaven, Under-Empire, Clan Mors *(default flavour-tag; sub-clan keyword adjustable at list-build)*, Clanrat, Infantry, Core

## Equipment

- **Worn armour (default):** Light armour (rusted scraps of chainmail and leather scavenged from the Under-Empire warrens; combined save **6+**)
- **Equipment (default):** Hand weapon + Light armour

## Special Rules

- **Undisciplined** *(per §8 Psychology)*. **-1 to Recovery rolls** (floor 1). The cowardly mass-tier Skaven baseline — Clanrats panic readily and recover poorly.
- **Verminous Valour** *(Skaven faction-wide identity rule — working title; pending §8 promotion when the second Skaven unit is drafted)*. **Mass-bravery / cowardice toggle, single threshold at half strength:**
  - While this unit has **more than half** its starting model count remaining (e.g., 11+ out of a 20-strong unit), it **ignores the state effect of Shaken** (per §8 — the standard -1 to-Hit and other Shaken consequences do not apply). The strength of the mass carries the Clanrat past minor stresses. Stress still accumulates normally; the Wavering and Broken thresholds still apply (Verminous Valour blocks the Shaken state effect specifically).
  - While this unit is reduced to **half or fewer** of its starting model count (e.g., 10 or fewer out of a 20-strong unit), it accumulates **+1 additional stress** every time it would normally take stress (combat-loss conversion, wounds, panic triggers, etc.). The mass has broken; cowardice manifests as compounded fear, and the depleted unit fails morale faster than its starting Resolve would predict.

  *(Lore-canonical: "ferocious in numbers, cowardly in isolation." Single half-strength threshold — above half, mass-bravery; at half or below, cowardice. Easy to track in play: count the models, check if it's above or at-or-below half. The Skaven player wants to keep Clanrat blocks intact and tightly massed; once a block dips to half, it routs *fast*.)*
- **Strength in Numbers** *(Skaven faction-wide identity rule — working title; pending §8 promotion)*. **Combat resolution bonus from raw model count — formation shape irrelevant:**
  - **+1 to CR** while this unit has **≥ 15 models** remaining.
  - **+2 to CR** while this unit has **≥ 25 models** remaining.
  - Counts current model count, not formation shape — a 15-model Clanrat blob in any arrangement (5×3 block, 10×2 line, 15×1 strung-out) gets the +1; a 25+ blob gets the +2. Skaven mass-bravery doesn't require formation discipline; the bodies are there or they aren't.
  - Stacks with the standard §6 Disciplined Depth Resolve bonus (which scales per full rank for stress-threshold purposes); Strength in Numbers is a *separate* CR-only identity rule expressing the species's combat-by-numbers fingerprint.

  *(Lore-canonical: the Skaven mass overwhelms the enemy line through sheer body count — wounds inflicted per combat round may favour the enemy, but the rank-bonus CR adjustment tips the resolution in the Clanrats' favour. The Warlord wins the field by mass, not by skill, and the rats don't bother with formation drill.)*
- **Backstabbing** *(Skaven faction-wide identity rule — working title; pending §8 promotion)*. When this unit is **Broken** (per §5 — reaches the Broken stress threshold and begins to flee), every friendly **Skaven** unit within **6"** of any model in this unit immediately gains **+1 stress** beyond the standard panic-cascade (per §5). The Skaven flee with such treachery and shrieking that allied Skaven units are *unsettled* — *"there go the cowards; we may be next."*

  *(Lore-canonical: Skaven panic spreads faster than any other species's. The mass-bravery edifice cracks the moment a block routs — the rest of the line feels the contagion. Mechanically captured as a faction-wide externality: every Skaven unit knows that its allies will panic-cascade harder than a Human or Elf army would. The rule applies symmetrically across the Skaven faction.)*

## Options

**Worn armour additive option:**
- **Shield** (+0.5 pt/model) → combined save **5+** (light armour 6+ → +1 step from shield, per §8 *Armour Save Stacking*). The Clan Mors black-and-red painted shield is the iconic Clanrat kit; this upgrade is taken by most Mors warriors in the canonical 8e roster.

**Equipment swap option (replaces Hand weapon, pick at most one):**
- **Spear** (+0.5 pt/model) → 2" reach, A 1, S 3, AP 0, D 1 — the cavalry-style rear-rank-fighting spear. Lets the second rank participate in melee, doubling the unit's combat output in a 2-rank-deep formation. Common in mass Clanrat blocks where the player wants maximum attack volume out of a deep regiment. *(Note: spear replaces hand weapon; cannot pair with hand weapon for additional A. May still pair with shield.)*

**Command options:**
- **Clawleader (Leader)** (+3 pts) — the unit's veteran warrior, promoted via successful backstabbing of the previous Clawleader. Carries no special stat bump; functions as the unit's champion for Rally / challenge / Leader-snipe purposes.
- **Standard Bearer** (+6 pts, may take Magic Standard up to 25 pts). The Mors banner-bearer carries the clan's black-and-red colours into battle, or — depending on sub-clan — the appropriate clan-banner equivalent.
- **Musician** (+3 pts) — the unit's drummer or piper; provides +1 to Recovery and Rally rolls. The clan-drum's beat is the only thing keeping the Clanrat mass marching forward.

## Weapon Profiles

### Close Combat

- **Hand weapon** *(default, 1H — pairs with shield if taken)* — 1" reach | **A 1** | S 3 | AP 0 | D 1 — rusted scimitar, hatchet, or dagger; the lowest-tier mass-issued Skaven blade. `[1H Blade]`
- **Spear** *(option, 1H — replaces Hand weapon, may pair with shield)* — 2" reach | **A 1** | S 3 | AP 0 | D 1 — rusted polearm; lets the second rank strike alongside the front rank in a deep formation. `[1H Reach]`
