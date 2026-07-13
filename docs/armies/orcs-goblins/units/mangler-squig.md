# Mangler Squig

> Two Great Cave Squigs chained together, goaded into mutual fury by a Night Goblin handler trying his hardest to die last. "Night Goblins, speculated to be driven mad by their subterranean lifestyle, exhibit a reckless mentality through the creation of Mangler Squigs. They capture Great Cave Squigs, chain two together, and incite them to attack enemy lines. This dangerous practice often results in uncontrollable chaos and gore, which the Night Goblins relish, despite the high risk of bloody accidents." The ideal end result, "from the Night Goblins' perspective, is that the Mangler Squigs enrage each other, whirling themselves into a tumbling motion. The beast builds a wild, unstoppable momentum of pure aggression, swirling chain and snapping jaws." Drafted here as a **chaotic mid-Monster Rare** for Greenskin / Night Goblin armies — the Mangler Squig has *no tactical control whatsoever* (Random Movement in a randomly-rolled direction; Force of Total Destruction crushes anything in its path including friendly units), explosive death (Ker-splat!), and a high probability of killing more of the Greenskin player's own troops than the enemy's. The lore signature is twofold: **Force of Total Destruction** *(every model the Squig moves over takes D3 hits at S 5 — anti-everything-in-path damage, friend or foe)* and **Ker-splat!** *(when killed, the chained Squigs explode in a 3" radius — death-rattle that hits everyone nearby, again friend or foe)*. Fills the pending Mangler Squig flag in the Greenskin FACTION.md "Greenskin-allied biology" listing. The Greenskin battlefield read: deploy the Mangler Squig at the front line, point it roughly toward the enemy, and accept that it might immediately roll backward into your own Boyz before exploding. The cost of admission for fielding chaos.

## Profile

| M | MA | MD | BS | S | T | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|----|-----|----|
| **Random** *(3D6")* | 4 | 3 | 0 | 5 | 4 | 8 | 4 | 5 | 3 | =W |

**Points:** 118 per model *(framework derivation under §13: stat-baseline 14.0 + rules 8.0 + equipment 5.0 = 27.0 raw × wound factor 5.48 (W 8) × 0.8 scaling = 118.4 → 118. **Pass 2 (2026-05-18):** W 6 → W 8 (+2 W for durability — the Squig isn't a one-turn glass cannon); **Out of Control mechanic restructured** — the Greenskin player now *chooses the direction* (no random scatter / D8); only the *distance* (3D6") remains random. The Squig still hits everything in its path (Force of Total Destruction) and can still roll past intended targets due to the random distance, but the Greenskin player can at least *aim* the chaos and avoid deliberately rolling over friendly units. Net +49 pts from Pass 1's +69. See `design.md` for full working)*

**Unit size:** 1

**Unit type:** Monster (single model — two chained Squigs + Goblin handler resolved as a single combined chaos-vehicle)

**Natural Armour:** 6+ (Squig hide — light biological armour; the Mangler Squig isn't tough, it's *fast and chaotic*)

**Base Size:** 50mm × 50mm (medium round base — two big Squigs chained together makes a substantial but not huge footprint)

**Keywords:** Greenskin, Night Goblin, Squig, Monster, Rare

## Equipment

- **Equipment:** Chained Squigs (the two Great Cave Squigs themselves — bound together, snapping at everything) + Goblin Handler (lore-only — provides direction-attempts, no separate combat profile; the Goblin dies with the Squigs on Ker-splat!). No worn armour, no shield.

## Special Rules

- **Random Movement (3D6")** *(per §8)* — The Mangler Squig moves at a chaotic 3D6 inches each Movement phase. Range 3-18", mean 10.5". **Cannot March.** The Random Movement *is* the Squig's full movement and *also* its charge range when it charges.

- **Out of Control** *(Mangler Squig unit identity rule — Pass 2: direction chosen, distance random)* — At the start of each Movement phase:
  1. **The controlling player chooses a direction** for the Mangler Squig (any direction the player wants — toward the enemy, around a flank, into a specific unit, etc.). The Goblin handler is *trying* to steer; this is the direction he's pointing.
  2. **Roll 3D6"** for the distance (range 3-18", mean 10.5"). The Squig will roll *that exact distance* in the chosen direction.
  3. The Mangler Squig moves in the chosen direction by the rolled distance, *in a straight line*, ignoring formations and intervening models per §8 rules. **Cannot stop voluntarily.**
  4. If the Mangler Squig's rolled distance carries it off the table edge, it is **removed from play**. No Ker-splat! trigger — the Squig is just gone.
  5. If the Mangler Squig moves into impassable terrain (a wall, a cliff, a building it can't fit through), it **immediately triggers Ker-splat!** at that location.

  **Tactical implications:**
  - **Direction is in the player's control** — the Greenskin player can aim the Squig away from friendly units, toward enemy formations, around terrain, etc. The Squig is no longer a self-destructive friendly-fire grenade.
  - **Distance is unpredictable** — the player picks the direction but doesn't know if the Squig will roll 3" or 18" in that direction. Risk of *overshooting* (rolling past intended target into open ground or off the table) or *undershooting* (rolling short of the enemy line).
  - **Friendly-fire risk persists** but is now *controllable* — the player won't direct the Squig through friendly units unless choosing to do so. Mistakes happen on long-distance rolls that overshoot intended targets.

  **Lore-direct:** "Out of Control" — the Goblin handler can *point* the Squigs in a general direction, but the rolling momentum is unpredictable. The Squigs go where the chains take them; the handler's "control" is purely advisory.

- **Force of Total Destruction** *(Mangler Squig unit identity rule — move-over damage)* — As the Mangler Squig moves during its Random Movement, **every model whose base is crossed by the Squig's path** (friend or foe — the rule is utterly indiscriminate) takes **1 hit at S 5 / AP -1 / D 1**. Hits are automatic (no to-Hit roll). Standard wound allocation applies; armour saves and Ward saves apply per standard.

  **Multi-unit hits:** if the Mangler Squig's path crosses multiple units, *each model in each unit* takes 1 hit. A particularly lucky (or unlucky) Mangler Squig roll can hit 8-15 models in a single Movement phase.

  **Friendly fire:** explicitly applies to *friendly Greenskin models* in the Squig's path. The Greenskin player must deploy carefully — placing the Mangler Squig in front of friendly units risks friendly-fire damage on its first chaotic move.

  **Lore-direct:** "The beast builds a wild, unstoppable momentum of pure aggression, swirling chain and snapping jaws." Everything in the path gets bitten / chained / crushed indiscriminately.

- **Immune to Psychology** *(per §8)* — The Mangler Squig is too maddened with bloodlust to register external Psychology effects (Fear, Terror, friendly-unit-destroyed-stress). The Goblin handler is too busy not-dying to notice morale shifts. Note: the Squig is NOT Imm Psych for its *own* effects — the Out of Control random direction is intrinsic biology, not Psychology, so it applies regardless.

- **Ker-splat!** *(Mangler Squig unit identity rule — explosive death-rattle)* — When this model is reduced to 0 W *or* when forced into impassable terrain by Out of Control, **immediately before removing the model**, the Mangler Squig explodes. **Every model within 3" of the Squig's last position** (friend or foe) takes **1 hit at S 5 / AP -1 / D 1**. Hits are automatic; standard wound allocation applies. The chained Squigs, the Goblin handler, and the iron chains all fly outward in a final burst of gore.

  **Tactical implication:** when the Mangler Squig is at low W, the opposing player must consider that killing it triggers a 3" explosion — sometimes worth the trade (kill the Squig, accept the explosion damage), sometimes not (let the Squig roll past and explode later in a less-relevant area).

## Weapon Profiles

### Close Combat

- **Snapping Jaws** *(natural — the chained Cave Squigs' bites)* — **1" reach** | **A 3** | **S 5** | **AP -1** | **D 1** — used only when the Mangler Squig stops in base contact with an enemy unit (rare — the Squig usually rolls *past* enemies via Force of Total Destruction rather than stopping in melee). Three snapping bites at modest S 5 / AP -1. If the Squig somehow ends a Movement phase in melee combat (e.g., charges and stops in base contact, or is charged itself), this is its profile. Most of the Squig's combat output lives in Force of Total Destruction, not Snapping Jaws. `[Natural]`
