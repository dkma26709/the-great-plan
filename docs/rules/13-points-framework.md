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

For units with **pooled wound counts** (Rider and Mount Profiles, per §1), use the combined W value. For units with **A=W / US=W dynamic stats** (Jungle Swarms and similar), use the starting (maximum) W value.

### 13.2 Stat Contribution

Start from a **baseline of 5**, representing a standard grunt — WS3 S3 T3 W1 I3 A1 Res7 M4, 6+ save. Adjust per the tables below.

**Per-stat modifiers:**

| Stat | Modifier per point from baseline |
|------|----------------------------------|
| WS | ±0.5 |
| S | ±1.0 |
| T | ±1.5 |
| I | ±0.5 |
| A | ±1.5 per attack |
| Res | ±0.5 |
| M | ±0.25 (M4–M8 range; M9+ scales faster per judgement) |
| Save | +1 per step above 6+ (5+ = +1, 4+ = +2, 3+ = +3, 2+ = +4) |

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

| Rule | Contribution |
|------|--------------|
| Stubborn | +2 |
| Predatory Fighter | +2 |
| Fast Cavalry | +2 |
| Aquatic | +0.5 |
| Skittish | -0.5 |
| Skirmishers | +1.5 |
| Elusive | +1.5 |
| Fly (10) | +3 |
| Fly (12) | +4 |
| Fly (14+) | +5 |
| Strider (X) | +0.5 |
| Chameleon | +2 |
| Mixed Unit | +0.5 |
| Unbreakable | +3 |
| Unstable | -2 |
| Stupidity | -2.5 |
| Expendable | 0 |
| Dispersed Mass | +2 |
| Smothering Mass | +3 |
| Poisoned Attacks | +1 |
| Magical Attacks | +1 |
| Ward Piercing (X) | +X |
| Multiple Shots (X) | +0.5 × (X-1) |
| Quick to Fire | +0.5 |
| Random Attacks | 0 |
| Random Movement | -1 |
| Swarm dynamic stats (A=W) | +2 |

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

### 13.4 Equipment Contribution

Weapons are rolled into stat contribution. Representative values:

| Weapon characteristic | Contribution |
|-----------------------|--------------|
| 1" hand weapon (implicit baseline) | 0 |
| 2" reach melee | +0.5 |
| 3" reach melee | +1 |
| AP -1 per step | +0.5 |
| D2 melee | +1 |
| Charge-only bonuses (e.g., +1 S, AP -1, D2) | +1 to +1.5 |
| Ranged 8"–12" D1 | +0.5 |
| Two-handed | 0 (trade-off against shield slot) |
| Poisoned built into weapon | +1 |
| Multiple Shots built into weapon | +0.5 × (X-1) |
| Killing Blow on weapon | +1 to +2 |
| Flame Template weapon (S4 Flaming, Slow to Fire, Artillery Die scatter) | +4 |
| Ranged volley weapon (18"+, Multiple Shots, AP -1) | +3 to +4 |

### 13.5 Calibration

The framework has been fit against the current roster of priced units:

| Unit | Stat Sum | W | Factor | Computed | Draft | Δ |
|------|----------|---|--------|----------|-------|---|
| Skink Cohort | 5.5 | 1 | 1.00 | 6 | 5 | -1 |
| Skink Skirmishers | 9.0 | 1 | 1.00 | 9 | 8 | -1 |
| Terrawings | 7.0 | 1 | 1.00 | 7 | 7 | 0 |
| Raptadon Hunters | 14.5 | 2 | 1.16 | 17 | 17 | 0 |
| Saurus Warriors | 19.0 | 2 | 1.16 | 22 | 22 | 0 |
| Temple Guard | 27.5 | 2 | 1.16 | 32 | 35 | +3 |
| Kroxigor | 22.25 | 6 | 3.40 | 76 | 75 | -1 |
| Jungle Swarms | 7.25 | 7 | 4.36 | 32 | 32 | 0 |
| Aggradon Lancers | 35.75 | 6 | 3.40 | 122 | 120 | -2 |
| Chameleon Skinks | 13.5 | 1 | 1.00 | 14 | 14 | 0 |
| Salamanders (beast only — M8 A3, NA 6+) | 19.5 | 5 | 2.60 | 51 | 65 | +14 |
| Salamanders (beast + 3 handlers bundle) | — | — | — | 66 (formula) | **80** (priced) | +14 |
| Razordons (beast only — M8 A3, NA 5+, Rapid Fire) | 21 | 5 | 2.60 | 55 | 65 | +10 |
| Razordons (beast + 3 handlers bundle) | — | — | — | 70 (formula) | **80** (priced) | +10 |
| Horned One Riders (M10, no Aquatic) | 18.5 | 2 | 1.16 | 21 | **28** | +7 |
| Terradon Riders (Fly 14, W4 pool, A2 mount, javelin default) | 22 | 4 | 1.96 | 43 | **42** | -1 |
| Ripperdactyl Riders (Fly 12, W4 pool, AP -2 mount) | 23.5 | 4 | 1.96 | 46 | **46** | 0 |
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
- Pooled wound units (Cavalry with Rider + Mount profiles) use the combined W value. Separate-model units with the same total wounds (e.g., two W1 models) are **cheaper per wound** because they split durability rather than pooling it — an Infantry unit of 10 × W1 models is not interchangeable with a Cavalry unit of 5 × W2 models for formula purposes.
- Points are rounded to the nearest whole number. Fractional results below 0.5 round down; 0.5 and above round up.
- The quadratic wound factor is calibrated against the current roster. As new units join (including ones with W8+ or unusual profile shapes), the factor curve may need adjustment at the extremes.
- **Extreme W (W9+) factor extension.** The quadratic factor escalates steeply past W8 (W8 = 5.48, W12 = 11.56 at the raw formula) which in practice over-prices Monster-scale units at the very extreme end. At high wound counts, durability is no longer purely linear with the attacker's difficulty of killing the unit — the enemy concentrates fire on the apex model, key abilities (Sniper, Ward Piercing, high-AP weapons) are brought to bear, and focus-fire becomes easier not harder. For W > 8 the framework applies a **linear extension**: `factor(W) = factor(8) + 0.5 × (W − 8)`. This produces W9 = 5.98, W10 = 6.48, W11 = 6.98, W12 = 7.48 — a scale that still reflects Monster durability premium without the raw quadratic runaway. The 0.5-per-W coefficient was calibrated against the Bastiladon (W10, 2+ save, heavy-relic bundle) and Stegadon (W12) to produce points that match the "Monsters cost real money" design intent. Playtest-tunable.
- **Extreme save values (2+ and lower).** Armour Save contributions scale linearly per §13.2 (+1 per step above 6+), but the *effective* durability gain from a 2+ save is sharply non-linear — a 2+ save against AP 0 weapons passes 83% of rolls vs 50% at 4+, so the effective-wound multiplier is much higher than the linear +4 contribution suggests. Units with a native 2+ save (typically Monsters with biological armour) are under-priced by the formula; adjust upward case-by-case. Bastiladon is priced at 150 vs formula 90 partly for this reason (the other part being the howdah-relic bundle).

---
