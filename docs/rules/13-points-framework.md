# §13 Points Framework


Unit costs are derived from a two-stage formula: a base **stat contribution** representing the unit's combat and rule value at W1-equivalent, multiplied by a **wound factor** that scales durability non-linearly with wound count.

```
cost = round(statContribution × woundFactor)
```

A linear cost-per-wound systematically undervalues high-W units — every additional wound buys both an extra survival interaction *and* an extra turn of offensive output. The quadratic wound factor captures this compounding.

### 13.1 Wound Factor

```
woundFactor = 1 + 0.08 × (W - 1) × W
            = 0.08W² - 0.08W + 1
```

Lookup table:

| W | Factor |
|---|--------|
| 1 | 1.00 |
| 2 | 1.16 |
| 3 | 1.48 |
| 4 | 1.96 |
| 5 | 2.60 |
| 6 | 3.40 |
| 7 | 4.36 |
| 8 | 5.48 |

For **mounted units** (Rider and Mount Profiles, per §1), use the **combined W computed under §1 *Combined Wounds*** — higher of rider/mount as base + the other contributing via 2:1 conversion. For units with **A=W / US=W dynamic stats** (Jungle Swarms and similar), use the starting (maximum) W value.

### 13.2 Stat Contribution

Start from a **baseline of 5**, representing a standard grunt — WS3 S3 T3 W1 I3 A1 Res7 M4, 6+ save. Adjust per the tables below.

**Per-stat modifiers** *(refined 2026-05-02 — Pass 6 framework update)*:

| Stat | Modifier per point from baseline |
|------|----------------------------------|
| WS-A / WS-D | ±0.5 each |
| S | ±1.0 |
| T | ±1.5 |
| I | ±0.75 *(refined — was ±0.5; bumped to reflect strike-order value at high tiers)* |
| A | ±1.5 per attack (lives on weapon profiles, per A-on-weapons convention) |
| Res | ±0.5 |
| M | ±0.5 in M4–M8 range; ±0.75 per step at M9+ *(refined — was ±0.25; bumped to reflect mobility value)* |
| Save | Cumulative — see schedule below |

**Save schedule (cumulative)** *(refined 2026-05-02 — was linear +1/step)*:

| Save | Cumulative cost from no-save | Marginal step cost |
|------|------------------------------|---------------------|
| no save | 0 | — |
| 6+ | +1 | +1 |
| 5+ | +2 | +1 |
| 4+ | +4 | +2 |
| 3+ | +6 | +2 |
| 2+ | +9 | +3 |

The non-linear schedule captures that each save step reduces incoming damage by a *larger* proportion at the high tiers — 3+ → 2+ halves remaining damage; 6+ → 5+ removes only 17%. Linear pricing under-priced 2+ and 3+ saves; the cumulative schedule honours the effective-durability gain.

**Unit-type keyword premiums:**

| Type | Premium |
|------|---------|
| Infantry | 0 (baseline) |
| Cavalry | +1 |
| Monstrous Infantry | +2 |
| Monstrous Cavalry | +3 |
| Warbeast | 0 to +1 |
| Chariot | +2 |
| Monster | +3 to +5 |
| Swarm | 0 to +1 |

**LiS/US modifiers:**

- LiS above typical for type: +0.5 per step
- LiS below typical: -0.5 per step
- US above type default: +0.5 per point
- Dynamic US (Swarm with US=W): +0.5 fixed

### 13.3 Rule Contribution Table

Representative values — playtest-adjustable.

**Flat-cost rules** (situational / formation / morale-binary; cost doesn't scale with model stats):

| Rule | Contribution |
|------|--------------|
| Fast Cavalry | +2 |
| Aquatic | +0.5 |
| Skittish | -0.5 |
| Skirmishers | +1.5 (includes +1 M, Cannot Form, Free pivots, Fire on the move, Coherency 2") |
| Elusive | +1.5 |
| Fly (10) | +3 |
| Fly (12) | +4 |
| Fly (14+) | +5 |
| Strider (X) | +0.5 |
| Chameleon | +2 |
| Mixed Unit | +0.5 |
| Unbreakable | +3 |
| Stupidity | -2.5 |
| Expendable | 0 |
| Dispersed Mass | +2 |
| Smothering Mass | +3 |
| Cold-Blooded | +1 |
| Disciplined | +1 |
| Undisciplined | -0.5 |
| Fear | +1.5 |
| Terror | +2.5 |
| Immune to Psychology | +1 |
| Will of Chaos (Imm Psych + reroll Recovery) | +3 |
| Random Attacks | 0 |
| Random Movement | -1 |
| Swarm dynamic stats (A=W) | +2 |
| Ward Piercing (X) | +X |

**Stat-dependent rules** *(refined 2026-05-02 — Pass 6)* — cost scales with the stat the rule synergises with. Formula form, then sample values:

| Rule | Formula | Sample values |
|------|---------|----------------|
| **Predatory Fighter** | +1 × A_primary | A 1: +1; A 2: +2; A 3: +3 |
| **Frenzy / F4** | +2 + 0.5 × (S − 3) | S 3: +2; S 4: +2.5; S 5: +3 |
| **Stubborn** | +1 + 0.3 × (Res − 7), floor +1 | Res 7: +1; Res 9: +1.6; Res 10: +1.9 |
| **Unstable** | −2 − 0.3 × (7 − Res), floor −3 | Res 7: −2; Res 5: −2.6; Res 4: −3 |
| **Hatred** | +0.5 × A_primary | A 1: +0.5; A 2: +1; A 3: +1.5 |
| **Killing Blow (Target, X)** | +0.3 × A × X × narrowness factor (~0.3 narrow keyword to 1.0 broad / Any) | KB(Cav, 2) on A 1: +0.6 × narrow; KB(Any, 2) on A 1: +0.6 |
| **Poisoned Attacks** | +0.5 × A_primary | A 1: +0.5; A 2: +1 |
| **Magical Attacks** | +0.5 × A_primary | A 1: +0.5; A 2: +1 |
| **Lightning Attacks** (ignore armour) | +0.5 × A_primary | A 1: +0.5; A 2: +1 |
| **Multiple Shots (X)** | +0.5 × (X − 1) × (BS / 4) | BS 3 / Mult 2: +0.4; BS 4 / Mult 2: +0.5; BS 5 / Mult 3: +1.25 |
| **Quick to Fire** *(inverse — low-BS shooters benefit more)* | +0.5 × (5 − BS) × 0.5, floor +0.3 | BS 2: +0.75; BS 3: +0.5; BS 4: +0.3; BS 5: +0.3 |

**Why stat-dependent.** Many rules synergise with a specific stat — Stubborn is more valuable on a high-Res unit (more morale range to exploit), Predatory Fighter scales linearly with attack count (each base attack triggers PF independently), Multiple Shots benefits high-BS shooters more (the to-hit penalty hurts less in proportional terms), Quick to Fire is the inverse (low-BS shooters gain more from +1 to-hit accessibility). Flat values mis-priced at the extremes; formula values track the synergy.

**Caveat.** Per §13.6, the formula is a calibration anchor, not a strict equation. Stat-dependent values get the prediction closer; final pricing still requires designer sanity-check against comparable units.

**Unit-specific identity rules** (costed case-by-case, typical band +1 to +7):

| Rule | Contribution |
|------|--------------|
| Pack Cohesion (Saurus Warriors) | +1 |
| Sworn Protectors (Temple Guard) | +7 |
| Emboldened Handlers (Kroxigor) | +1.5 |
| Predator's Scent (Raptadon Hunters) | +1 |
| Flock Disruption (Terrawings) | +2.5 |
| Blood Frenzy (Aggradon Lancers) | +4 |
| Perfect Stillness (Chameleon Skinks) | +2 |
| Unleashed Flame (Salamanders) | +2 |
| Instinctive Defence (Razordons) | +2.5 |
| Aimless (Razordons) | -2 |
| Impaling Charge (Horned One Riders) | +1.5 |
| Drop Rocks (Terradon Riders) | +1.5 |
| Predatory Instinct (Ripperdactyl Riders) | -1 |
| Toad Rage (Ripperdactyl Riders) | +2 |
| Unstoppable Momentum (Stegadon) | +4 |
| Impervious Defence (Bastiladon) | +2 |
| ~~Thunderous Bludgeon (Bastiladon)~~ | *dropped — replaced by Crushing Tail dedicated rear-arc weapon* |
| ~~Primeval Roar (Troglodon)~~ | *dropped — thematically inappropriate for a blind cave ambusher* |
| Sightless Hunter (Troglodon) | +2.5 |

### 13.4 Equipment Contribution *(expanded 2026-05-02 — Pass 6)*

Weapons contribute to a unit's price via per-component costs. Sum the components on each weapon profile to get its equipment contribution; the sum of all profile contributions is the unit's equipment cost (after the wound factor multiplier on stats and rules).

#### Melee weapon components

| Component | Contribution |
|-----------|--------------|
| 1" reach (baseline hand weapon) | 0 |
| 0.5" reach (front-rank-only natural attack — e.g., Saurus Jaws) | -0.3 |
| **2" reach — Infantry** *(frontage-doubler in deep blocks)* | **+1** |
| 2" reach — Cavalry / MonstInf / Mixed Unit | +0.5 |
| 2" reach — single-model Character / Monster | +0.3 |
| 3"+ reach — Infantry | +1.5 |
| 3"+ reach — other unit classes | +1 |
| Per extra Attack on weapon (above A 1 baseline) | +1.5 |
| AP -1 (per step from AP 0) | +0.5 |
| Damage 2 melee | +1 |
| Damage 3 melee | +2 |
| Wielder S+1 (always-on, baked into weapon) | +0.5 |
| Wielder S+2 (always-on — Great Weapon class) | +1.5 |
| Charge-only bonuses (e.g., +1 S on charge, AP -1 anti-charge, D 2 anti-Cav) | +1 to +1.5 (per conditional) |
| Two-handed | 0 (trade-off — quantified via the lost shield save step elsewhere in the unit's loadout) |
| Always Strikes Last | -1 to -1.5 |
| Always Strikes First (per attack) | +1 |
| -1 Initiative wielder penalty (e.g., Orc Great Choppa) | -0.5 |
| Killing Blow (Target, X) | per stat-dependent formula in §13.3 |

**Reach value scales with unit class** because the second-rank-attack benefit only applies when there *is* a second rank. A 2" polearm in a 5-wide × 4-deep Infantry block effectively doubles attacking frontage; the same reach on a Carnosaur is irrelevant.

#### Ranged weapon components

| Component | Contribution |
|-----------|--------------|
| Range 6" (very short — pistol, breath-close) | -0.5 |
| Range 8" (short skirmish — javelin throw) | -0.25 |
| **Range 12" (baseline — blowpipe, sling, shortbow)** | **0** |
| Range 18" | +0.5 |
| Range 24" | +1 |
| Range 30" | +1.5 |
| Range 36" | +2 |
| Range 48" | +3 |
| Range 60"+ (cannon, war machine) | +4 |
| AP -1 (per step from AP 0) | +0.5 |
| Inherent S (when weapon-specified, e.g., Handgun S 4, Cannon S 10) | +1 per S point above wielder's typical S |
| Damage 2 | +1 |
| Damage D3 | +2 |
| Damage D6 / multi-D (artillery / cannon scaling) | +3 to +4 |
| Multiple Shots (X) | per stat-dependent formula in §13.3 |
| Quick to Fire | per stat-dependent formula in §13.3 |
| Rapid Fire (negates Multiple Shots penalty) | +0.5 × (X-1) |
| 360° arc | +0.5 |
| Slow to Fire | -0.5 |
| Flaming | +0.5 (negates Regeneration; flame-panic vs LiS 2+ beast units) |

**Increment for range:** +0.5 per 6" of range above 12" baseline. Tactical reach (range + movement) is the practical threat zone; longer-range weapons threaten more board with the same model.

#### Aggregate weapon archetypes (cross-check baselines)

| Archetype | Components | Total |
|-----------|------------|-------|
| Hand weapon (1" baseline) | reach 0 + A 1 baseline | **0** |
| Spear + shield (1H, 2" reach Infantry) | +1 reach | **+1** |
| Halberd-class (1H, 2" reach, AP -1, KB(Cav,2)) | +1 reach + 0.5 AP + ~0.4 KB | **+1.9** |
| Great weapon (2H, S+2, AP -2) | +1.5 S + 1 AP + 0 Two-Handed | **+2.5** *(plus the unit pays for the lost shield via save schedule)* |
| Heavy Lance (1H, 2" reach, charge S+2 AP-2 D2) | +0.5 reach (Cavalry) + +1 to +1.5 charge bonus | **+2 to +2.5** |
| Skink Blowpipe (12" Mult 2 Quick Poisoned 360°) | range 0 + Mult ~0.4 + QtF ~0.5 + Poisoned 0.5 + 360° 0.5 | **+1.9** |
| Empire Handgun (24" S 4 AP -1) | range +1 + AP +0.5 + inherent S +1 | **+2.5** |
| Empire Crossbow (30" S 4, Slow to Fire) | range +1.5 + inherent S +1 + Slow -0.5 | **+2** |
| Glade Bow (Wood Elf, 30") | range +1.5 | **+1.5** |
| Skeleton Bow (18") | range +0.5 | **+0.5** |
| Flame Template (basic, S 4 Flaming Slow Artillery) | range -0.5 (close) + S +1 + Flaming +0.5 + Slow -0.5 + template-class +3 | **+3.5 to +4.5** |
| Bolt Thrower (48" S 6 AP -3 D D3) | range +3 + S +3 + AP +1.5 + D D3 +2 | **+9.5** |
| Cannon (60"+ S 10 AP -3 D D6) | range +4 + S +7 + AP +1.5 + D D6 +3.5 | **+16** *(per profile; multiplied to crew/platform per War Machine convention)* |

### 13.5 Calibration

> **Note (2026-05-02 — Pass 6).** The calibration table below reflects pricing computed under the **pre-refinement framework** (linear save schedule, flat rule values, ±0.25 M, ±0.5 I). Existing roster prices held; new drafts use the refined framework per §13.2/§13.3/§13.4 above. Re-pricing of existing units under the refined framework deferred until playtest signals systematic miscalibration. Sample audit (Halberdier / Saurus / Chaos Warrior / KotR / Aggradon Lancers) shows refined-framework prices typically run +10-20% above current calibration, with cheaper units (Halberdier) showing the largest proportional jumps.

The framework has been fit against the current roster of priced units:

| Unit | Stat Sum | W | Factor | Computed | Draft | Δ |
|------|----------|---|--------|----------|-------|---|
| Skink Cohort | 5.5 | 1 | 1.00 | 6 | 5 | -1 |
| Skink Skirmishers | 9.0 | 1 | 1.00 | 9 | 8 | -1 |
| Terrawings | 7.0 | 1 | 1.00 | 7 | 7 | 0 |
| Raptadon Hunters *(Pass 3 — W2 pool → W1 highest+conv)* | 14.5 | 1 | 1.00 | 15 | **15** | 0 |
| Raptadon Chargers *(Pass 3 — W2 pool → W1 highest+conv)* | ~28 | 1 | 1.00 | 28 | **28** | 0 |
| Saurus Warriors | 19.0 | 2 | 1.16 | 22 | 22 | 0 |
| Temple Guard | 27.5 | 2 | 1.16 | 32 | 35 | +3 |
| Kroxigor | 22.25 | 6 | 3.40 | 76 | 75 | -1 |
| Jungle Swarms | 7.25 | 7 | 4.36 | 32 | 32 | 0 |
| Aggradon Lancers *(Pass 3 — W6 pool → W5 highest+conv)* | 35.75 | 5 | 2.60 | 93 | **95** | +2 |
| Chameleon Skinks | 13.5 | 1 | 1.00 | 14 | 14 | 0 |
| Salamanders (beast only — M6 A3, NA 6+) | 19.5 | 5 | 2.60 | 51 | 65 | +14 |
| Salamanders (beast + 3 handlers bundle) | — | — | — | 66 (formula) | **80** (priced) | +14 |
| Razordons (beast only — M6 A3, NA 5+, Rapid Fire) | 21 | 5 | 2.60 | 55 | 65 | +10 |
| Razordons (beast + 3 handlers bundle) | — | — | — | 70 (formula) | **80** (priced) | +10 |
| Horned One Riders *(Pass 3 — W2 pool → W1 highest+conv)* | 18.5 | 1 | 1.00 | 19 | **26** | +7 |
| Terradon Riders *(Pass 3 — W4 pool → W3 highest+conv)* | 22 | 3 | 1.48 | 33 | **34** | +1 |
| Ripperdactyl Riders *(Pass 3 — W4 pool → W3 highest+conv)* | 23.5 | 3 | 1.48 | 35 | **36** | +1 |
| Stegadon (beast only — T6, W12 extended factor 7.48) | 33 | 12 | 7.48 | 247 | 250 | +3 |
| Stegadon (beast + 5 Skink Crew bundle) | — | — | — | 272 | **275** | +3 |
| Bastiladon (beast only — W10, T7, S5, 3-weapon profile, NA 2+) | 38.5 | 10 | 6.48 | 250 | 250 | 0 |
| Bastiladon (beast + 4 Crew + Ark of Sotek default) | — | — | — | 270 | 270 | 0 |
| Bastiladon (beast + 3 Crew + Revivification Crystal) | — | — | — | 275 | 275 | 0 |
| Bastiladon (beast + 3 Crew + Solar Engine) | — | — | — | 305 | 305 | 0 |
| Troglodon (beast only — W10, Ambushers, Sightless Hunter, three-weapon split) | 33 | 10 | 6.48 | 214 | 215 | +1 |
| Troglodon (beast + Oracle bundle) | — | — | — | 219 | **220** | +1 |
| Ancient Salamander (beast only — W7, S5, T4, NA 5+, Searing Stream S5 AP-2) | 17 | 7 | 4.36 | 74 | 100 | +26 |
| Ancient Salamander (beast + 3 Handlers bundle) | — | — | — | 115 (formula+weapon premium) | **140** (priced) | +25 |
| Arcanadon (beast only — W14, sauropod, Stubborn, Aura of the Old Ones, PoA cannon) | 42 | 14 | 8.48 | 356 | 360 | +4 |
| Arcanadon (beast + 3 Crew bundle with Power of the Ancients) | — | — | — | ~380 | **400** | +20 |
| Coatl (W8 — Fly 8, MR3, Terror, Magical Storm, Guardian; Wizard flat pkg +50 for Lore Access 3 / Cast Base 2 / Dispel Base 2 / Channelling 2 / Cast Bonus +1 / Dispel Range 18") | 30 | 8 | 5.48 | 214 (164 base + 50 flat wizard) | **225** | +11 |
| Dread Saurian (beast only — W25 apex, Earth-Shaking Roar, 4-weapon profile, NA 3+, LiS 6) | 40 | 25 | 13.98 | 559 | **550** | -9 |

**Drift policy:**
- Units within ±1 pt of the formula are considered formula-accurate. No action needed.
- Divergences ≥ 2 pts trigger investigation. Either the formula is missing a rule cost, or the draft price is wrong.
- Temple Guard was investigated — Sworn Protectors was initially valued at +5; re-costed to +7 in this framework to reflect the combined Bodyguard + Slann's Resolve package. With that update, the formula produces 35, matching the draft price.
- Jungle Swarms was investigated — formula produces 32; draft price was 30. Updated to 32 per the ≥ 2 pt threshold policy.
- Ancient Salamander Δ +25 — the Searing Stream template weapon (S 5 AP -2) is under-priced in the equipment table (+4 for a basic flame template); playtesting will decide whether to bump template weapon baseline or keep the bundle premium.
- Arcanadon bundle Δ +20 — the Power of the Ancients (cannon + channel-aura combo) is underweighted in the rule-contribution table. Deferred investigation; value matches Stegadon's price envelope for a comparable apex-utility Monster and reads correct by design intent.
- Coatl Δ +11 — the Wizard package is currently priced **flat** (+50 for Lore Access 3 / Cast Base 2 / Dispel Base 2 / Channelling 2 / Cast Bonus +1 / Dispel Range 18") rather than W-factor-multiplied. Convention pending formal §13 write-up once more wizard profiles (Skink Priest, Slann) are drafted. Multiplying the wizard package by the W factor would over-price magic on durable casters; keeping flat is the current working call.

### 13.6 Caveats and Limitations

- The formula is a **baseline**. Specific unit interactions, army-list synergies, and playtest evidence may shift a final price by ±10%.
- Identity rule values (Sworn Protectors, Predator's Scent, etc.) are designer judgement within the +1 to +7 band, not arithmetic derivations.
- Mounted units (Cavalry / Monstrous Cavalry / Monster-mount) use the **model W computed under §1 *Combined Wounds*** — the higher of rider/mount W as base + the other contributing via 2:1 conversion. The factor curve applies to the resulting model W. Separate-model units with the same total wounds (e.g., two W1 models) are **cheaper per wound** because they split durability rather than pooling it — an Infantry unit of 10 × W1 models is not interchangeable with a Cavalry unit of 5 × W2 models for formula purposes.
- Points are rounded to the nearest whole number. Fractional results below 0.5 round down; 0.5 and above round up.
- The quadratic wound factor is calibrated against the current roster. As new units join (including ones with W8+ or unusual profile shapes), the factor curve may need adjustment at the extremes.
- **Extreme W (W9+) factor extension.** The quadratic factor escalates steeply past W8 (W8 = 5.48, W12 = 11.56 at the raw formula) which in practice over-prices Monster-scale units at the very extreme end. At high wound counts, durability is no longer purely linear with the attacker's difficulty of killing the unit — the enemy concentrates fire on the apex model, key abilities (Sniper, Ward Piercing, high-AP weapons) are brought to bear, and focus-fire becomes easier not harder. For W > 8 the framework applies a **linear extension**: `factor(W) = factor(8) + 0.5 × (W − 8)`. This produces W9 = 5.98, W10 = 6.48, W11 = 6.98, W12 = 7.48 — a scale that still reflects Monster durability premium without the raw quadratic runaway. The 0.5-per-W coefficient was calibrated against the Bastiladon (W10, 2+ save, heavy-relic bundle) and Stegadon (W12) to produce points that match the "Monsters cost real money" design intent. Playtest-tunable.
- **Extreme save values (2+ and lower).** Armour Save contributions scale linearly per §13.2 (+1 per step above 6+), but the *effective* durability gain from a 2+ save is sharply non-linear — a 2+ save against AP 0 weapons passes 83% of rolls vs 50% at 4+, so the effective-wound multiplier is much higher than the linear +4 contribution suggests. Units with a native 2+ save (typically Monsters with biological armour) are under-priced by the formula; adjust upward case-by-case. Bastiladon is priced at 150 vs formula 90 partly for this reason (the other part being the howdah-relic bundle). *(Note: the Pass 6 cumulative save schedule in §13.2 partially addresses this; the +9 cost at 2+ is closer to the effective-durability gain.)*

### 13.7 Deriving Upgrade Costs from the Framework *(added 2026-05-02 — Pass 6)*

The framework is also the canonical tool for pricing **weapon swap upgrades** within a unit's options menu. The methodology:

1. **Compute the base unit price** with the default loadout (default weapon, default armour, default save).
2. **Compute an alternative-loadout price** with the swap (different weapon, different armour, possibly different save tier).
3. **Upgrade cost = (alternative price) − (base price)**.

The §13.4 component values *are* this delta in disguise — "AP -1 per step: +0.5", "2" reach Infantry: +1", "Killing Blow: per formula" are the per-component contributions you sum and difference to get the swap cost.

#### Worked example — Empire Halberdier weapon options

Base unit: Res 9, Disciplined, State Troops, light + shield = 5+ save. Stats + rules subtotal (no weapon): **9.5 pts**.

| Option | Components | Equip Δ | Save Δ | Total |
|--------|------------|---------|---------|-------|
| **Hand weapon (baseline)** | reach 0 + AP 0 + S 0 | 0 | 5+ baseline | 9.5 |
| **Halberd (default)** | 2" reach Infantry +1 + S+1 +0.5 + AP -1 +0.5 + KB(Cav,2) ~0.4 | +2.4 | 5+ | 11.9 |
| **Spear + shield** | 2" reach Infantry +1 | +1 | 5+ | 10.5 |
| **Great Weapon (no shield)** | 1" reach 0 + S+2 +1.5 + AP -2 +1 + Two-Handed 0 | +2.5 | **6+ (light only, no shield)** | (9.5 − save delta from 5+ to 6+ = -1) + 2.5 = 11.0 |

Upgrade prices fall out:
- Halberd over hand weapon baseline: **+2 pts** (matches current default-included Halberd price)
- Spear + shield swap: **+1 pt** (alternative)
- Great Weapon swap: **+1.5 pts** (offensive gain partially offset by save loss)

#### Why this matters

- **Cross-unit consistency.** Halberd-class polearms across factions (Empire Halberd, Chaos Polearm, Skeleton Polearm) get the same base contribution — different identity rules and stats tweak the price, but the polearm-class baseline is shared.
- **Cross-faction calibration.** When new ranged units draft (Wood Elf Glade Bow vs Empire Crossbow vs Dwarf Quarreller's crossbow), the formula produces consistent base equipment costs. Differentiation lives in S/AP/D/special rules, not designer drift.
- **Audit trail.** When playtest reveals an upgrade is mispriced, the formula tells you which component is off — saving the tedious "is it the AP or the reach?" debate.

#### Limits of formula-derived upgrades

- **Conditional weapon traits** (charge-only bonuses, anti-keyword bonuses, KB) need a *narrowness factor* — how often does the bonus actually fire in typical play? Estimate 0.3 (very narrow keyword) to 0.7 (broad / often-engaged) and scale.
- **Multi-weapon stacking** (a model with hand weapon + natural attack + tail sweep) sums per-weapon costs but **partially-overlapping attacks should discount** — each attack profile that fires from the same engagement counts at full value, but profiles that only fire in specific arcs (rear-arc Tail Sweep) count at ~0.4-0.5×.
- **Equipment trade-offs** (Great Weapon = lose shield) need to be calculated as *net swap* — the offensive gain minus the defensive loss. The formula handles this naturally because save tier appears in §13.2 stats; the swap just changes both equipment line and save line.
- **Equipment that grants new identity rules** (e.g., Magic Standards) needs the rule cost added separately; the equipment is the *carrier* of the rule, not the rule itself.

When formula and judgement disagree by more than ~15%, prefer judgement and document the divergence in the unit's design diary — the formula then learns from the case rather than dictating it.

---
