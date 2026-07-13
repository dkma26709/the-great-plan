# §13 Points Framework


Unit costs are derived from a two-stage formula: a base **stat contribution** representing the unit's combat and rule value at W1-equivalent, multiplied by a **wound factor** that scales durability non-linearly with wound count, and finally scaled by a **global scaling factor** that tunes overall model count per points-budget.

```
cost = round(scalingFactor × statContribution × woundFactor)
```

A linear cost-per-wound systematically undervalues high-W units — every additional wound buys both an extra survival interaction *and* an extra turn of offensive output. The quadratic wound factor captures this compounding. The scaling factor is the global lever for army density: a lower factor makes units cheaper without altering relative power between units, allowing larger armies in the same points budget.

### 13.0 Global Scaling Factor *(added 2026-05-03 — Pass 8)*

```
scalingFactor = 0.8   (current)
```

The global scaling factor is a single tunable knob that scales every unit, character, equipment, and spawning price uniformly. **Relative power between units is unchanged**; only the points-budget ratio shifts.

**Why 0.8?** Pre-scaling prices made rank-and-file blocks feel expensive — a 20-Saurus regiment at 22 pts/model consumed 22% of a 2000-pt budget. The 0.8 scaling drops that to ~18% (Saurus 18 pts/model × 20 = 360 pts), enabling the "big block of infantry plus support" feel that the WAP / Old World tradition relies on. Values were chosen for clean rounding on the most common unit costs.

**How to apply at draft time.** Compute `statContribution × woundFactor` per the framework below to get the *raw* cost. Multiply by `scalingFactor` (currently 0.8). Then round per the **rounding policy** below.

**Rounding policy** *(refined 2026-05-07 — Pass 9)*:

| Cost type | Rounding |
|---|---|
| Equipment / weapon upgrades / character upgrades **< 50 pts** | Nearest **0.5 pt** (e.g., 1.45 → 1.5; 1.7 → 1.5; 1.8 → 2.0) |
| Unit base costs / character base costs **< 50 pts** | Nearest **whole pt** |
| Anything **≥ 50 pts** (units, characters, big mounts, etc.) | Nearest **5 pt** |
| Magic items (any cost) | Nearest **5 pt** *(overrides the 0.5/whole rules — items are an unscaled pool, WAP-tradition pricing in 5-pt increments)* |

The tiered policy avoids the "0.4 raw rounds to 0 pt" precision-loss problem that flat whole-pt rounding caused on cheap upgrades (Spear options, small weapon swaps), while keeping unit and character-base prices clean integers and large-cost items at 5-pt granularity for roster-math readability.

**Existing prices retained.** Prices priced under the previous rounding rule (whole pts only) are kept as-is; re-rounding under the new policy happens organically as units / equipment options are touched in normal design passes. No bulk re-pricing operation is scheduled.

**For "is it equipment or unit-tier?"** — under 50 pts, the line is "is this an additive upgrade to something that already exists" (equipment / character options → 0.5-pt rounding) or "is this a base cost that exists on its own" (unit / character base → whole-pt rounding). For mounts: small mounts that read as character-options (Warhorse +14, Pegasus +24) round per the equipment rule (0.5); big mounts that read as their own statline (Royal Hippogryph 100+ pts, Carnosaur 280+) round per the 5-pt rule.

**Exempt from the scaling factor:**
- **Character magic-item allowances** — Lord-tier 100 pts, Sub-Lord 75 pts, Hero-tier 50 pts. These are armoury-budget caps the player spends *into* the game's separate magic items pool, not points the unit pays for stats and rules. The cap stays anchored to the magic items list (which is itself unscaled) so list-builders see consistent numbers regardless of the global density knob.
- **Battle Standard upgrade cost** — flat **+25 pts** for any character carrying the Army Battle Standard. Conventional cross-faction value; not driven by the §13 stat formula.

These two exemptions are the only ones; everything else (unit base costs, equipment swaps, character base costs, mount upgrades, vow upgrades, Blessed Spawning costs, command upgrades, magic-banner caps on unit standards) flows through the scaling factor.

**Tuning the factor.** If playtest shows armies are too dense (board congestion, slow play) raise toward 0.9 or 1.0; if too sparse (handful of elite models per side) lower toward 0.7. Re-tuning is a single-pass operation against the framework — every priced unit re-derives at the new factor in one bulk update.

**Currently scaled rosters (Pass 8 / Pass 9 / Pass 10):** **§10 Lizardmen, §14 Empire, §15 Ogre Kingdoms, §16 Vampire Counts, §17 Bretonnia, §18 Cross-Faction Reference Units** *(all at 0.8× scaling — full bulk re-scale completed 2026-05-07; Wizard pricing formalised 2026-05-08 in §13.8 (Pass 10), all caster characters re-derived under the framework).*

**No pending re-scales.** All rosters are now consistently scaled at 0.8× and all framework gaps have been closed.

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
| MA / MD | ±0.5 each |
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
| Per extra Attack on weapon (above A 1 baseline) | **+1.5 × (1 + 0.5 × \|AP step (always-on)\| + 0.5 × S_bonus_step (always-on))** *(refined 2026-05-07 — Pass 9; multiplier scales with weapon's offensive amplifier stack)* |
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

**Per-extra-A multiplier scales with the weapon's offensive amplifiers** *(refined Pass 9, 2026-05-07)*. Each additional attack on a weapon profile inherits the weapon's always-on AP and S bonuses — and the value of those amplifiers compounds with attack count. An extra attack on an AP -2 / S+2 great-weapon profile delivers ~2× the unsaved wounds of an extra attack on a plain hand weapon, but the old flat +1.5 priced both the same. The multiplier `1 + 0.5 × |AP step| + 0.5 × S_bonus_step` corrects this — a plain hand weapon (AP 0, no S bonus) keeps the +1.5 base unchanged, but multi-attack weapons with AP / S amplifiers pay proportionally more per extra attack.

**Lookup table for per-extra-A cost** (raw, before scaling):

| Weapon profile | Multiplier | per_extra_A raw |
|---|---|---|
| Plain hand weapon (AP 0, no S) | 1.0 | 1.5 |
| AP -1 weapon | 1.5 | 2.25 |
| AP -2 weapon | 2.0 | 3.0 |
| AP -3 weapon | 2.5 | 3.75 |
| S+1 weapon | 1.5 | 2.25 |
| Great Weapon class (S+2 AP -2) | 3.0 | 4.5 |

**Conditional bonuses don't compound.** Charge-only AP / S (Heavy Lance, Tepok Lance, etc.) and target-conditional bonuses (anti-Cavalry damage, anti-Charge AP, etc.) are NOT included in the multiplier — they keep the existing flat +1 to +1.5 per conditional from the table above. Conditional bonuses fire only once per battle (the charge round, the matchup turn) and don't scale per-attack value the way always-on amplifiers do.

**Per-attack rules already scale with A.** Hatred, Predatory Fighter, Killing Blow, Magical Attacks, Poisoned Attacks, etc. have per-A formulas in §13.3 (e.g., "Predatory Fighter: +1 × A_primary"). They auto-scale when extra attacks are added — no double-counting needed in the per-extra-A multiplier.

**Known gap — MA coupling.** The user's diagnostic also identified MA as a per-attack value driver (more skill = more hits land). MA is on the unit profile, not the weapon, so coupling per-extra-A to wielder MA would require a framework architectural change. Flagged as a follow-up task; current refinement covers AP and S bonuses only.

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
| Coatl (W8 — Fly 8, MR3, Terror, Magical Storm, Guardian; Wizard flat pkg +50 for LA 3 / CaB 2 / DiB 2 / Ch 2 / CB +1 / DR 18") | 30 | 8 | 5.48 | 214 (164 base + 50 flat wizard) | **225** | +11 *(historical pre-Pass-6 entry; Pass 10 re-derivation under §13.8 lands at 250 priced; see §13.8 worked example)* |
| Dread Saurian (beast only — W25 apex, Earth-Shaking Roar, 4-weapon profile, NA 3+, LiS 6) | 40 | 25 | 13.98 | 559 | **550** | -9 |

**Drift policy:**
- Units within ±1 pt of the formula are considered formula-accurate. No action needed.
- Divergences ≥ 2 pts trigger investigation. Either the formula is missing a rule cost, or the draft price is wrong.
- Temple Guard was investigated — Sworn Protectors was initially valued at +5; re-costed to +7 in this framework to reflect the combined Bodyguard + Slann's Resolve package. With that update, the formula produces 35, matching the draft price.
- Jungle Swarms was investigated — formula produces 32; draft price was 30. Updated to 32 per the ≥ 2 pt threshold policy.
- Ancient Salamander Δ +25 — the Searing Stream template weapon (S 5 AP -2) is under-priced in the equipment table (+4 for a basic flame template); playtesting will decide whether to bump template weapon baseline or keep the bundle premium.
- Arcanadon bundle Δ +20 — the Power of the Ancients (cannon + channel-aura combo) is underweighted in the rule-contribution table. Deferred investigation; value matches Stegadon's price envelope for a comparable apex-utility Monster and reads correct by design intent.
- Coatl Δ +11 — the Wizard package is currently priced **flat** (+50 for LA 3 / CaB 2 / DiB 2 / Ch 2 / CB +1 / DR 18") rather than W-factor-multiplied. Convention pending formal §13 write-up once more wizard profiles (Skink Priest, Slann) are drafted. Multiplying the wizard package by the W factor would over-price magic on durable casters; keeping flat is the current working call.

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

### 13.8 Wizard Pricing *(added 2026-05-08 — Pass 10)*

Characters with the **Wizard** keyword carry a **Magic Profile** in addition to the standard stat line: **LA** (Lore Access tier), **CaB** (personal Cast dice), **DiB** (personal Dispel dice), **Ch** (Channel attempts), **CB** (cast modifier), **DB** (dispel modifier), **DR** (Dispel Range), **SK** (Spells Known). These components define the wizard's contribution to the Magic phase and are priced **flat, outside the wound factor** — added directly to the unit's raw cost before global scaling, not multiplied through `woundFactor`.

```
cost = round(scalingFactor × (statContribution × woundFactor + wizardPackage))
```

The flat-outside-W convention is deliberate. A Slann's per-turn casting throughput does not scale with the eight wounds his palanquin carries — he casts the same number of spells whether at full health or one wound from death. Coupling the wizard package to the wound factor would over-price magic on durable casters (a W8 Slann would pay 5.48× the wizard premium of a W3 Battle Wizard for the same magical capability). Flat addition keeps wizard pricing capability-driven, not durability-driven.

#### Per-component contributions

| Component | Cost (raw) |
|---|---|
| **LA Tier 1** (Sig + Basic spells) | +22 |
| **LA Tier 2** (+ Intermediate) | +30 cumulative *(+8 step)* |
| **LA Tier 3** (+ Advanced) | +40 cumulative *(+10 step)* |
| **LA Tier 4** (+ Master) | +42 cumulative *(+2 step)* |
| **CaB** per personal Cast die | +6 |
| **DiB** per personal Dispel die | +5 |
| **Ch** per Channel attempt | +5 |
| **CB** per +1 cast modifier | +8 |
| **DB** per +1 dispel modifier | +6 |
| **SK** per spell known above 2 baseline | +3 |
| **Multi-lore intrinsic** per additional lore beyond the 1st | +5 |

There is **no flat "Wizard chassis" cost** — every cost line ties to a concrete in-game capability. A model with the Wizard keyword but LA 0 / CaB 0 / DiB 0 (a hypothetical Wizard-keyword carrier with no actual magic) pays nothing for the keyword alone.

**LA tier costs are deliberately modest** — the qualitative jump from Tier 3 to Tier 4 (Master spells) is captured in the **Cast Mastery synergy** below, not in the flat tier cost. A Lvl 4 wizard's value over a Lvl 3 wizard is dominated by the LA-multiplied compounding of his cast bundle, not by a large flat fee for the tier.

**DR is not a flat per-inch cost** — it is folded into the Dispel Mastery synergy below. A wizard's dispel reach has value only in proportion to his other dispel components (a 36" DR with 0 dispel dice and DB +0 is mechanically equivalent to a 12" DR for the same loadout).

#### Cast Mastery synergy

```
Cast Mastery = LA × min(SK, CaB + Ch) × CB × 0.15
```

Cast Mastery captures two compounding effects:

- **LA tier amplifies per-cast value.** A successful cast at LA 4 (Master tier) is qualitatively more decisive than one at LA 1 — Master spells include game-winners (Final Transmutation, Soulfire, Pit of Shades, Purple Sun). The LA factor multiplies the synergy because higher-LA wizards generate more value per cast attempt.
- **CB compounds over multiple casts, capped by dice throughput.** A wizard's dice pool sets the ceiling on casts per turn. A wizard with high CB but few spells still benefits because each smaller cast exercises the modifier; a wizard with many spells but low dice cannot cast them all anyway. The `min(SK, CaB + Ch)` term enforces this — once spell count exceeds the dice ceiling, additional spells become flat *selection cost* (the SK line above), not multiplicative casting effectiveness.

The 0.15 coefficient calibrates the synergy contribution to fit the existing Empire / Bretonnia / Vampire Counts mortal-tier wizard ladder while keeping the synergy modest at low tiers (Battle Wizard L1 with CB 0 generates 0 Cast Mastery; Lvl 4 wizards with CB +3 and 4 dice generate 3.6 raw).

#### Dispel Mastery synergy

```
Dispel Mastery = DiB × (DB + (DR − 12) / 12) × 0.5
```

DiB and DB compound symmetrically to the cast pair, with **DR folded in** as a proportional contribution rather than a separate flat fee. The `(DR − 12) / 12` term makes a 12" DR contribute 0 to the synergy (no dispel reach above the implicit baseline), 18" contributes 0.5, 24" contributes 1.0, 36" contributes 2.0. A wizard's dispel reach then multiplies through his dispel dice — a Slann with DR 36" / DiB 5 / DB +4 produces Dispel Mastery 5 × (4 + 2) × 0.5 = 15 raw, capturing the apex defensive umbrella; a Battle Wizard L1 with DR 18" / DiB 1 / DB 0 produces 1 × 0.5 × 0.5 = 0.25 raw, mostly invisible at low tiers.

LA does not multiply Dispel Mastery — defensive dispelling depth is more uniform across LA tiers than offensive casting, and the symmetrical synergy already grows naturally with the Lord-tier wizard's higher dispel components.

#### Lvl ladder packages (quick reference)

The Empire / Bretonnia / Vampire Counts mortal-tier wizards follow a canonical Lvl 1 → Lvl 4 ladder with these magic profiles:

| Lvl | LA | CaB | DiB | Ch | CB | DB | DR | SK | Wizard package (raw) |
|---|---|---|---|---|---|---|---|---|---|
| **1** | 1 | 2 | 1 | 1 | +0 | +0 | 18" | 2 | **44.25** |
| **2** | 2 | 2 | 1 | 2 | +1 | +0 | 18" | 2 | **65.85** |
| **3** | 3 | 3 | 2 | 3 | +2 | +1 | 24" | 2 | **108.8** |
| **4** | 4 | 4 | 3 | 3 | +3 | +2 | 24" | 2 | **140.1** |

Lvl-to-Lvl upgrade costs (raw) fall out of the ladder: L1→L2 = +21.6, L2→L3 = +43.0, L3→L4 = +31.3. The L2→L3 step is the largest because it spans the Hero-to-Lord magic capability transition (one extra die in each pool, +1 CB, +1 DB, DR extends 18" → 24"); L3→L4 is smaller because the Lord-tier dispel dice and DR are already in place at Lvl 3.

#### Worked example — Empire Wizard Lord at Lvl 4

| Component | Value | Contribution |
|---|---|---|
| LA Tier 4 | 4 | 42 |
| CaB | 4 | 4 × 6 = 24 |
| DiB | 3 | 3 × 5 = 15 |
| Ch | 3 | 3 × 5 = 15 |
| CB | +3 | 3 × 8 = 24 |
| DB | +2 | 2 × 6 = 12 |
| SK above 2 | 0 | 0 |
| Multi-lore | 0 | 0 |
| **Cast Mastery** | 4 × min(2, 7) × 3 × 0.15 | 3.6 |
| **Dispel Mastery** | 3 × (2 + 1) × 0.5 | 4.5 |
| **Wizard package** | | **140.1** |

Wizard Lord stat × wound = 8.0 × 1.96 = 15.68. Total raw = 15.68 + 140.1 = 155.78. Scaled = 0.8 × 155.78 = 124.6. Rounded to nearest 5 = **125 pts**.

#### Off-ladder casters

Casters whose magic profile diverges from the canonical Lvl 1-4 ladder — typically **fixed-LA characters** (Skink Priest LA 2 fixed, Skink High Priest LA 3 fixed, Skink Starseer LA 4 Heavens fixed, Coatl LA 3 Heavens, Slann LA 4 + Mastery of All Winds) — derive their wizard package by summing components per the table above. The Cast Mastery and Dispel Mastery synergies apply normally.

**Slann Mage-Priest** stress-tests the high end (LA 4, CaB 5, DiB 5, Ch 5, CB +4, DB +4, DR 36", SK 6, three intrinsic lores via Mastery of All Winds): Cast Mastery 4 × min(6, 10) × 4 × 0.15 = 14.4; Dispel Mastery 5 × (4 + 2) × 0.5 = 15; Multi-lore 2 lores beyond 1st × 5 = 10. Wizard package totals to ~239 raw, contributing ~191 scaled to the Slann's price.

#### Identity-rule premia

Wizard-specific identity rules (Mark of the Wind, Mark of the Lady, Mark of the Old One, Master of Death, Mastery of All Winds, Bloodgreed, Vampiric Hunger, etc.) live in §13.3 Rule Contribution alongside other identity rules — priced inside the wound factor like normal stat-line content, not in the wizard package. The wizard package handles only the magic profile components; everything else routes through the standard framework.

**Loremaster** (Slann's *Focus of Mystery* Discipline at +32 raw) is a paid Discipline upgrade, not part of the chassis. It expands the wizard's known-spell list to "all spells in one chosen lore" — encoded as a flat upgrade cost on the unit profile, not through the SK component (which would generate an inflated SK premium for a flexible-but-not-actually-cast capability).

### 13.9 Unit-Class Scaling Guidelines *(added 2026-05-15 — Pass 11)*

A drafting-time guide for *what stats a unit at a given class should typically have*. The framework formulas in §13.1-13.8 produce correct *prices* given the stats — but only if the *stats* themselves are calibrated to the project's actual tier-scaling. This section codifies the W tiers, peer anchors, and drafting workflow per unit class.

**Motivation.** WHFB 8th edition stat-lines are *one* reference, but the project has consistently elevated stats above 8e canon at the Monstrous-Infantry-and-larger tier (Trolls W 7 vs 8e's W 3; Ogre Bulls W 7; Kroxigor W 8). A unit drafted at 8e stats and dropped into our framework prices like a *small* unit even though it's a large unit — the W-factor multiplier means a small mistake here cascades into a large pricing error. Recurring symptom: large-creature units priced ~3-4× too cheap when drafted directly from 8e canon.

#### No stat ceiling at 10 — stats may exceed 10 where lore-justified

The §2 to-hit and to-wound resolution is **formula-driven, not table-locked**. The to-hit formula reads *"3+ if MA > MD; 5+ if MA × 2 < MD; otherwise 4+"* — this extends cleanly to any value (MA 12 vs MD 20 evaluates to 4+; MA 15 vs MD 5 evaluates to 3+ trivially). The §2 *To-Hit (Melee) — MA vs MD* table at MA 1-10 / MD 1-10 is a **precomputed convenience**, not a stat cap. The same applies to the §2 To-Wound (S vs T) lookup.

In practice this means **legendary named characters, apex Monsters, and faction-anchor Lord-tier units may carry stats above 10 where the lore warrants it.** Examples that may surface in future drafts:

- **MA 11-12** for canonical "deadliest mortal" named characters (Gotrek Gurnisson, Tyrion of Ulthuan, the Witch King, Grand Master of the Old Ones-era apex characters)
- **S 8-10** for apex Monster natural-weapon profiles (Star Dragons, Black Dragons, Ancient Treemen, Bone Giants when drafted)
- **T 8-10** for stone-construct apex (Bone Giants, larger Khemrian constructs, the Anvil of Doom shrine when drafted at apex tier)
- **W 12-15+** for apex-Monster Lord-equivalents (Hell Pit Abomination max configuration, Verminlord, Hellpit Bone Giants)
- **Res 11-12** for unbreakable lore-anchors (Slann Mage-Priest with Disciplines, named Anvil-of-Doom-borne Runelords, Greater-Daemon characters when drafted)
- **I 8-9** for apex-reflex named characters (Tyrion, Witch King, Gotrek "slay-first" tier)

When a stat exceeds 10, the unit's pricing through §13.2 *Stat Contribution* and §13.3 *Rule Contribution* continues to apply linearly — the per-step modifiers (±0.5 MA/MD, ±1.0 S, ±1.5 T, etc.) extend without modification. **The 1-10 table at §2 is illustrative, not normative.**

This is a deliberate framework opening for the apex-tier identity space — without it, every legendary character bottoms out at the same MA 10 / MD 10 / S 10 ceiling, which compresses the lore's "vastly above mortal scale" framing into a tier already occupied by elite-but-not-named-character units.

#### Lore-height → unit-class crosswalk

A second cross-check for drafting: **how tall is the creature in lore?** Warhammer fantasy races span roughly 2-3' (Halflings, Snotlings) up to 20'+ (Dragons, Treemen, Wild Carnosaur), and the lore-canonical height maps reasonably cleanly to our unit-class tiers. When the peer-anchor list (below) leaves room for interpretation, fall back on lore-height: a 10'+ creature is Mon Inf or Monster, not Infantry, regardless of how the unit happens to be deployed mechanically.

| Lore-canonical height | Typical class | Typical W | Examples |
|-----------------------|---------------|-----------|----------|
| **~2-3'** (diminutive) | Infantry | W 1 | Halflings, Snotlings (rabble), individual Forest Goblin sneaks |
| **~3-4'** (small) | Infantry | W 1 | Dwarfs, common Goblins, larger Skinks, Night Goblins |
| **~4-5'** (mid-small) | Infantry | W 1 | Skaven (Clanrats, Stormvermin), Beastmen Gor, Halfling soldiery |
| **~5-6'** (standard) | Infantry (or Cavalry rider) | W 1 | Humans (Empire, Bretonnian, Chaos), High / Dark / Wood Elves, Half-Saurus / Skink-Saurus hybrids |
| **~6-7'** (tall humanoid) | Infantry — **W 3 for spawn-bred / cultivated-elite tier** | W 1-3 | **W 3 anchors:** Saurus Warriors (spawn-bred, T 4, broad-muscled), Black Orcs (Greenskin Disciplined elite, T 4, drilled brute). **W 2 anchors:** Wood Elf Dryads (bark-grown Forest Spirit frame). **W 1:** Chaos Warriors (mortal, despite the size — kept at standard Infantry W). The project supports an explicit *big-Infantry W 3* tier between standard W 1 rank-and-file and W 6+ Mon Inf — Saurus and Black Orcs occupy it as 6-7' tall elite-Infantry classes; the W 3 reflects the spawn-bred / drilled-veteran frame without crossing into the Mon Inf base-size or class |
| **~7-8'** (large humanoid / small monstrous) | **Monstrous Infantry — smaller tier** | **W 6** | **Rat Ogres** (lighter rat-bio frame, smaller than full-Ogre / Troll), Bestigor (some readings) |
| **~8-10'** (Ogre-tier) | **Monstrous Infantry — standard tier** | **W 7** | **Trolls, Ogre Bulls**, Tree Kin, Minotaurs (some readings) |
| **~10-12'** (large monstrous) | **Monstrous Infantry — heavier tier** | **W 8** | **Kroxigor**, larger Trolls (River, Stone), Chaos Spawn (high-end), Bestigor / Minotaur apex |
| **~12-15'** (Monstrous Cavalry mount tier / smaller Monster) | Mon Cav mount / smaller Monster | Mount W 3-4 / Monster W 6-8 | Demigryphs, Great Stags, Aggradons, smaller Treemen, Hippogriffs (when drafted) |
| **~15-20'** (Monster-tier) | Monster | W 8-10 | Wild Carnosaur, Stegadons, Treemen, larger Hippogriffs, Hell Pit Abomination |
| **~20'+** (apex Monster) | Monster | W 10-12+ | Dragons (Sun / Moon / Star tiers), Dread Saurian, Kroxigor Ancient, Verminlord (when drafted) |

**Drafting cross-check:** look up the unit's lore-canonical height. If the height is **7'+**, the unit is *probably* Monstrous Infantry or larger, regardless of any 8e-canon stat-line that might suggest otherwise. The height-tier should agree with the peer-anchor list; if they disagree, surface the conflict and resolve it explicitly rather than silently picking the lower tier.

*(Lore-height reference grounded against the "Rough Heights of Warhammer Fantasy Races (Expanded)" community-image — 2026-05-15. The Mon Inf 7'-12' band on this image corresponds to our W 6-8 tier, with creatures shorter than Ogres anchoring the W 6 lower-end.)*

#### Class W tiers (typical, refined per peer-anchor inventory 2026-05-15)

| Class | Typical W | Notes / Exceptions |
|-------|-----------|---------------------|
| **Infantry** | **W 1 (W 2-3 for elite biological tiers)** | W 1 is the default for most rank-and-file Infantry. **Explicit W-tier exceptions within Infantry class:** Dryads W 2 (Forest Spirit Infantry — bark-bodied bigger-than-elf-but-not-Mon-Inf bio frame); **Saurus Warriors W 3 (spawn-bred warrior elite)**; **Black Orcs W 3 (Greenskin Disciplined drilled-veteran elite)**. These W 2-3 Infantry units are still 25mm-base Infantry-class (not Mon Inf), but represent the "big-bodied / spawn-engineered / drilled-veteran" Infantry exceptions that the project supports as an explicit tier between standard W 1 rank-and-file and W 6+ Mon Inf |
| **Cavalry** | **W 1-2** *(rider + mount combined per §1 mounted-wound convention)* | Rider W 1 + mount W 1 → combined W 1 (Bret Knights, most rank-and-file cavalry). Rider W 1 + mount W 2 → combined W 2 (Imperial Knights, heavier cavalry; mount-W-2 = "Knightly Order" tier) |
| **Monstrous Infantry** | **W 6-8** | **The most-commonly-mis-drafted class.** Project standard: **W 6 for the lighter Mon Inf tier** (Rat Ogres — rat-bio frame, lighter than full-Ogre / Troll mass); **W 7** for standard Mon Inf brutes (Trolls, Ogre Bulls); **W 8** for the bigger Mon Inf tier (Kroxigor); **W 10** for the apex (Kroxigor Ancient, certain bio-engineered apex bio-creations). **Do not default to 8e canon W 3** — 8e Mon Inf were significantly under-statted relative to our project's elevated tier. The framework wound-factor (W 1=1.00, W 3=1.48, W 6=3.40, W 7=4.36, W 8=5.16) is calibrated against the W 6-8 baseline; pricing breaks if you use W 3 stats |
| **Monstrous Cavalry** | **Mount W 3-4** *(rider + mount combined per §1)* | Demigryph mount W 3 → combined W 3; Aggradon mount W 4 → combined W 4; Great Stag Knights mount W 3 → combined W 3 (Demigryph-parity). The Mon Cav mount-W band is *narrower* than Mon Inf because the rider's contribution is significant; the mount needn't carry the full durability burden |
| **Warbeast** | **W 1-3** | Skinks-on-Salamanders carrier W 4; War Lions W 3 (Skirmisher pride); Razordons W 3-4. The Warbeast class is genuinely variable — the lore-anchor matters more than a fixed band. Lower-end: Giant Rats W 1, Forest Goblin Wolf Riders mount W 1. Higher-end: bigger predator-beasts W 3-4 |
| **Monster** | **W 6-10+** | Treemen W 6-8; Stegadon W 8; Wild Carnosaur W 10; Dread Saurian W 12+; Hell Pit Abomination (pending) projected W 10+. Apex Monsters reach W 10-12; smaller / Hero-mounted Monsters at W 6-8 |
| **Chariot** | **W 3-6** | Held for chariot-tier review when more Chariot units are drafted |
| **Swarm** | **W 4-7** *(US = W convention)* | Swarms have W = US, so W tracks both durability and unit-strength simultaneously. Skink-Salamander-attendant Swarms W 4-5; bigger ground-swarms W 6-7 |

#### Peer-anchor reference (existing units, 2026-05-15 inventory)

When drafting a unit at a given class, **check the peer-anchor list FIRST** — not WHFB 8e canon. The peer-anchor is the project's authoritative W-tier:

**Infantry (W 1 baseline):**
- Dwarf Warriors W 1 / T 4 / 4+ save
- High Elf Spearmen W 1 / T 3 / 5+ save
- Empire Halberdiers W 1 / T 3 / 5+ save
- Clanrats W 1 / T 3 / 6+ save
- Stormvermin W 1 / T 3 / 4+ save (elite-Infantry, not Mon Inf despite "elite tier" framing — body-frame is unchanged)

**Infantry — W 2-3 exceptions (big-bodied / spawn-engineered / drilled-veteran Infantry tier):**
- **Saurus Warriors W 3 / MA 5 / MD 3 / T 4 / S 4 / 4+ NA+shield save / 30 pts** — the spawn-bred warrior anchor; 6-8' tall, broad-muscled, instinct-drilled. MA 5 at the cross-faction apex-elite-Infantry tier per the canonical lore
- **Black Orcs W 3 / T 4 / MA 5 / 29 pts** — the Greenskin Disciplined drilled-elite anchor
- **Dryads W 2 / T 4 / NA 6+ / 15 pts** — Forest Spirit Infantry, bark-grown bio-frame

**Monstrous Infantry (W 6-8 baseline):**
- **Rat Ogres W 6 / T 4 / S 5 / NA 6+ / 52 pts** — the *smallest* Mon Inf brute; Skaven bio-engineered, lighter rat-bio frame
- **Trolls W 7 / T 4 / S 5 / NA 5+ / 65 pts** — the canonical Mon Inf brute anchor
- **Ogre Bulls W 7 / T 4 / S 4 / 55 pts** — Mon Inf grunt; lower S
- **Kroxigor W 8 / T 5 / S 5 / NA 4+ / 112 pts** — the heavier Mon Inf tier
- **Kroxigor Ancient W 10 / T 6 / S 6 / NA 4+** — apex Mon Inf

**Monstrous Cavalry (mount W 3-4 baseline):**
- Demigryph Knights — mount W 3 / T 4 / S 4 / 2+ save / 50 pts
- Great Stag Knights — mount W 3 / T 4 / S 5 / 5+ save / 45 pts
- Aggradon Lancers — mount W 4 / T 5 / S 5 / 3+ save / 76 pts

**Monster (W 6+ baseline):**
- Wild Carnosaur W 10 / T 5 / S 7 / NA 5+ / 224 pts
- Treemen (projected) W 6-8 / T 6 / S 6-7
- Dread Saurian / Hell Pit Abomination (apex) W 10-12+

#### Drafting workflow (Mon-Inf-and-larger)

When drafting a unit that is plausibly Mon Inf, Mon Cav, Warbeast, or Monster, **follow this checklist**:

1. **Identify the class.** Use the unit's lore-size and base-size to determine class (Mon Inf = 40mm base, elite-rank-and-file = 25mm base, etc.). If a creature is "Ogre-sized" or larger, it's almost certainly Mon Inf or higher.
2. **Check the peer-anchor list above.** Find the existing units at the same class. The W-tier is locked there.
3. **Do NOT default to WHFB 8e stat-lines.** 8e Mon Inf were drafted under a different framework calibration; our project elevated the tier. Use peer-anchors as the truth source.
4. **Apply class stat-baseline bonuses** (per §13.2): Mon Inf +2 raw, Mon Cav +3, Monster +3 to +5. These are *structural* and easily forgotten.
5. **Apply US bonus** (per §13.2): US 3 = +1 raw for Mon Inf; US 5 = +2 for bigger Mon Inf or Mon Cav. The bonus is class-specific and easily forgotten.
6. **Wound factor (§13.1)** at the correct W tier: W 1 = 1.00; W 3 = 1.48; W 7 = 4.36; W 8 = 5.16; W 10 = 7.40. The 3-5× cost multiplier from getting W wrong is what causes the pricing error.
7. **Sense-check against peer cost.** If the unit you've drafted prices under 30 pts and the class is Mon Inf, something is structurally off — the Mon Inf tier sits at 55+ pts in our roster.

#### Pattern: under-statting large creatures

A recurring drafting error (called out 2026-05-15 after three corrections in two days):

- **Dryads** — initially mis-classified as Monstrous Infantry W 2; should have been Infantry W 2 (the unit IS Infantry, but if it were Mon Inf it would need W 7+, not W 2). User correction surfaced the misclassification.
- **Great Stag Knights mount** — initial draft W 2 mount; user correction bumped to W 3 (Demigryph-parity) at the Mon Cav tier.
- **Rat Ogres** — initial draft W 3 (Skaven 8e canon); first correction bumped to W 7 (Troll-parity); second correction (user refinement) settled at W 6 (the *smaller* Mon Inf tier — Rat Ogres are lighter than full-Ogre or Troll mass). Pricing trail: 19 pts → 65 pts → 52 pts. The W 6 anchor establishes that Mon Inf has a *band* (W 6-8) rather than a single W; the lower end is for lighter bio-frame creatures.

The pattern: defaulting to WHFB 8e stat-lines for large creatures, missing the project's elevated Mon Inf tier, and pricing the unit ~3× too cheap as a result. The §13.9 guidelines above are intended to prevent this recurrence.

---
