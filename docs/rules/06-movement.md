# §6 Movement, Positioning, and Formation


### Base Movement

Each unit has a Movement value in inches. On its activation, a unit may take one of the following actions:

- **Advance:** move up to M inches in any direction
- **March:** move up to 2×M inches, but may not shoot or charge this turn
- **Charge:** declare a charge against a target in sight and within charge range (see *Charging* below)
- **Rally:** forgo movement entirely, roll D3 and remove that much stress. Requires a living Leader or nearby General; cannot be used in combat (unless within General's Inspiring Presence) or while Broken (see §5)

**The board edge.** The battlefield edge bounds all voluntary movement — no model may voluntarily move off the board; moves are limited accordingly. Involuntary movement interacts with the edge per its own rule: fall-back is blocked by the edge (§4 *Losing Combat — Fall Back*), while a Broken flee carries models off it to their destruction (§5 *State Effects*).

**Per-model movement.** Movement within a unit is conceptually per-model — each model has a movement allowance equal to the unit's M. For playability, Formed units moving as a block are measured as one (individual-model paths are implied, not traced). Only in Loose state, or during a state transition, do models move fully independently.

**Individual model pivoting.** A model may change its facing only at the **end** of its move — never mid-move. A pivot is the last thing a model does in its activation; having pivoted, the model cannot then continue moving. Additionally, a model cannot pivot if it is in base contact with another model at the end of its move — there is no physical room to rotate. This applies whether the contacting model is friendly or enemy.

#### Engaging the Enemy — the Charge Is the Only Door

A charge is the only voluntary way to enter melee. A unit making any voluntary non-charge move (Advance, March, wheel, pivot, or any other movement its controller chooses) may not end that move with any enemy model within melee weapon reach — in either direction: it may neither place its own weapons in reach of an enemy model nor end inside an enemy model's reach. If a planned move would violate this, it must stop short.

Exceptions:

- **Broken enemies** may be engaged by simply moving into weapon reach — no charge declaration needed (per §5 *State Effects*).
- **Pursuit** (§4) may carry the pursuer back into reach of the disengager — re-engagement, not a charge.
- **Involuntary movement** (charge-induced displacement, flee moves, spell-forced relocation) may create reach contact. The units are simply engaged from that point, with no charge bonuses, Impact attacks, or Stand and Shoot for either side.

This is why the charge apparatus matters: Stand and Shoot, charge stress, +1 Initiative, and Impact all hang off the declaration. Walking quietly into a fight is not an option for a disciplined battle line — or anyone else.

**Movement within an engagement.** The prohibition governs *creating* engagements, not moving within one. A unit that is already engaged may use its Normal Movement activation freely: it may disengage (per §4 — provoking Free Strikes as it leaves reach), reposition, or move *deeper* — closing from inside the enemy's reach until the enemy is inside its own. Closing is ordinary movement, not a charge: no charge bonuses, no Impact, no Stand and Shoot. The move may not, however, create a new engagement with a further enemy unit — that still requires a charge. An outranged unit caught at a reach weapon's standoff distance therefore has its answer on its own activation: walk onto the pikes, or walk away.

### Coherency

Every multi-model unit must maintain **coherency** — each model within a specified distance of at least one other model in the same unit. Coherency is continuously checked; a unit that fails coherency at the end of its activation must rectify on its next activation (see *Involuntary Splits and Reformation* below for how this interacts with mid-combat disruption).

**Default coherency: 1".** Specific units modify this via special rules:

- **Tight Formation**: coherency 0.5" — disciplined drilled infantry, shield-wall style
- **Skirmishers**: coherency 2" — loose order, dispersed skirmish line
- **Dispersed**: coherency 3" — very spread-out types; some cavalry, hunters, pickets

A unit cannot voluntarily split. Specific units may have special rules permitting detachment (*Splinter* and similar), but absent such a rule, the unit is always a single coherency blob — though the blob may take any shape the player wishes (line, cluster, ring, crescent) provided coherency is maintained throughout.

#### Enemy-Blocked Coherency

> An enemy model whose melee weapon reach covers models from the same unit on opposite sides of a physical split acts as a **coherency bridge**. The two groups are treated as coherent while the enemy threatens both.

"Threat range" is the enemy's longest melee reach, measured from its base; arc restrictions (e.g., tail-only attacks) are ignored for this check — what matters is the weapon's raw reach. The bridge applies only while the enemy continues to threaten both sides. If the enemy moves, dies, or otherwise ceases to threaten one side, the bridge ends — and the groups must satisfy normal coherency on their own.

Multiple enemies may chain bridges: the unit is coherent if every group connects to every other group through some alternation of friendly-coherency links and enemy bridges.

#### Friendly Unit Separation

> At the end of any activation, no model in a unit may be within the **larger of the two units' coherency values** of a model from a different friendly unit.

Two default-coherency infantry units stay ≥ 1" apart. A Saurus block (1") near a Skink skirmish screen (2") must keep ≥ 2" separation — skirmishers' looser spacing becomes a natural "personal bubble" that line units don't penetrate.

Units **may interpenetrate during movement** — models may pass through each other en route — but must end the activation respecting separation. This preserves useful movement (passing allies through allies) without allowing end-state intermingling.

The rule buys table clarity: shooting targets are unambiguous, coherency checks are simple, and unit membership is always visible. The cost is that layered "reserves behind the line" formations require real gaps — no stacking units tightly in depth.

#### Character Attachment Exception

A **single-model character** (not a monster) with the same **LiS value** as a friendly unit may stand within that unit's coherency — exempt from the friendly-unit separation rule with respect to that unit. LiS match is **exact**: a LiS 1 character fits with LiS 1 units only; a LiS 2 character (mounted cavalry hero) fits with LiS 2 units only. Monsters (LiS 4+) never qualify.

While attached:

- The character remains its **own unit mechanically** — separate activation, shooting, combat, stress, wound tracking. The attachment is positional, not mechanical integration.
- The character **cannot be singled out as a target** by enemy shooting attacks, hostile magic, or **charge declarations**. Ranged and magical attacks must target the unit the character is within; resolving those attacks affects the unit's models, not the character. Chargers must declare against the host unit — though the character may still be struck in melee by enemy models within reach of it (attachment shields targeting, not combat). Specific weapon, spell, or ability rules may override this — **Sniper** (§8) explicitly bypasses the protection, and character-targeting spells do the same where their text says so.
- The character may cast, shoot, or otherwise act from within the unit, subject to normal engagement rules (no shooting if in melee reach of an enemy).
- Attachment/detachment happens freely during the character's own activation — no declaration, just position. Moving out of coherency ends the exception.

### Involuntary Splits and Reformation

A unit may be **involuntarily split** — carved into groups by an enemy model (typically a monster carving the middle of a line, leaving survivors on either side of its base) during combat or any other event removing models from its interior. The *Enemy-Blocked Coherency* rule keeps the split unit coherent while the enemy continues to threaten both sides.

**While the unit remains in combat** (any model in melee reach of any enemy): the unit may operate in its split configuration. No forced reformation. The split is an accepted consequence of combat.

**When the unit is no longer in combat** (no model within melee reach of any enemy): on the unit's next Normal Movement activation (§7.2b), every model must take the shortest available path toward the nearest friendly model in the unit — moving up to M, with reformation as the priority. The unit may not take other movement actions until coherency is restored under its own rule (no longer relying on enemy-bridge).

**Abandonment** (escape valve): during the unit's activation in the Normal Movement sub-phase, the controlling player may declare any contiguous group of models in the unit as **lost**. Those models are removed as casualties — counting toward the 25% stress threshold and any effects that care about unit losses. The remaining models continue as the surviving unit, free of further reformation obligation.

Abandonment is a hard choice: you write off part of your unit as gone (fled, cut off, presumed destroyed) to free the rest to do something useful. Reserved for when reformation would consume so many turns that the unit is effectively removed from play anyway.

### Unit Identification

Both players must be able to tell every unit apart at all times. The friendly-unit separation rule prevents units from intermingling, which handles most of the identification problem — one cluster is visibly one unit.

The remaining case is **two units of identical models** (e.g., two Saurus Warriors blocks). For these, at least one **distinguishing element** is required:

- A visually distinct champion, standard, or musician
- A coloured base rim or marker
- A unit movement tray
- A written deployment record referenced in disputes

The controlling player is the authority on which of their models belongs to which unit. If clarity cannot be established in a dispute, the players should reset affected models to the last clearly-identified positions and replay from there.

### Formed, Loose, and Disordered

A unit is always in one of three states: **Formed**, **Loose**, or **Disordered**. The state is determined by the unit's arrangement on the table, not by declaration. If the arrangement satisfies the requirements for Formed, the unit is Formed; if it satisfies the requirements for Loose, the unit is Loose. A unit that satisfies neither is Disordered and receives no formation benefits of any kind.

> **Square bases are required** for this ruleset. Facing and formation rules depend on each model having a clearly identifiable front edge, two flanks, and a rear.

#### Requirements for Formed

A unit is Formed if **both** of the following are true:

1. Every model in the unit is in base contact with at least two other models in the same unit
2. Every model in the unit is oriented in the same direction

This rules out shapes that shouldn't count as formation:

- A single-rank line fails (end models have only one contact)
- A dispersed skirmish line fails (no base contact)
- Any cluster at least two models deep passes
- A ring passes — though a ring has no natural frontage (see *Front, Flank, and Rear* below)

> Other unit types — including Monstrous Infantry — may Form if the conditions are satisfied. A 3-model Monstrous Infantry unit arranged in a triangle passes the 2-contact test, though the formation is naturally fragile and a single casualty breaks it.

#### Requirements for Loose

A unit is Loose if **both** of the following are true:

1. No model in the unit is in base contact with any other model in the same unit
2. Every model in the unit is within coherency distance of at least one other model in the unit

A Loose unit is genuinely dispersed — models are spread across ground with clear gaps between them. A near-Formed cluster with a single straggler pulled out is not Loose; it is Disordered.

#### Disordered

A unit that satisfies neither the Formed nor the Loose requirements is **Disordered**. This is not a state a player chooses — it is the consequence of being caught between two disciplined arrangements. A Disordered unit receives no formation benefits whatsoever: no Formed bonuses, no Loose bonuses.

Disordered typically occurs during transitions (a Formed unit spreading out, a Loose unit bunching up), after casualties disrupt a formation, or when combat forces models into irregular positions. It is a temporary state that the unit should resolve on its next activation by committing to either Formed or Loose.

#### Front, Flank, and Rear

Because all models in a Formed unit face the same direction, the unit's facing is visible on the table — no token or declaration required. Arcs are read from each model's base:

| Arc | Cone | Role |
|-----|------|------|
| Front | 90° forward | Charge resistance applies; "frontal attack" |
| Flank (×2) | 90° each side | Defender loses charge resistance |
| Rear | 90° backward | Defender loses all Formed benefits |

**Single models** (monsters, characters) use their physical facing — the direction the miniature is pointed. **Multi-model Loose units have no facing of any kind.** All attacks against a multi-model Loose unit are resolved without directional modifiers.

> **Special Formations:** a unit with a specific special rule (e.g., *Circle of Defence*, *Hedgehog*, *Phalanx*) may adopt an alternate arrangement — typically models facing outward in all directions. Such formations alter or remove the standard front/flank/rear distinction and are described per-unit. For all other units, the standard arcs apply.

#### Wheeling

A Formed unit changes facing by **wheeling** — a rigid rotation of the entire cluster around a chosen pivot point (any model in the unit, typically a corner or the centre).

- All models are carried rigidly by the rotation; base contacts and relative positions are preserved
- Any angle is permitted (not restricted to 90° increments)
- **Cost:** the distance the outermost model travels along its arc, measured against the unit's movement allowance for the activation

Because rigid rotation preserves every model's position relative to every other model, base contacts stay intact and no overlap occurs — regardless of the angle chosen. Wide units wheel slowly; narrow units wheel cheaply.

A Loose unit does not wheel. Individual models are oriented during their own moves, subject to the pivot rule in *Base Movement* above.

#### Formed Benefits

While Formed, a unit gains the following:

| Benefit | Scope |
|---------|-------|
| **Disciplined Depth** — treat Resolve as +1 per full rank beyond the first, for all stress threshold purposes (Shaken, Wavering, Broken). Uncapped. | Non-directional |
| **Steady Ranks** — during the Combat phase, models killed in the engaged rank are immediately replaced from the rank behind, model-for-model, preserving the unit's engaged frontage and attack count for that round of combat. The replacement uses its own profile and Initiative; the dead model's strike does not transfer. Once no rear-rank models remain to fill, frontage shrinks naturally. | Combat phase only |
| **Charge Resistance** — enemies charging into this unit's front arc do not gain their +1 Initiative charge bonus. | Front arc only |
| **Shield Wall** — foot models in this unit equipped with a shield gain **+1 MD** against melee attacks resolved into the unit's front arc. | Front arc only; conditional on shield + foot |
| **Disciplined Volley** — the unit's Stand-and-Shoot reactions are made at the unit's full BS (no -1 BS penalty per §7). | Charge-reaction shooting only |
| **Command Eligibility** — only Formed units may benefit from `[Command]`-tagged abilities (external aura projections from generals, BSBs, and other authority sources). Unit-internal upgrades — Patrol Leader / Standard Bearer / Musician / Magic Standards borne by the unit's own model — are not `[Command]` and apply to the unit regardless of formation state. See §8 for the keyword definition. | Always while Formed |

##### Counting ranks for Disciplined Depth

A **rank** is a transverse line of models, in base contact with the rank ahead, parallel to the unit's front edge. A rank is **full** if it contains 5 or more models, for unit sizes greater than 5; for unit sizes of 5 or fewer, every rank counts as full.

Disciplined Depth grants +1 Resolve per full rank beyond the first. A 5-wide × 2-deep block of 10 models counts 2 ranks → +1 Resolve. A 5-wide × 4-deep block of 20 → +3 Resolve. A 6-wide × 5-deep block of 30 → +4 Resolve. The bonus is **uncapped** — depth is a player choice that pays its costs elsewhere (lost frontage and attack count, wheeling cost, vulnerability to AoE damage and template weapons that hit dense formations harder).

Lost models reduce the rank count dynamically. A 5-deep block taking casualties down to 4 effective ranks loses one step of Resolve immediately; the depth bonus and the rank discipline decay together as the unit is ground down.

##### Directional erosion of Formed benefits

| Attack arc | Effect |
|------------|--------|
| **Front** | All Formed benefits apply in full. |
| **Flank** | Non-directional benefits retained: Disciplined Depth, Steady Ranks, Disciplined Volley, Command Eligibility. **Charge Resistance and Shield Wall do not apply** for attacks resolved into a flank arc. |
| **Rear** | All Formed benefits drop for that attack. The unit is treated as Disordered for the rear-arc attack only. |

The directional logic is consistent: front-arc benefits assume the unit is *facing the threat* (locked shields, levelled spears, braced footing). Flank attacks bypass the shielded face but the rank-and-file behind is still cohesive. Rear attacks dissolve all formation discipline — the unit is reacting blind, models turning into the strike from a stable footing they no longer have.

#### Loose Benefits

While Loose, a unit gains the following:

| Benefit | Effect |
|---------|--------|
| **Extended Charge** — charge range is **M + 2D6 inches** (vs M + D6 for Formed). | — |
| **Irregular Movement** — the unit ignores the movement penalty for difficult terrain. | — |
| **Dispersed** — enemies suffer **-1 to hit** this unit with ranged attacks. Models with **LiS 4 or higher** do not benefit from Dispersed (too large for spacing alone to make them harder targets). | — |
| **No Facing** — a multi-model Loose unit has no front, flanks, or rear. All attacks against it are resolved without directional modifiers, and it cannot be flanked or struck-from-the-rear in any sense that would normally erode benefits. | — |

*Sustained-pace mobility (a baseline Movement bonus) lives on the Skirmisher unit-class rule rather than on the Loose state itself — see §8. Generic Loose-state benefits are about charge bursts, terrain freedom, and dispersion, not raw speed; Skirmisher specialists are the units that earn the speed bump as their identity.*

#### Why each state — at a glance

> **Formed = pressure-resistance, depth-discipline, command-integration.** Stress spine that grows with depth. Charge denial at the front. Shielded mutual support. Replaceable casualties. Volleyed fire. Commanded and signalled by the chain of authority.
>
> **Loose = burst speed, evasion, independent operation.** Faster charges, terrain freedom, harder to shoot, no flanks to exploit. The cost: no command structure reaches a Loose unit; it fights as it finds. Sustained-pace mobility belongs to Skirmisher specialists, not to the Loose state itself.

The two states model two genuinely different battlefield roles. A unit choosing Formed is **committing to the line** — accepting movement constraints and command dependence in exchange for depth-discipline and shielded mutual support. A unit choosing Loose is **operating independently** — gaining speed and evasion but losing the buff economy of the regimental drum.

#### Single-Model Units

A single-model unit counts as Loose. It cannot satisfy the requirements for Formed (no other models to contact) and by definition satisfies the requirements for Loose (no model in base contact with another model in the unit). A single model uses its physical facing — the direction the miniature is pointed — for determining shooting arcs and charge arcs against it.

#### State Transitions

A unit's state is determined continuously by its arrangement. A change between states is not a declared action but a consequence of how the models end their movement. Because the requirements for Formed and Loose are mutually exclusive (base contact vs no base contact), a unit transitioning between the two will pass through Disordered — there is no way to flicker directly from one to the other.

**Leaving Formed.** If during movement the models lose base contact or break the shared-facing requirement, the unit becomes Disordered immediately. If models continue spreading until no model is in base contact with another (while maintaining coherency), the unit becomes Loose. This may be deliberate (the player disperses the cluster) or involuntary (casualties scatter the formation, a push-back forces separation). A unit that becomes Disordered or Loose mid-activation uses that status for any subsequent attacks, tests, or calculations.

**Leaving Loose.** If any models move into base contact with another model in the unit, the unit becomes Disordered. It does not become Formed until all models satisfy the 2-contact and shared-facing requirements.

**Entering Formed.** A unit re-forms by ending its activation with all models in the 2-contact cluster and sharing a single facing. No declared "reform" action is needed — the cluster either satisfies the conditions at the end of movement or it does not.

**Entering Loose.** A unit enters Loose by ending its activation with no model in base contact with any other model in the unit, while all models remain within coherency.

**The consequence of pivot-at-end-of-move.** Because individual models may only pivot at the end of their move, a unit that breaks formation to reorient its models cannot then re-form within the same activation — the models have already used their movement. Re-forming with a new facing therefore requires a subsequent activation. Achieving significant reorientation in a single turn requires wheeling, whose cost at large angles may exceed the movement allowance. A disciplined formation cannot spin to face a new threat on a whim.

### Charging

#### Declaring a Charge

A unit may declare a charge during its activation against any enemy unit in sight and within its **maximum possible charge range** — the declaration is legal if a maximum roll could cover the required path:

- **Formed chargers:** M + D6 inches (declaration legal within M + 6)
- **Loose chargers:** M + 2D6 inches (declaration legal within M + 12)

The charge distance is then rolled (full sequence in §7.2a). The charger moves along its path and must end within weapon reach of a target model. **If the required path exceeds the rolled distance, the charge fails: the unit must advance up to its normal M along the declared charge path toward the target, halting outside mutual melee reach** — it may neither reach the enemy nor end inside the enemy's reach; the surge pulls up short. Momentum is committed: a failed charge leaves the unit stranded in front of the enemy, and it may not move again this turn (per §7.2b).

A unit that charged this turn gains **+1 Initiative** for its first round of attacks. (A Formed defender charged into its front arc denies this bonus — see *Charge Resistance*.)

#### Charge Arcs

The arc of a charge — front, flank, or rear — is determined by the **charger's position at the moment of charge declaration**, before any charge movement is made. The path of the charge does not change the arc.

- If the majority of the charger's models fall within the defender's front arc: frontal charge
- If the majority fall within a flank arc: flank charge
- If the majority fall within the rear arc: rear charge
- If exactly split between arcs, the defender chooses which arc applies

> This means a fast unit starting in the defender's front cannot simply outrun the facing to hit the flank. Flank attacks must be set up through prior manoeuvre — deployment, advance, or a pivot forced on the defender.

#### Charge-Induced Displacement of Friendlies

If a successful charge's contact position would put the charger within friendly-unit separation of another friendly unit, that friendly unit is **displaced backward** by the minimum distance required to restore separation.

- The displacement is a rigid translation of the whole friendly unit. Formed state is preserved if the translation preserves the 2-contact cluster (which it does for small displacements).
- **Geometric feasibility:** the charger's base must fit in its contact position. If the space is physically blocked — wedged between terrain, enemies, or walls — the charge fails regardless of displacement math.
- **Cascading:** if displacing Unit A would violate separation with Unit B, Unit B is also displaced, and so on. Tight formations can produce chains of ripple-back.
- **Nowhere to displace:** if any unit in the cascade cannot find legal space (blocked by board edge, impassable terrain, or an enemy unit), the charge must pick a different contact angle within its 45° wheel allowance. If no valid angle exists, the charge fails entirely.

Packing units tightly in depth becomes a real liability under this rule: a single enemy charge can ripple displacement backward through your own formations.

#### Wheeling During the Charge

A charger may adjust its direction of travel by up to 45° during the charge path to find a good angle of contact or avoid terrain. Charge distance is measured along the wheel path. Wheeling does not change the charge arc.

---

## 6.5. Terrain

> **Design pillar (per Design Goals #2):** terrain matters. Battles are won and lost by how units exploit, avoid, or defend the features on the table. The keyword library below is the canonical set this ruleset references; themed terrain features (Mystical Wood, Damned Altar, etc.) are deferred to faction-specific or scenario-specific extensions and may layer additional rules on top of these baselines.

Each terrain feature on the table is **tagged with one or more terrain keywords** before deployment. Players agree on the tags during setup — the AoS-style "place the terrain, then talk through what each piece is" convention. Keywords compose; their effects stack independently. A forested hill is **Forest + Hill**; a low stone wall on a forested hill is **Walls + Forest + Hill**.

Themed terrain features may add unique rules on top of the keyword baseline (e.g., a Sigmarite Shrine might be Walls + Hard Cover + an Inspiring Presence (6") aura), but the baseline keyword behaviour always applies underneath.

### 6.5.1. Terrain Categories

#### Open Ground

The default. No keyword needed; everything outside other terrain features is Open Ground.

- **Movement.** No restriction; full M.
- **LOS.** Unobstructed.
- **Combat.** No modifier.

#### Difficult Terrain

Rough, uneven, slippery, or dense ground that slows movement — scree slopes, marshland, dense undergrowth, ruined floors, broken paving.

- **Movement.** While **moving through** Difficult Terrain (any model in the unit is on the feature during movement), the unit moves at **half speed** — half M for Advance, half pace for fall-back / pursuit. The penalty applies along the path-segment that crosses the terrain only; portions of the move on Open Ground use full M.
- **Charge interaction.** **A unit cannot Charge through or into Difficult Terrain.** A charge whose path or contact position would cross or end inside Difficult Terrain is illegal — the charger must redirect around (subject to the 45° wheel allowance per §6) or abort. Chargers already inside Difficult Terrain (e.g., a unit declared a charge from within a wood) are unrestricted; the prohibition is on *entering* the terrain at charging speed.
- **Formation.** No formation penalty. A Formed unit moving through Difficult Terrain stays Formed; the terrain slows movement but doesn't break cohesion. (Loose units already suffer no terrain-derived penalties; this restates that the formation-axis is unaffected for Formed too.)
- **LOS / Combat.** No inherent modifier; specific terrain types layered on top (Forest, Marsh) may add LOS / combat effects.
- **Bypassed by:** Fly (passes over and may charge over), Strider (Difficult) (no penalty at all, and may charge through).

#### Dangerous Terrain

A terrain feature with the **Dangerous Terrain** keyword imposes a per-model risk on units that move recklessly through it.

When any model in a unit **Marches into** or **Charges through** a Dangerous Terrain feature, that model must immediately take a **Dangerous Terrain Test**:

1. Roll a **D6**
2. On a **1**, the model takes **1 wound** with **no saves allowed** (no Armour, no Ward, no Regeneration). The wound is environmental damage — sharpened stakes, lava bursts, collapsing scree, caltrops — not a weapon or magical attack, and no defensive layer applies
3. On a **2-6**, the model is unhurt

Each model in the unit tests independently. A 10-model unit charging through stakes makes 10 tests (each a 1-in-6 chance for that model to take a wound), averaging ~1.7 wounds across the unit.

**Trigger granularity.** The test fires once per model per crossing. A unit that Marches into and out of the feature in a single move tests each model once. A unit that ends a March on the feature tests on entry; if it later leaves the feature on a subsequent movement, it tests again. **Advance** moves do NOT trigger Dangerous Terrain — the unit is moving carefully and avoids the hazards. Only **March** and **Charge** actions trigger the test (the unit is moving recklessly, fast enough to crash into stakes / step on caltrops / fall into pits).

**Damage profile.** Default Dangerous Terrain inflicts **1 wound on a roll of 1** with no save. Specific terrain types may override the threshold (e.g., a particularly hazardous lava field might wound on a roll of 1-2; a mild caltrop field might wound on a roll of 1 only on March, not on Charge). Default applies when no override is specified.

**Bypassed by:**
- **Fly** (per §8) — flying movement passes over the ground feature entirely; no Dangerous Terrain test triggered
- **Strider (X)** keyword where X matches the terrain type (e.g., **Strider (Stakes)**, **Strider (Lava)**, **Strider (Forest)**) — models with the matching Strider keyword skip the test for that terrain type
- Specific exemptions on individual unit profiles

**Common applications:**
- **Defensive Stakes** (Bretonnian Longbowmen, §17) — peasant levies plant stakes at deployment; the staked band is Dangerous Terrain (Stakes type)
- Future applications: trap-pits, caltrops, lava streams, sharpened spike-fields, magically-summoned hostile terrain, spell-summoned environmental hazards

#### Impassable Terrain

Sheer cliffs, deep crevasses, lava pools, magic-warded zones, walls of stone — features that physically cannot be crossed by ground units.

- **Movement.** Cannot be entered. Models must move around. A unit whose required path runs through Impassable Terrain must wheel or redirect.
- **Charge interaction.** A charge whose path is blocked by Impassable Terrain must reroute around (subject to the 45° wheel allowance per §6) or fails.
- **LOS.** Typically blocks LOS; specific features may allow see-over only for units physically taller than the feature.
- **Bypassed by:** Fly (passes over).

#### Forest / Woods

Dense canopy, trees, undergrowth.

- **Keywords applied:** Forest = **Difficult Terrain** + LOS-blocking (see §6.5.2 Line of Sight below).
- **Movement.** Half M (inherits from Difficult Terrain). Cannot be charged into from outside (inherits from Difficult Terrain) — combined with the LOS rule that outside cannot see inside, a unit fully in a wood is genuinely safe from charge declaration until the attacker enters the wood by Advance or March.
- **Formation.** No formation penalty (inherits from Difficult Terrain). Formed units cross / fight in woods at full formation cohesion.
- **LOS.** A model **inside** a wood can see only models within **6"** through the foliage. **Models outside the wood cannot see any model inside the wood** — the canopy and undergrowth fully obscure the interior. A unit fully inside a wood is invisible to outside shooters; a unit straddling the wood's edge has its outside-the-wood models targetable as normal, but its inside-the-wood models cannot be seen or targeted from outside. Charges between outside and inside still need a target visible at the charge declaration; a unit fully inside a wood cannot be declared as a charge target by a unit outside (cf. the Charge prohibition for Difficult Terrain below).
- **Combat.** No melee modifier; the wood's tactical impact is movement and LOS, not melee mechanics.
- **Bypassed by:** Strider (Forest), Forest Stride *(Wood Elf, per §1.5)* — full Open Ground treatment, no Difficult, no Disordered, full M, no LOS-into-self penalty for Wood Elves themselves.

#### Hill / High Ground

Elevated ground — a hill, a rocky outcrop, a mound, a flat-topped plateau.

- **Movement.** No inherent penalty. The slopes do not slow movement at this scale of abstraction. (A Hill keyword can be combined with Difficult Terrain for genuinely steep / rocky climbs — e.g., a "Crag" feature would be Hill + Difficult.)
- **LOS — atop the hill.** A model on a Hill **sees over** intervening Soft Cover and same-elevation Hard Cover that is below the Hill's top — line-of-sight extends past obstructions a same-level shooter would be blocked by. The viewer must still have a physical eye-line to the target; Hill elevation does not grant X-ray through Forest interiors or through Hard Cover features at the same elevation as the Hill itself.
- **LOS — behind the hill.** A unit **fully behind a Hill** from a shooter's angle is in **Hard Cover** against shooters at the same elevation or lower. The hill body itself is the obstruction. (Shooters atop a higher hill or on a flying mount looking down do not get the cover effect — they see clearly over.)
- **Combat — defending the high ground.** A unit **defending a Hill against a charge from below** (the charger ascends the slope into combat) gains **+1 to its MD in the round of the charge only**, *provided the defender's LiS is greater than or equal to the charger's LiS*. The high-ground advantage represents the defender getting to swing down at a lower-profile attacker; a tall charger (Cavalry charging Skinks on a low rise; a Carnosaur charging Saurus on a hilltop) towers over the elevation and gains nothing for the defender to push back against. The bonus does not apply if both units are on the Hill, if the defender charged off the Hill into combat, or in subsequent rounds of melee.
- **Bypassed by:** N/A — Hill confers benefit, doesn't penalise.

#### Water

Streams, ponds, rivers, marsh, swampland.

- **Keywords applied:** features tagged simply *Water* default to **Difficult Terrain**. **Shallow Water** (an explicit keyword) is Open Ground for movement. **Deep Water** (an explicit keyword) is Impassable for non-Aquatic, non-Fly ground units. Players agree at setup which tag applies per feature.
- **Movement.** Per applied keyword. Default Water = half M.
- **LOS.** No effect by default.
- **Combat.** No modifier.
- **Bypassed by:** **Aquatic** *(per §8)* — no penalty for any Water feature, including Deep Water (the unit swims, wades, or is amphibious by biology); **Fly** — passes over.

#### Walls / Barriers

Linear obstacles — stone walls, hedgerows, low fences, ruined sections, barricades. Distinct from Buildings (below), which are enclosed structures.

- **Movement.** Crossing a wall consumes an extra **2"** of movement beyond the model's normal step — climbing, scrambling over, or pushing through the obstacle. A model that ends its move atop a wall remains there. Charges whose path crosses a wall pay the 2" penalty along their charge distance; if the charge's measured distance is insufficient after the climbing cost, the charge fails.
- **LOS.** **Hard Cover** — blocks LOS for any unit fully behind the wall from the shooter's angle (see §7.4 for the 50% threshold and stacking rules).
- **Combat — defending across a wall.** A **Formed** unit with at least one model in **base contact with the wall along its front edge** gains **+1 to MD against melee attacks coming from the wall's far side, in the same arc**. The wall absorbs blows aimed at the defender, and the defender strikes from a stable position over the rampart. The bonus persists across multiple rounds (unlike the Hill bonus, which is charge-round-only) — the wall doesn't go anywhere. **Stacks with Shield Wall.** Loose units do not gain the wall defender bonus (their dispersed posture doesn't anchor against the obstacle).
- **Heavy fortifications.** Castle perimeters, garrisoned keeps, full city walls — these go beyond standalone Walls and are governed by **Buildings** rules below.
- **Bypassed by:** Fly (passes over).

#### Buildings

A garrisonable structure — ruined houses, defensive towers, chapels, fortified inns, walled compounds. Usable in scenarios that explicitly permit garrisoning.

- **Keywords applied:** Buildings = Impassable to non-garrisoning movement + Hard Cover for garrisoned units + +1 MD for garrisoned units in melee.
- **Garrisoning.** An **Infantry** unit may garrison a building it has at least one model in base contact with at the start of its activation. Garrison capacity per the building's profile (default: **10 models** for a small structure, **20 models** for a larger one). Non-Infantry unit types (Cavalry, Monstrous Infantry, Monsters, etc.) cannot garrison — buildings are scaled for foot-soldier occupancy.
- **Garrisoned formation.** A garrisoned unit is treated as **Formed** for all purposes regardless of physical model arrangement. The structure imposes its own coherency.
- **Garrisoned defence.** The unit gains **Hard Cover** against ranged attacks and **+1 MD** in melee against attackers outside the building. A garrisoned unit's models cannot be individually targeted; wound allocation follows §4 *Wound Allocation* (front-rank-equivalent first).
- **Shooting from a building.** Models may shoot from the building, with all eligible models treated as if in clear LOS to front and flanks (the windows and arrow-slits abstract away). Rear-arc shots are blocked unless the building's profile states otherwise.
- **Charges into a garrisoned building.** Chargers declare a building face being attacked; combat is resolved through that breach. Only models within reach of the breach contribute attacks each round. Multiple chargers on different faces resolve as separate combats.
- **Losing combat / Breaking inside a building.** A garrisoned unit that loses a combat does **not** fall back and takes no blocked-path stress — standard combat-loss stress only. The walls make retreat unnecessary, and the winner gains no Follow up. A garrisoned unit that becomes **Broken** abandons the building: place it outside, in contact with the building face furthest from the enemy it is fleeing, then resolve its flee moves normally from there.
- **Specific buildings** may carry additional keywords (Sacred, Cursed, Magical, Inspiring) per scenario or faction rules.
- **Bypassed by:** Fly (passes over the structure body but does not bypass the garrisoned defenders inside if charging in).

### 6.5.2. Line of Sight

The ruleset uses **true line of sight** — a viewer can target what its model can physically see, eye-line to model. Model pose, base position, and intervening terrain all matter.

#### Tall-unit visibility convention

To prevent endless model-pose disputes over whether a specific cavalryman is or isn't visible behind a hedge, certain unit types are **always considered visible over Soft Cover and over low walls** (waist-high or shorter), regardless of model-pose specifics. The convention:

- **Tall-unit types** *(Cavalry, Monstrous Infantry, Monstrous Cavalry, Chariot, Monster, and Warbeast variants larger than a Skink-base)* — visible over Soft Cover and over low walls. Hard Cover (full-height walls, building corners), Forest interiors, and Impassable Terrain still block.
- **Small-unit types** *(Infantry W 1–2, Swarm, Skink-base Warbeasts)* — true LOS only. A skink ducked behind a hedge is genuinely invisible; a ratman swarm in undergrowth is genuinely lost in the brush.

The convention prevents tall units from being "hidden" by terrain features they physically tower over, while preserving the small-unit identity-axis advantage for skirmishers, swarms, and ground-hugging W 1 troops. The 50% obscuration rule for **cover qualification** (per §7.4) is independent — a tall unit visible over a hedge can still be **in cover** for cover-modifier purposes if the hedge obscures 50% of its visible models from the shooter's angle.

#### Elevation and seeing over cover

A model on **Hill / High Ground** sees over intervening obstacles that would block a same-level model. The elevation extends LOS forward over Soft Cover and over walls *that are below the Hill's top*. The viewer must still have a physical eye-line to the target; Hill elevation doesn't grant X-ray vision through Hard Cover or Forest interiors at the same elevation as the Hill itself.

A model on a wall top, building roof, or other elevated platform (occupying the elevated position, not standing behind it at ground level) sees out at the elevated position's height — the same Elevated-LOS convention as Hill.

#### Cross-reference to §7.4 Cover

§7.4 Cover applies the **to-hit modifiers** (-1 Soft Cover / -2 Hard Cover) when LOS is partially obscured by terrain at or below the shooter's level. The 50% obscuration threshold for "the unit is in cover" applies as drafted in §7.4.

### 6.5.3. Special-Rule Cross-References

Existing §8 special rules and §1.5 species traits that interact with terrain:

- **Fly (X)** — flying movement passes over all ground terrain; ignores Difficult, Dangerous, Impassable, and Water keywords for movement purposes. Does not bypass LOS-blocking effects (a flyer behind a Forest is still in cover).
- **Strider (X)** — ignores **Difficult Terrain** and **Dangerous Terrain** effects of the named type, *and* may charge through that terrain (the terrain's no-charge-into prohibition is bypassed for Strider holders). *X* matches a terrain keyword: Strider (Forest) ignores Forest's half-movement, no-charge-into, and 6"-LOS-into-self effects; Strider (Stakes) ignores Defensive Stakes' Dangerous Terrain test.
- **Aquatic** — ignores all Water terrain penalties, including Deep Water's Impassable effect. May charge through any Water feature.
- **Skirmishers** — Loose formation; full mobility through woods, marsh, etc. Half-movement through Difficult Terrain still applies (skirmishers aren't immune to rough ground), but combined with Loose's burst-speed identity and the +1 M baseline (per §8), Skirmishers are the natural-fit unit type for terrain-heavy battlefields. Per §8 Skirmishers, individual Skirmisher unit profiles may specify Strider effects on top.
- **Forest Stride** *(Wood Elf, per §1.5)* — treats Forest terrain as Open Ground; no half-movement penalty inside woods, no charge-into prohibition (Wood Elves may charge through and into woods at full distance), no LOS-into-self penalty (Wood Elves inside woods see normally), no Dangerous-Terrain test for thorn-fields / dense undergrowth. The forest doesn't impede the forest-folk. Note: Forest Stride is a unilateral Wood Elf benefit; enemies attempting to charge a Wood Elf unit defending inside a wood are still blocked by the default Forest no-charge-into rule. The Asrai keep their forest sanctuary.

These rules now key off the §6.5 terrain keyword library directly. `Strider (Forest)` matches a feature with the **Forest** keyword; `Strider (Lava)` would match a feature tagged **Dangerous Terrain (Lava)** for that specific application.

---
