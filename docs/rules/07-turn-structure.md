# §7 Turn Structure


A turn proceeds through six phases in order. Within each non-deterministic phase, players alternate activating units one at a time.

| # | Phase | Activation |
|---|-------|-----------|
| 1 | Start of Turn | — |
| 2a | Movement — Charges | Alternating |
| 2b | Movement — Normal Movement | Alternating |
| 3 | Magic | Alternating |
| 4 | Shooting | Alternating |
| 5 | Combat | Initiative order |
| 6 | End of Turn | — |

One player is the *active player* for the turn. The active player declares first in each alternating phase.

### 1. Start of Turn

Turn counter advances. Then, in order:

1. **"Start of turn" effects** resolve (General slain follow-up stress, spell durations, any other triggered effects).
2. **Recovery rolls.** Every unit rolls D3 (+ modifiers from musician, BSB, General reroll) and removes that much stress.
3. **Threshold check.** Each unit's stress is compared against its Ld-based thresholds. States (Shaken, Wavering, Broken) are applied or removed. Broken units will flee in the Movement phase.
4. Active player determination — the active player swaps each turn.

### 2. Movement Phase

Divided into two sub-phases: **Charges** (all charges declared and resolved first) and **Normal Movement** (everything else).

#### 2a. Charges sub-phase

Players alternate declaring charges. The active player declares first. For each declared charge:

1. **Declare target.** The charger picks an enemy unit in sight and within charge range (Formed M + D6; Loose M + 2D6).
2. **Determine charge arc.** Based on the charger's position *before any charge movement*, relative to the defender's facing (see §6).
3. **Stand and Shoot.** The defender may declare Stand and Shoot as a charge reaction **only if the distance between the charger and the defender is greater than the charger's M value**. If the charger's M is equal to or greater than the distance, the charger closes too fast to react and no Stand and Shoot is permitted. The defender must also have eligible shooting models (per §7.4) and cannot have already shot this turn. Once declared, the defender's unit has used its Shooting-phase activation for the turn.
4. **Roll charge distance.** D6 or 2D6 as appropriate.
5. **Charge movement.** The charger moves along its path, wheeling up to 45° if needed to reach contact. Charge distance is measured along the wheel path.
6. **Resolve Stand and Shoot** (if declared). Each eligible model in the defending unit makes one ranged attack against the charging unit at **-1 to hit**. Stand and Shoot represents hurried, reactive fire — not a normal shooting-phase volley.
    - **Eligibility per model:** the charger must be in the model's weapon range, in its shooting arc, and visible. Models in the defender's own unit do **not** block LOS (the volley is a unit act). The target is measured to the charger's **final position** after its charge move (whether contact was made or not).
    - **Weapon rule interactions:** **Quick to Fire** ignores the -1 to-hit penalty. **Slow to Fire** cannot participate. **Multiple Shots (X)**, **Rapid Fire**, **Ponderous**, and **Move or Fire** apply per their normal effects.
    - **Failed charges:** Stand and Shoot resolves even if the charge fails due to insufficient distance — the volley flies at the closing enemy regardless of whether they reach contact.
7. **Apply casualties** to the charger (front-rank models first). If coherency breaks or the unit is reduced below charge eligibility, the charge fails — the unit ends at its stopping point and cannot act further this turn.
8. **Resolve contact.** If the charge succeeds, the charger ends in weapon reach of a target model.
9. **Impact attacks.** If any model in the charging unit has a weapon with the Impact keyword (see §8), those attacks are resolved now — before the Combat phase begins. Apply wounds, make saves, remove casualties. If the defender's formation breaks or it is reduced, that state persists into the Combat phase.

Alternation continues until both players pass or have no eligible chargers remaining.

#### 2b. Normal Movement sub-phase

Players alternate moving units. Units that declared a charge this turn (successful or failed) do not move again. Other units may:

- Advance, March, Rally (see §6)
- Wheel (Formed units only)
- Any combination within their movement allowance

Alternation continues until both sides have moved every unit they wish.

### 3. Magic Phase

The Magic phase runs on a two-tier dice-pool economy: each wizard has **personal Cast and Dispel pools**, and each player has a small **shared magic pool**. Casts and dispels are paid in dice from these pools. Rolling more dice raises the ceiling of the result but also increases the risk of miscasting. Activations serve only as the back-and-forth cadence between players — there is no per-wizard cap on how many spells a wizard may cast as long as they have dice and uncast spells.

#### Phase Setup

At the start of each Magic phase (after first-activation is determined per §7.1), each player in turn performs the following, independently (asymmetric — the two players roll their own pools):

1. **Personal pools.** For each of your wizards, place **Cast Base** dice in that wizard's Cast pool and **Dispel Base** dice in their Dispel pool.
2. **Channeling rolls.** For each of your wizards, roll **Channelling D6s**. For every result of **5+**, gain one extra die — placed, at your discretion, into that wizard's Cast pool *or* Dispel pool. A wizard with Channelling 0 rolls nothing.
3. **Shared magic pool.** Roll **`floor(points limit / 1000)` D3**, minimum 1D3. The sum is your shared magic pool for the phase — external to any specific wizard, usable on any of your casts or dispels.

All pools are **per-player**. Unused dice are **lost** at phase end unless a specific rule (typically RIP or similar persistent effects) says otherwise.

#### Turn Structure

Players alternate magical activations. The player with first activation this turn acts first. On your activation you nominate one of your wizards as the caster and cast one spell; resolve the cast (including any opponent dispel attempt) before the opponent takes their activation.

A wizard may be nominated if:

- They have at least **1 unspent Cast Die** in their personal Cast pool (shared-pool dice may supplement but cannot substitute this minimum), AND
- They have at least one spell from their known set that they have not already cast this turn

A player **passes** when they choose not to cast — even if able, a player may pass to conserve dice for dispelling. When both players pass consecutively, the Magic phase ends.

There is **no per-wizard cap** on casts: a wizard may keep casting as long as they have Cast Dice and uncast spells. Activations exist purely as back-and-forth pacing.

**Spell restrictions:**

- A wizard may not cast the same spell more than once per turn.
- A unit may not be targeted by the same spell more than once per turn, regardless of which wizard casts it. **Exception:** direct damage spells (magic missiles and similar) may target the same unit multiple times from different casters — they are magical shooting, not persistent effects.

**Range and line of sight** are defined per spell. Some spells require line of sight; others do not. Some target a point on the battlefield; others target a unit. The spell's description is authoritative.

**Spells Known** is set per army book entry — the number of spells the wizard selects from their available lores during list building, up to the tier their Lore Access permits. The special rule **Loremaster** replaces this: the wizard knows all spells in the specified lore up to their Lore Access tier.

#### Casting a Spell

1. **Declare** the spell and its target.
2. **Invest dice.** The casting wizard declares how many dice to invest from their personal Cast pool. Shared-pool dice may also be spent (one-for-one, each adding one die to the cast). **There is no upper limit on dice invested.**
3. **Roll all invested dice.**
4. **Bonus D6s.** For each natural **6** rolled in the cast pool, roll **one additional D6** and add its result to the sum. Bonus D6s count as rolled dice for miscast purposes (below). Bonus D6s do **not** themselves generate further bonuses — there is no chain.
5. **Cast result** = sum of all dice (initial + bonuses) + **Cast Bonus** (capped +5).
6. **Compare to casting value.** If the cast result meets or exceeds the spell's CV, the cast succeeds (subject to dispel). If lower, the cast fails.
7. **Check for miscast** (below). Miscasts apply regardless of success or failure — there is no auto-fail from miscast; the cast resolves at its face-value result.

**Invested dice are spent** whether the cast succeeds, fails, or miscasts.

#### Dispelling

After a spell is successfully cast, the opposing player may attempt a single dispel attempt, provided they have at least one wizard eligible to act as lead dispeller:

1. The **lead dispeller** must be within **Dispel Range** of the spell's target (or of the casting wizard, for spells with no target point).
2. The player must have at least 1 Dispel Die available (personal or shared) to invest.

**Procedure:**

1. **Nominate the lead dispeller.**
2. **Nominate supporting wizards.** Any other friendly wizards *also within their own Dispel Range* of the target may contribute dispel dice.
3. **Invest dice.** The lead and each supporter may invest any number of Dispel Dice from their personal pools. Shared-pool dice may also be added. **No upper limit.**
4. **Roll all invested dice.**
5. **Bonus D6s.** Each natural **6** grants a bonus D6 (same mechanic as casting).
6. **Dispel result** = sum of all dice (initial + bonuses) + **lead wizard's Dispel Bonus + 1 per supporting wizard** (total effective Dispel Bonus capped at **+5**).
7. **Compare to cast result.** If dispel ≥ cast result, the spell is nullified. The caster's invested dice are still spent.
8. **Check for dispel miscast** (below).

Only one dispel attempt per cast. If the dispel fails, the spell goes through.

> Dispelling is harder against a wizard who rolled well. A Slann who pushes six dice through and rolls bonus D6s on a pair of 6s has set a result of 25+ — taking that down requires a committed defensive effort, possibly pooling multiple wizards and burning shared dice. Rolling high on a cast isn't wasted — it doubles as dispel resistance.

#### Miscasts

**Cast miscast trigger.** When a cast roll contains **two or more natural 1s** — counting initial invested dice and any bonus D6s together — the cast miscasts. The cast still resolves at its rolled value; miscasts do **not** cause the spell to auto-fail.

**Cast miscast severity.** Compute severity as (**total dice rolled**, including bonuses) **+ D3**, then apply the matching row:

| Severity | Consequence |
|----------|-------------|
| 3–4 | 1 wound (no save) + 1 stress |
| 5–6 | D3 wounds (no save) + 1 stress |
| 7–8 | D3 wounds (no save) + 2 stress; wizard loses all remaining personal **Cast Dice** this phase |
| 9+ | **D3+1 wounds** (no save) + 2 stress; wizard loses all remaining personal **Cast *and* Dispel Dice** this phase; wizard **forgets the spell** for the rest of the game (cannot attempt it again this battle) |

Wounds ignore all saves (armour and ward alike). Stress is always applied, regardless of severity tier. The spell-forgetting at 9+ applies only to the miscast spell, not to the wizard's other known spells.

Miscasts chip away at a wizard's durability and tempo. A wounded wizard can keep casting in subsequent turns, but they are closer to death, more stressed, and — at the extreme — have lost the very spell that burned them.

**Dispel miscast (lite).** If a dispel roll contains **two or more natural 1s**, the dispel fails (the spell goes through) and the **lead dispeller suffers 1 wound** (no save). No stress, no dice loss, no severity scaling — the defensive miscast is a deliberately lesser consequence than offensive miscasting. Defence still costs something when it breaks, but cannot become a wizard-killer.

#### Shared Magic Pool

The shared pool is rolled once per Magic phase (see Phase Setup). Dice may be spent:

- **On casts.** One shared die adds one die to the casting wizard's cast roll. It rolls with the rest of the cast pool and counts identically for bonuses, miscast triggers, and severity.
- **On dispels.** One shared die adds one die to any dispel attempt, rolled alongside the pooled dispel dice.

Shared dice are committed as they are allocated — once spent on a cast or dispel, they are gone. Unused shared dice are lost at phase end.

#### No Irresistible Force

There is no automatic success on any cast. Even a roll of all 6s must meet the CV on its summed value. In practice, after bonus D6s are rolled, such a roll will almost always succeed — but pushing hard is still genuine risk: more dice always means more potential natural 1s, and high-dice miscasts sit in the top severity tier.

#### Remains In Play

Certain spells have the **Remains In Play (RIP)** keyword. A RIP spell is cast as normal, resolving its initial effect immediately, and then **persists on the battlefield** — continuing to apply its effect during each subsequent Magic phase of the controlling player's turn.

**Dispelling a RIP spell:**

- **On the turn it is cast:** the opponent's single dispel opportunity (the normal reaction to the cast) is the only chance to stop it. If the opponent chooses not to dispel, or the dispel attempt fails, the spell is locked in for that turn — no second dispel is permitted the same turn.
- **In subsequent turns:** the opponent may spend one dispel activation during the caster's Magic phase to attempt to dispel the RIP spell. Roll 2D6 + Dispel Bonus against the spell's original casting result. Only one dispel attempt per RIP spell per turn.

**Caster voluntary end:** the caster may voluntarily end a RIP spell at any time, at no activation cost.

**Multiple RIP spells:** a wizard may maintain any number of RIP spells simultaneously. Each must be dispelled separately.

**Caster death:** the caster being slain does **not** automatically end their RIP spells — the magic was released, not tethered.

**Effect timing:** RIP spell effects that produce ongoing damage or state changes trigger during the controlling player's Magic phase each turn (after the initial cast's turn), unless the spell specifies different timing.

#### Summoning

Certain spells have the **Summoning** keyword. A Summoning spell creates a **permanent effect on the battlefield** that persists for the rest of the game — a new terrain feature, a lasting alteration of the battlefield, or a summoned entity.

**Dispelling:** the opponent's single post-cast dispel reaction is the **only chance** to prevent a Summoning spell from taking effect. Once the cast succeeds past that reaction, the summoned effect is permanent — it cannot be dispelled in subsequent turns.

**No ongoing cost:** unlike RIP, Summoning spells do not require the caster to remain alive to maintain the effect. The caster's death does not undo a summoned feature or entity.

**No voluntary end:** the caster cannot voluntarily unmake a Summoning. What was called is called — the grove grows, the creature exists, and only external intervention (unit destruction for summoned entities, or specific rules that remove terrain) can undo it.

This makes Summoning spells genuinely decisive: the opponent must stop them at the cast or live with the battlefield change for the rest of the game. They are typically high casting values to balance this weight.

#### Magic Resistance

Magic Resistance is a defensive special rule defined in §8 (Magic Resistance (X) reduces the casting roll of enemy spells targeting the unit). See the glossary for full details.

### 4. Shooting Phase

Players alternate activating units that wish to shoot. One unit shoots at a time, resolving all its eligible models' shots, before the opposing player activates the next unit.

#### Eligibility per model

A model may shoot if all of the following are true:

1. It has a ranged weapon in hand
2. It is not engaged (no enemy model is within melee reach of either side — see §4)
3. The target is within the weapon's range
4. The target is within the model's shooting arc (below)
5. The model has line of sight to the target (below)
6. The model has not already shot this turn (e.g., via Stand and Shoot)

#### Shooting arcs

- **Formed units:** all models share the unit's facing. Shooting arc is the 90° front cone from that facing.
- **Loose units:** each model has its own facing (set during movement — no free pivot at shooting time). Each model shoots within its own 90° front cone.
- **Single models** (monsters, characters) use the 90° front cone from the miniature's physical facing.
- **360° shooting** is not a default. A unit-specific special rule may grant it.

#### Line of Sight

Every unit has a **LiS** (Line of Sight value) on its profile. Line of sight from shooter to target is **clear** if *either* the shooter's LiS *or* the target's LiS is greater than the LiS of every intervening model. Otherwise **blocked**.

Reference LiS scale:

| LiS | Typical |
|-----|---------|
| 0 | Swarms (low to the ground; do not block line of sight) |
| 1 | Infantry, characters on foot |
| 2 | Monstrous Infantry, Cavalry, Warbeast |
| 3 | Monstrous Cavalry, Chariots, small monsters |
| 4 | Standard monsters |
| 5 | Large monsters, dragons, giants |

Intervening models include friendly units, enemy units, and parts of the shooter's own unit — **except** during Stand and Shoot (see §2a), where the shooter's own-unit models are ignored for LOS.

#### Target selection

- **Formed units** fire at a **single** target unit — disciplined volley; all eligible models shoot at the same enemy.
- **Loose units** may split fire across up to **two** target units; each model selects its own target within its range, arc, and LOS.

A unit's shooting is a single alternating action — all its eligible models shoot together, then the opposing player activates the next unit.

#### Move-and-shoot

A unit that made any **voluntary movement during its own activation** this turn (Advance, March, Wheel, reform) suffers **-1 to hit** on all shots this turn. Stand and Shoot is exempt (it is a reaction, not a Shooting-phase activation). Involuntary relocation (push-back, forced movement from spells, Impact displacement) does **not** count.

Several weapon rules modify the baseline (see §8):
- **Quick to Fire** — ignores the -1 penalty entirely.
- **Ponderous** — **-2 to hit** if the unit moved (replaces the -1).
- **Move or Fire** — cannot fire at all if the unit moved.
- **Slow to Fire** — no move-penalty impact, but the weapon cannot be used in a Stand and Shoot reaction.

#### Cover

Two cover levels modify to-hit rolls against the target unit:

- **Soft cover** (**-1 to hit**): partial concealment without a physical barrier — tall grass, light foliage, smoke, brush, low fences, shooting through a screen of much-smaller friendly models (e.g. Skink screen in front of Saurus).
- **Hard cover** (**-2 to hit**): physical obstruction between shooter and target — walls, buildings, heavy rocks, the trunk rank of a wood, fortifications.

**Eligibility (unit-level):** a target unit counts as being in cover if **50% or more of its visible models** (from the shooter's angle) are in, behind, or obscured by the cover feature. All hits on the unit then suffer the cover modifier — cover is not tracked per model or per hit.

**Stacking:** if multiple cover sources would apply, use only the **best single source** (the biggest penalty). Cover does not sum — a unit behind a wall *inside* a wood still gets -2, not -3.

**Over-shooting:** a shooter on elevated terrain looking clearly over a cover feature at a lower target ignores that cover feature's benefit.

**Templates:** templates ignore cover entirely — they fall where they fall, regardless of what's between shooter and target. Cover applies to hit rolls, not to area-effect placement.

**Setup convention:** players should agree at the start of the game which ambiguous terrain features provide soft vs hard cover (ruins, hedges, dense brush etc.).

#### Templates

Three standard template shapes:

- **Flame Template** — teardrop cone, roughly 8" long and 3" wide at the base. Used for breath weapons and burst-fire weapons.
- **Small Round Template** — 3" diameter circle. Used for grenades and small spell areas.
- **Large Round Template** — 5" diameter circle. Used for cannon rounds, artillery, and mass spell areas.

**Placement:** the wielder nominates a point within the weapon's Range (for ranged attacks) or the spell's range (for magic). The template centres on that point, then scatters per the weapon/spell profile.

**Scatter:** weapons and spells specify **Scatter (X)**, where X is the scatter distance dice expression (D3, D6, 2D6, Artillery Die, etc. — see §8 Scatter (X)). Roll a **scatter die** (4 arrow faces + 2 HIT faces) together with the specified distance roll.
- **HIT face:** the template lands exactly on the nominated point; no scatter.
- **Arrow face:** the template moves the scatter distance in the indicated direction.
- **BS modifier (ranged weapons only):** the scatter distance is reduced by the wielder's BS, minimum 0. Spells do not apply a BS modifier — the scatter die roll is the whole uncertainty.

**Partial coverage:** a model is **under the template** if the template covers any part of the model's base. Each model under the template is resolved as one hit from the weapon's or spell's profile.

**Base overlap:** if the final template position would overlap a model's base entirely, move the template the smallest distance in the direction of scatter needed to clear the base. Models the template initially passes through are still "under" the template.

**Cross-unit coverage:** a single template may cover models from multiple units. Each model takes a hit; apply damage unit by unit, with each unit rolling its own saves and wound allocation separately.

**RIP template behaviour:** by default, a template from a Remains In Play spell **re-scatters** at the start of each controlling-player's Magic phase (scatter die + distance, no BS mod). Per-spell text may override:
- "Stays in place" — the template does not move after initial placement.
- "Moves in [direction]" — the template moves a specified distance each phase in a specified direction (e.g. scatter die direction, or "directly forward").

**Breath Weapons:** a breath weapon is simply a ranged weapon profile that uses the flame template. Usable repeatedly like any other ranged weapon — no once-per-phase limit.

**Multi-model units with template weapons:** when a unit contains multiple models each armed with a template weapon (e.g., a unit of Salamanders, each with its own Spout Flames), **each such model places and resolves its own template independently**. Each fires with its own scatter die roll, its own distance-dice roll (Artillery Die, D6, etc. per the weapon's Scatter expression), and its own misfire check if applicable. Templates may overlap: **a model under two templates takes two hits**, one from each template, resolved separately. A model under three templates takes three hits, and so on. This is the natural consequence of each model being an independent shooter, and it is intended — stacked templates represent mass breath-weapon fire concentrated on a single target area.

A multi-model template-weapon unit may split its templates between multiple target points (each model may choose its own nominated point, within that model's own Range and line of sight) or concentrate all templates on a single target. No coordination bonus applies; no penalty either. Each shot is its own shot.

### 5. Combat Phase

Every unit with at least one model within melee reach of an enemy fights. Strikes resolve in **Initiative order**, high to low, across both armies. Ties are simultaneous.

Charging bonuses (+1 I this round, per §4 and §6) apply to units that successfully charged in this turn.

Combat mechanics — attacks, wounds, saves, combat resolution, fall-back — are described in §4 *Attacks and Combat*. Combat resolution and fall-back resolve at the end of the Combat phase, not in End of Turn.

### 6. End of Turn

- Any "at end of turn" effects resolve (spell durations expire, etc.).

Stress thresholds are **not** checked here — recovery and threshold checks happen at the Start of the next Turn (§7.1), giving units a chance to recover before consequences take effect.

---
