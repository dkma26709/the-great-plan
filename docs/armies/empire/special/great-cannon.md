# Great Cannon

> The Empire's signature artillery piece — a black-powder cannon forged at the Imperial College of Engineers in Nuln, crewed by three engineers. Rolled into position, aimed, fired — the cannonball travels further than the human eye can follow, punches through plate, bounces through ranks, turns whatever it hits into debris. The Empire's answer to monsters, heroes, and heavy formations that won't bend to infantry work.

## Profile

**Great Cannon (platform + crew, unified profile):**
| M | WS-A | WS-D | BS | S | T (ranged) | T (melee) | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|---|----|-----|----|
| 2 | 3 | 3 | 3 | 3 | **7** | **3** | **5** | 3 | 8 | 2 | 2 |

**Points:** 110 for the Great Cannon (platform + crew bundle, W 5 baseline). +5 for optional **Reinforced Crew** upgrade (raises W to 6 and melee A to 4 — represents an additional engineer trained to assist with loading, sighting, and melee defence).

**Unit type:** War Machine — single unified profile. Dual Toughness (T 7 ranged / T 3 melee). W is a wound pool, not a crew count. Combat output stays at baseline until W=0. Can be charged normally; in melee, resolve against melee T

**Natural Armour:** 6+ (ranged attacks only — platform's bronze casing; Crew have no save in melee)

**Base Size:** 60mm × 100mm (machine + crew)

**Keywords:** Empire, Human, **War Machine**, Special

## Equipment

- **Ward Save:** —
- **Equipment (Crew):** Hand weapons baseline

## Special Rules

- **War Machine** *(unit type)* — single-profile unit with dual T. Ranged incoming: T 7. Melee incoming: T 3. W is a wound pool — wounds accumulate but do not reduce combat output, melee A, or fire rate. The unit fires at full effectiveness from W=full all the way down to W=1; the cannon goes silent only at W=0 (destroyed). Can be charged normally. Cannot itself Charge
- **Crew attack in melee** — Crew fight with hand weapons at unified WS 3, I 3, **A 3** baseline (A 4 with Reinforced Crew upgrade). Melee A is fixed and does not scale with remaining wounds — the crew fights at full effort until the machine is destroyed
- **Imperial Engineers** *(identity rule)* — once per battle, the Crew may **re-roll the Artillery Die** for a cannon shot, including re-rolling a MISFIRE result. The re-roll stands (no re-re-rolling). Represents the Nuln Imperial Engineers' Guild training — the three engineers work the cannon with a precision and MISFIRE-recovery that other factions' artillery crews cannot match

## Options

**Command options:** none (War Machines do not take champions, standards, or musicians)

## Weapon Profiles

### Close Combat

- **Hand weapon** *(Crew melee)* — 1" reach | **A 3** (or A 4 with Reinforced Crew) | S 3 | AP 0 | D 1 — fixed melee attack count, does not decrement with wounds `[1H Blade]`

**Bounce Line mechanic** *(new ranged weapon rule — Great Cannon and similar line-firing war machines)*:

1. Declare a target direction within the cannon's **forward 90° arc** (facing +/- 45°). No specific target unit must be named.
2. Place a straight line from the cannon's muzzle, up to **48" long**, in the declared direction (player chooses landing point).
3. Roll the **Artillery Die** (2/4/6/8/10/MISFIRE) for the **bounce**: cannonball lands at chosen point, then **bounces forward Artillery Die inches** along the same line.
4. Every model (friendly or enemy) whose base is touched by either the initial impact point or the bounce-line segment is hit at **S 10 | AP -5 | D D6**. Ward and Regeneration saves apply; Armour at AP -5 effectively null except for native 1+ saves.
5. **MISFIRE result** — no shot fired this phase. Roll **D6** on the Cannon Misfire Table:
   - **1** — cannon destroyed. The unit is removed (all remaining wounds lost).
   - **2–3** — cannon damaged; cannot fire next Shooting phase. **D3 wounds** inflicted on the unit (no Ward, no Armour).
   - **4–5** — cannon jammed; cannot fire next Shooting phase. No wounds taken.
   - **6** — close call — cannon operable next phase; no wounds taken.

### Ranged

- **Great Cannon** *(ranged, Crew fire once per Shooting phase)* — **48" range | S 10 | AP -5 | D D6** — fired via the **Bounce Line** mechanic (below). One shot per Shooting phase. Crew must be alive (W > 0).
