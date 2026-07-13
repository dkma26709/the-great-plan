# Flamespyre Phoenix

> Sacred firebird of Asuryan, native to the Flamespyres of Caledor — the volcanic peaks where the Asur god of flame is most directly present. Where Dragons are *pure biology* — ancient apex predators with no inherent magic — the Phoenix is the opposite: a *magical creature* whose every feather burns with the fire of Asuryan, whose every wingbeat trails sacred flame. The Flamespyre Phoenix is the *young* form: hot-blooded, fierce, the plumage blazing red-gold with active fire. "Over generations, the Phoenixes of the Flamespyres have become attuned to fire magic" — they live their early centuries as Flamespyres, then, as they age, their fire cools and they transform into Frostheart Phoenixes. The lore signature is twofold: **Wildfire** *(an AoE damage aura — enemies in base contact with the Phoenix take D3 Flaming hits at start of each Combat phase, modelling the burning plumage)* and **Fiery Rebirth** *(when slain, the Phoenix may rise again from its own ashes — roll D6, on 4+ the Phoenix returns at half W, the iconic resurrection mechanic)*. Drafted here as the **Hero-tier Monster Mount profile** for High Elf Anointed of Asuryan characters (canon Phoenix rider; deferred to future character draft). Sister-piece: Frostheart Phoenix — same biology, aged form with Cold Aura debuff instead of Wildfire damage AoE. The High Elf battlefield read: the Phoenix isn't a melee duellist; its value lies in *area damage* (Wildfire) + *Hero-mount Fly mobility* + *Rebirth swing* — the opposing player has to commit to fully killing it, then succeed on a 4+ rebirth roll, then kill it again.

## Profile

**Flamespyre Phoenix (Mount profile):**
| M | MA | MD | BS | S | T | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|----|-----|----|
| 1 | 5 | 5 | 0 | 4 | 5 | 7 | 6 | 8 | 4 | =W |

**Points:** +131 added to the rider's base cost (Flamespyre Phoenix + Rider combined per Rider and Mount Profiles §1). *(Framework derivation under §13: stat-baseline 16.0 + rules 16.5 + equipment 5.0 = 37.5 raw × wound factor 4.36 (W 7) × 0.8 scaling = 130.8 → +131. **Pass 2 (2026-05-18):** NA removed (Flamespyre's young plumage burns rather than armours — fire-aspect = no protective scaling); Wildfire upgraded to 6" range with 1 hit per enemy model in range (much stronger AoE); Attuned to the Winds variable Ward added. Pass 1 reported +103 due to an arithmetic error in stat subtotal — corrected to +120 in Pass 2 (with no NA: +131). Mid-Monster Hero-mount tier. See `design.md` for full working)*

**Unit size:** 1 (combined model — Anointed of Asuryan Hero rider + Flamespyre Phoenix mount)

**Unit type:** Monster Mount (single model combining Flamespyre Phoenix + Rider — see §1 Rider and Mount Profiles)

**Natural Armour:** — *(Flamespyre's young plumage burns rather than armours — the fire-aspect biology is offensive, not defensive. Survival comes from Wildfire's deterrent aura, Fiery Rebirth's resurrection swing, and the Attuned to the Winds variable Ward — not from passive scales. Contrast: Frostheart's aged plumage cools into harder frost-rimed scales at NA 5+; Arcane's blazing magical feathers turn arrows at NA 4+)*

**Fly:** 8" (per §8 — Phoenix is a flier first and foremost; ground M 1 is essentially flavour, the Phoenix doesn't really walk)

**Base Size:** 50mm × 100mm (medium flyer footprint)

**Keywords:** High Elves, Asur, Phoenix, Flamespyre, Monster, Character Mount, Magical Creature

## Equipment

- **Equipment:** Talons-and-Beak (natural — apex Phoenix talons + flame-touched beak) + Wildfire (passive aura — see Special Rules). No worn armour, no shield, no rider weapons.

## Special Rules

- **Terror** *(Psychology — per §8)* — at LiS 4, the Terror aura projects to **(6 + 4)" = 10"**. A flaming sacred firebird of Asuryan registers as terror on any battlefield — most enemy soldiers have never seen a Phoenix and will not stand against it.
- **Fly (8")** *(per §8)* — Phoenix wings of fire carry the model over terrain and intervening models.
- **Magical Attacks** *(per §8 — Phoenix biology intrinsic)* — all of the Phoenix's attacks (Talons-and-Beak + Wildfire) count as Magical Attacks. **Unlike Dragons** *(which our codebase treats as pure-biology, non-magical)*, **Phoenix is genuinely magical** — sacred to Asuryan, biologically infused with the firmament's fire. The Magical Attacks rule lets Phoenix attacks bypass Ethereal immunity and certain spell-deflection rules.
- **Wildfire** *(Flamespyre Phoenix unit identity rule — Pass 2: range-based AoE damage aura)* — At the start of each **Combat phase**, **every enemy model within 6"** of the Flamespyre Phoenix takes **1 hit at S 4 / AP 0 / D 1 / Flaming / Magical Attacks**. Hits are automatic (no to-Hit roll); allocated per-model (the rule targets each model individually, not per-unit); standard wound allocation applies; armour saves and Ward saves apply per standard. The hits resolve **before any model's melee attacks** in the Combat phase — the Phoenix's plumage burns the entire battlefield-radius before strikes land.

  **Lore-direct:** The Phoenix's body is a continuous *radiating* burn — any creature within 6" feels the heat. **Mean expected damage per Combat phase scales with the number of enemy models in range:** vs a tightly-packed 5-wide × 4-deep State Troops formation (20 models, ~12 within 6"), the Wildfire deals ~12 hits × 0.67 wound × 0.67 unsaved × 1 = **~5 dead per Combat phase**. Vs an apex single-model Monster within 6": 1 hit × 0.67 wound × low save = ~0.3 dmg per Combat phase. The rule's value scales with enemy density — *anti-horde* by design.

  **Flaming triggers** the standard interactions per §8: negates Regeneration on the target, Flame-panic on US 2+ beast units (the Phoenix is itself US 7, immune to its own Flame-panic by the "any Flaming weapon in profile" exception). Magical Attacks lets the aura damage Ethereal targets.

- **Attuned to the Winds** *(Phoenix-shared identity rule — variable Ward save scaling with the Magic phase)* — At the start of each **Magic phase**, after both Power and Dispel pools are determined, roll a **D6**. The result determines the Flamespyre Phoenix's Ward Save for the rest of this turn:

  | D6 | Ward this turn |
  |---|---|
  | **1-2** | None (the winds are still — the Phoenix's fire is dim) |
  | **3-4** | **Ward 6+** |
  | **5** | **Ward 5+** |
  | **6** | **Ward 4+** |

  The Ward applies to all incoming wounds (melee, ranged, magic, template). **Lore-direct:** "The Phoenix is attuned to the flow of magic — its protective fire waxes and wanes with the Winds of Magic." All three Phoenix variants (Flamespyre, Frostheart, Arcane) share this rule; the Arcane Phoenix's Magic-attunement is most pronounced via its Emberstorm interaction, but the variable Ward is biology-wide.

- **Fiery Rebirth** *(Flamespyre Phoenix unit identity rule — once-per-battle resurrection)* — When this model is reduced to 0 W (i.e., would be removed as a casualty), **immediately roll a D6 before the model is removed**. On a **4+**, the Phoenix is *not* removed — instead:

  1. The Phoenix is restored to **half its starting Wounds, rounded up** (W 7 → 4 W remaining).
  2. The model stays at its current position (in melee if it was in melee; out of melee if it was killed by shooting / magic).
  3. **If the rider was attached**, the rider is removed from play permanently (the rebirth burns the Anointed of Asuryan in the resurrection-flames — *only the Phoenix returns*, not the rider). The mount-profile continues without a rider for the rest of the battle.
  4. **Fiery Rebirth may trigger only ONCE per battle**, regardless of how many times the Phoenix is killed.

  On a **1-3**, the Phoenix is removed normally as a casualty (no rebirth; the sacred fire failed to reignite).

  **Lore-direct:** "The Phoenix may, if slain, return to life in a blazing fire." The chick-form Phoenix continues fighting at reduced W but with full stats — the resurrection isn't an apex revival, it's a partial recovery. The rider-loss reflects the lore that the resurrection-flame consumes everything except the Phoenix's own immortal essence.

## Weapon Profiles

### Close Combat

- **Talons-and-Beak** *(natural — apex Phoenix talons + flame-touched beak)* — **1" reach** | **A 3** | **S 4** | **AP -1** | **D 1** | **Magical Attacks** — three flame-touched strikes per Combat round. **S 4** wounds T 3 on 3+, T 4 on 4+, T 5 on 5+; **AP -1** strips light armour. **D 1** baseline. The Phoenix's direct melee output is *modest* — its real damage comes from the Wildfire aura and from the rider's attacks. The Phoenix isn't a duellist; it's an aura-platform and Hero-mount delivery vehicle. `[Natural, Magical]`
