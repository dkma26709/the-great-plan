# Giant

> Thirty feet of drunken muscle, bad temper, and ill-fitting hand-stitched clothing — the Giant is one of the Old World's most iconic Monsters, fielded by Greenskin tribes who keep them well-fed (and well-bribed-with-beer), by Chaos warbands who twist them into things even more terrible, and by mercenary captains willing to risk having their own front rank crushed if a Giant should happen to **Fall Over** in the wrong direction. "Giants are creatures that Greenskin tribes would employ by rewarding them with food regularly, and in combat they would often charge mindlessly into enemy front-lines, usually wielding a massive club or tree as a weapon." The lore signature is twofold: **Random Attack Table** *(once per Combat phase the Giant rolls D6 to determine which kind of brutal lunacy it commits — Yell and Bawl, Pick Up and Eat, Jump Up and Down, Swing With Club, Thump, or 'Eadbutt — capturing the unpredictable drunken-rage Giant battlefield experience)* and **Fall Over** *(when the Giant dies, it pitches over in a random direction, dealing crush-hits on whatever's underneath — friend or foe — the iconic "killed your own troops with the Giant" lore moment)*. Drafted here under the **Greenskins faction** (the most common employer of Giants in the Old World; flagged as pending in the Greenskin FACTION.md), but the same profile is usable by Chaos warbands (with optional Mark-of-Chaos variants), Mercenary armies, and Dogs of War lists. The Greenskin battlefield read: pay the Giant's beer-bribe, send him stomping toward the enemy line, and hope the dice are kind — the Random Attack Table is part of the price of admission.

## Profile

| M | MA | MD | BS | S | T | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|----|-----|----|
| 6 | 3 | 2 | 1 | 6 | 5 | 12 | 3 | 10 | 5 | =W |

**Points:** 287 per model *(framework derivation under §13: stat-baseline 17.5 + rules 10.5 + equipment 3.0 = 31.0 raw × wound factor 11.56 (W 12) × 0.8 scaling = 286.7 → 287. **Pass 2 (2026-05-18):** W 8 → W 12 (wounds is the Giant's primary defence; the W jump more than doubles the wound factor, driving most of the price increase); Random Attack Table buffed across multiple results + two-table structure added (Small Enemies vs Big Enemies). **Pass 2.1 (2026-05-18):** 'Eadbutt A-reduction softened from rest-of-battle to next-round-only (-1.0 raw on Random Attack Table, -9 pts final). Now sits in the W 12 tier alongside Star Dragon (+511 mount-adder) and Tyrant (310 pts foot character) — the Giant is the cheapest W 12 unit in the codebase, reflecting Stupidity / MD 2 / no NA downsides offset by the strong Random Attack Table. See `design.md` for full working)*

**Unit size:** 1

**Unit type:** Monster (single model, no rider)

**Natural Armour:** — *(Giant biology — thick hide and enormous bulk, but no formal armour. The Giant's survival comes from raw W 8 wound pool and high Res 10 Stubborn / Imm Psych biology, not from scales or plate)*

**Base Size:** 50mm × 50mm (Giants are tall, not wide — a single large round base captures the model footprint)

**Keywords:** Greenskin-Allied, Giant, Monster, Rare *(also fielded by Chaos with optional Mark-of-Chaos overlay; by Mercenary armies; by Dogs of War lists)*

## Equipment

- **Equipment:** Giant Club / Tree-Trunk (natural — whatever oversized blunt weapon the Giant has fashioned or scavenged) + Whatever's at Hand (the Random Attack Table represents the Giant's varied combat repertoire). No worn armour, no shield, no rider.

## Special Rules

- **Stupidity** *(Psychology — per §8)* — the Giant is drunken, slow-witted, and easily distracted. At the start of each Movement phase, the Giant must take one of the following actions and nothing else: charge nearest visible enemy in range, OR advance full M toward nearest visible enemy, OR if no enemy visible, advance full M in a random direction. The Giant cannot March, cannot voluntarily target a specific unit beyond "nearest visible enemy."
- **Stubborn** *(Psychology-adjacent — per §8)* — the Giant ignores the state effects of Shaken and Wavering. The drunken brute doesn't notice when things are going badly. Combined with Res 10, the Giant rarely Breaks even when taking heavy damage.
- **Terror** *(per §8)* — at LiS 5, the Terror aura projects to **(6 + 5)" = 11"**. A thirty-foot-tall drunken Giant is terrifying to most mortal soldiers regardless of what the Random Attack Table rolls.
- **Random Attack Table** *(Giant unit identity rule — Pass 2: dual-table system + buffed results)* — At the start of each **Combat phase** in which the Giant is engaged in melee, instead of resolving normal Giant Club attacks, **roll a D6 to determine the Giant's attack for that Combat phase**. **The table used depends on the Giant's primary target unit:**

  - **Small Enemies Table** — used when the Giant's primary target unit contains *any* model with **per-model US ≤ 3** (typical rank-and-file Infantry, Cavalry, light Monstrous Infantry like Trolls at US 3, single-base characters, etc.)
  - **Big Enemies Table** — used when the Giant's primary target unit consists *entirely* of models with **per-model US ≥ 4** (Monsters, large constructs, apex Lord-mount combined models, large Monstrous Cavalry)

  *(If the Giant is engaged with multiple units simultaneously, the "primary target" is the unit in the Giant's front arc, chosen by the controlling player if ambiguous. Roll on the table once per Combat phase per Giant.)*

  ### Small Enemies Table *(target unit has any model with US ≤ 3)*

  | D6 | Attack | Resolution |
  |---|---|---|
  | **1** | **Yell and Bawl** | The Giant doesn't attack this Combat phase. Instead, every enemy unit within **12"** of the Giant immediately gains **+D3+2 stress** (mean ~4 stress). The Giant is too busy roaring obscenities at the heavens to actually hit anything, but the noise *carries* |
  | **2** | **Pick Up and Eat** | Select **one specific enemy model in base contact with US ≤ 3**. That model immediately takes an **Initiative test** (roll D6; if the result is ≤ the model's I, the model passes and escapes; if greater, the model fails). On a **fail**, the model is **removed as a casualty** (no save of any kind — armour, Ward, Regen do not apply), and the Giant **heals 1 W** (capped at starting W 12). On a **pass**, the model escapes the Giant's grasp; no effect this Combat phase. *(High-I models — Elves at I 5-7, certain Heroes — frequently dodge; low-I models — Trolls, Skaven slaves, dwarfs at I 2 — get caught reliably. Counterplay exists)* |
  | **3** | **Jump Up and Down** | The Giant makes **D6+1 Stomp hits** at **S 6 / AP 0 / D 1** on the unit in base contact. Hits are automatic; standard wound allocation applies |
  | **4** | **Swing With Club** | The Giant makes **2D6 attacks** at **S 6 / AP -2 / D 1** with his Giant Club. Hits at the Giant's MA 3 (vs target's MD); standard combat resolution applies. The "drunken wide swing" — many strikes (mean 7), lower per-hit damage but higher AP than other table results |
  | **5** | **Thump With Club** | The Giant makes **A 2 attacks** at **S 7 / AP -2 / D D3+1** with his Giant Club. Mean D damage 3 — solid per-hit punch |
  | **6** | **'Eadbutt** | The Giant makes **A 1 attack** at **S 8 / AP -3 / D D3** against a single enemy model in base contact (controlling player picks). **If this attack causes an unsaved wound**, the target model's **A characteristic is reduced by D3** (minimum A 1) **for the next round of combat only**. The target shakes off the stun after a round of recovery. *Lore: the 'Eadbutt rings the target's bell — they're physically dazed, swing-rate drops while they recover from the head-strike* |

  ### Big Enemies Table *(target unit consists entirely of US 4+ models — Monsters, large constructs)*

  | D6 | Attack | Resolution |
  |---|---|---|
  | **1** | **Yell and Bawl** | Same as Small Enemies Table (every enemy unit in 12" gains +D3+2 stress) |
  | **2** | **Grapple and Crush** | The Giant wrestles the Monster hand-to-hand. **A 2 attacks** at **S 8 / AP -3 / D D3+1** vs the Monster in base contact. The "I can't pick this thing up but I can bear-hug it" result. Replaces Pick Up and Eat (which can't apply against a Monster) |
  | **3** | **Jump Up and Down** | Same as Small Enemies Table (D6+1 Stomp hits at S 6 / AP 0 / D 1 — against a single-model Monster, this is D6+1 hits all applied to that model) |
  | **4** | **Swing With Club** | Same as Small Enemies Table (2D6 attacks at S 6 / AP -2 / D 1) |
  | **5** | **Thump With Club** | Same as Small Enemies Table (A 2 attacks at S 7 / AP -2 / D D3+1) |
  | **6** | **'Eadbutt** | Same as Small Enemies Table (A 1 attack at S 8 / AP -3 / D D3; if wounds, target's A reduced by D3 min 1 for rest of battle) |

  **Notes (both tables):**
  - The Random Attack Table replaces *all* of the Giant's normal Combat-phase attacks. The Giant does not also make a Giant Club attack on top; the table result IS the attack.
  - The Giant **must** be engaged in melee (in base contact with an enemy unit) to roll on the table. If the Giant is not engaged, no Combat-phase attacks happen.
  - The result is rolled freshly at the start of each Combat phase; the Giant may roll different results on consecutive turns.
  - **Imm Psych units** are NOT immune to Yell and Bawl's stress (the rule applies stress as a direct game-mechanic effect, not as a Psychology-tagged trigger — captures the audial impact of the Giant's roaring as a physical pressure on morale).

- **Fall Over** *(Giant unit identity rule — death-rattle)* — When the Giant is reduced to 0 W (i.e., would be removed as a casualty), **immediately before removing the model**, the Giant falls over in a random direction:

  1. **Roll a scatter die** (or, if scatter die unavailable, roll D8 / D6 for direction).
  2. The Giant's body falls in the rolled direction, extending **3D6"** from the model's current base position (roll 3D6 for the fall length; this represents how far the body sprawls).
  3. **Every model under the fallen-body line** (friend or foe — the Giant doesn't discriminate when crashing down) suffers **1 hit at S 6 / AP -1 / D D3 / no armour save** (Ward and Regen apply per standard).
  4. The Giant model is then removed.

  **Notes:**
  - The fall direction is fully random — including "back the way the Giant came," which often catches the Giant's own army's units. This is the iconic "killed your own troops with the Giant" lore moment.
  - The fall length (3D6") averages 10-11 inches — a long line that frequently catches multiple units.
  - Friendly-fire considerations apply: a Giant deployed in the centre of a Greenskin army may, on death, fall across multiple friendly units behind it. **Tactical implication:** deploy the Giant at the front edge, in advance of friendly forces, to minimise friendly-fire risk.

## Weapon Profiles

### Close Combat

The Giant's "weapon profile" is functionally the Random Attack Table above. For mechanical-reference purposes:

- **Giant Club / Tree-Trunk** *(natural — overridden by Random Attack Table during Combat phases when the Giant is engaged)* — 1" reach | **A 3 baseline** (replaced by Random Attack Table result in actual Combat) | S 6 | AP 0 | D 1 — the baseline weapon profile used only if for some reason the Random Attack Table cannot resolve (e.g., a rule that suppresses random rolls). In normal play, the Random Attack Table replaces this profile each Combat phase. `[Natural]`
