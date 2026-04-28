# Great Cannon


> The Empire's signature artillery piece — a black-powder cannon forged at the Imperial College of Engineers in Nuln, crewed by three engineers. Rolled into position, aimed, fired — the cannonball travels further than the human eye can follow, punches through plate, bounces through ranks, turns whatever it hits into debris. The Empire's answer to monsters, heroes, and heavy formations that won't bend to infantry work.

**Great Cannon (platform + crew, unified profile):**

| M | WS | BS | S | T (ranged) | T (melee) | W | I | Ld | LiS | US |
|---|----|----|---|---|---|---|---|----|-----|----|
| 2 | 3  | 3  | 3 | **7**      | **3**     | **5** | 3 | 8  | 2   | 2  |

*The platform and its Crew share a single unified profile. The unit has a **W 5 wound pool** — wounds accumulate on the machine as a whole. The crew is **not** individually removed as wounds are taken; the unit fires, fights in melee, and operates at **full output** until W reaches 0, at which point the cannon is destroyed (catastrophic structural collapse, last surviving crew lost with it). The dual Toughness reflects what's being hit: **T 7 when targeted by ranged attacks** (shots hit the bronze barrel and iron carriage), **T 3 when targeted in melee** (attackers reach the Crew past the platform). The War Machine's defining tension: devastating at range, almost unkillable by small arms, but genuinely vulnerable when something gets close — and **all-or-nothing under focused targeting** (a single magic missile or cannon shot doesn't drop it, but two or three coordinated shots will).*

**Points:** **110** for the Great Cannon (platform + crew bundle, W 5 baseline). +5 for optional **Reinforced Crew** upgrade (raises W to 6 and melee A to 4 — represents an additional engineer trained to assist with loading, sighting, and melee defence).

- **Keywords:** Empire, Human, **War Machine**, Special
- **Unit type:** **War Machine** — single unified profile. Dual Toughness (T 7 ranged / T 3 melee). W is a wound pool, not a crew count. Combat output stays at baseline until W=0. Can be charged normally; in melee, resolve against melee T
- **Unit composition:** 1 Great Cannon (fixed platform with attached crew, W 5 baseline). Optional: **Reinforced Crew** upgrade (+5 pts, W 6 / melee A 4)
- **Natural Armour:** 6+ (ranged attacks only — platform's bronze casing; Crew have no save in melee)
- **Ward Save:** —
- **Equipment (Crew):** Hand weapons baseline
- **Command options:** none (War Machines do not take champions, standards, or musicians)
- **Movement:** **M 2** — Crew may push the cannon 2" per turn voluntarily. Cannot Charge. May pivot freely up to 180° during Movement phase
- **Special rules:**
  - **War Machine** *(unit type)* — single-profile unit with dual T. Ranged incoming: T 7. Melee incoming: T 3. W is a wound pool — wounds accumulate but do not reduce combat output, melee A, or fire rate. The unit fires at full effectiveness from W=full all the way down to W=1; the cannon goes silent only at W=0 (destroyed). Can be charged normally. Cannot itself Charge
  - **Crew attack in melee** — Crew fight with hand weapons at unified WS 3, I 3, **A 3** baseline (A 4 with Reinforced Crew upgrade). Melee A is fixed and does not scale with remaining wounds — the crew fights at full effort until the machine is destroyed
  - **Imperial Engineers** *(identity rule)* — once per battle, the Crew may **re-roll the Artillery Die** for a cannon shot, including re-rolling a MISFIRE result. The re-roll stands (no re-re-rolling). Represents the Nuln Imperial Engineers' Guild training — the three engineers work the cannon with a precision and MISFIRE-recovery that other factions' artillery crews cannot match

**Weapon profiles:**

- **Great Cannon** *(ranged, Crew fire once per Shooting phase)* — **48" range | S 10 | AP -5 | D D6** — fired via the **Bounce Line** mechanic (below). One shot per Shooting phase. Crew must be alive (W > 0).
- **Hand weapon** *(Crew melee)* — 1" reach | **A 3** (or A 4 with Reinforced Crew) | S 3 | AP 0 | D 1 — fixed melee attack count, does not decrement with wounds

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

> **Lore notes:** First **War Machine** unit type in the ruleset. Single unified profile per design call — wound-pool model (W 5 baseline, no individual crew removal), no Mixed Unit split-W-pool complexity. Dual Toughness (T 7 ranged / T 3 melee) is the identity: at range the cannon is a fortress, in melee the Crew are fragile humans. **Getting into melee with a War Machine is the reward mechanism** — the enemy pays an activation / charge to reach the cannon, and once there the fight is favourable for them. Encourages the defender to place war machines behind friendly units, and the attacker to break through or flank. **Bounce Line** fires at **S 10 | AP -5 | D D6** — classic anti-anything cannon numbers; wounds Dread Saurian T 7 on 2+, cuts any Armour save to nothing (except native 1+), inflicts D6 damage per hit. **MISFIRE** cascades to a D6 severity roll — "cannon destroyed" (1) to "close call, no harm" (6); the 2-3 result inflicts D3 wounds on the unit's wound pool (no Ward, no Armour). **Bounce Line mechanic** replaces WFB's guess-distance skill-check with a cleaner "line extends Artillery Die inches" pattern; retains the long-range-heavy-damage-misfire-risk triangle that defines cannons while being mechanically simpler. **Imperial Engineers** identity rule gives one re-roll-the-Artillery-Die per battle — captures Nuln Guild training as a once-per-game reliability moment. **W 5 wound pool with no crew-decrement** — the cannon fires at full effectiveness from W=5 down to W=1, going silent only at W=0. This creates an **all-or-nothing tactical profile**: a single magic missile or enemy artillery shot doesn't drop the cannon, but two-three coordinated shots will. First-turn priority becomes critical in artillery-vs-artillery matchups. Points **110** (+10 over reference 100). The War Machine unit-type convention extends naturally to Mortar, Helblaster, Helstorm, Dwarf Cannons, Skaven Warpfire Thrower, Bretonnian Field Trebuchet (§17), etc. across factions.
