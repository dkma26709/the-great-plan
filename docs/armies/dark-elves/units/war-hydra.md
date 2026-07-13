# War Hydra

> Titanic multi-headed serpent of the Blackspine Mountains, bred and enchanted in vast dungeons beneath the cities of Naggaroth. The War Hydra "regenerates damage at a frightening rate" — only severing every head in quick succession kills the beast, "and if even a single one remains, the remainder will swiftly grow back and devour the impudent attacker." Druchii Beastmasters tend the Hydras from hatching, casting enchantments upon the eggs "to raise the ferocity of successive generations to new heights." The handler bond is fraught — "a Beastmaster must be quick with his lash lest he be devoured in the enemy's stead" — but the result is the apex non-character Druchii Monster: a beast that **belches smoke and fire**, **rends men with sharp fangs**, and tears its way into the enemy line. The mechanical translation favours the *model* over some of the lore exaggeration: the Hydra is **serpentine and snake-bodied** — sinuous more than armoured-fortress, low to the ground rather than upright-tower. Scales protect (NA 5+) but the bulk of survival comes from regeneration, not from being unhittable. **Multi-Headed Regrowth** is the lore signature: wounds dealt to the Hydra trigger end-of-phase healing rolls, and unlike standard Regeneration, fire does *not* stem the regrowth — only outpace it. **Many Heads** (the degrading damage table) captures the mid-fight head-severing: at full Wounds the Hydra strikes with all five heads; as Wounds are lost the heads diminish, until the crippled beast is down to two functional jaws but still snapping. **Fiery Breath** is the cone-attack signature, igniting whole regiments at close range. The Hydra is fielded here as a **pure Monster** (single profile, no on-table Beastmasters) — the handler bond is implicit, the Beastmaster off-stage representation deferred to a future Druchii Hero draft. The Naggarothi battlefield read: send the Hydra forward, breathe fire into the line, then let the heads tear apart whatever survives.

## Profile

| M | MA | MD | BS | S | T | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|----|-----|----|
| 5 | 4 | 3 | 0 | 5 | 6 | 10 | 3 | 6 | 4 | =W |

**Points:** 294 per model *(framework derivation under §13: stat-baseline 18.5 + rules ~7.5 + equipment ~18.9 = 44.9 raw × wound factor 8.20 (W 10) × 0.8 scaling = 294.5 → 294; the per-extra-A pricing for the Heads-and-Jaws uses lifespan-average A 5.5 rather than full-strength A 10, because the Many Heads mechanic ties A directly to current W and the unit spends most of its game-time at sub-full A. See `design.md` for full working)*

**Unit size:** 1

**Unit type:** Monster (single model, no rider, no on-table Handler)

**Natural Armour:** 5+ (serpentine-scaled hide — armoured against glancing blows, but the bulk of the Hydra's survival comes from regeneration rather than from being impenetrable)

**Base Size:** 100mm × 75mm

**Keywords:** Druchii, Dark Elf, Monster, Rare

## Equipment

- **Equipment:** Heads-and-Jaws (natural multi-head bite) + Fiery Breath (natural breath weapon). No worn armour, no shield, no rider.

## Special Rules

- **Terror** *(Psychology — see §8)* — at LiS 4, the Terror aura projects to **(6 + 4)" = 10"**. A titanic multi-headed reptile that belches fire and regenerates damage registers as terror on any battlefield — the lore-canonical "horror as the beast emerges unscathed from the carnage, vents forth an ear-splitting roar."
- **Multi-Headed Regrowth** *(War Hydra unit identity rule, custom Regeneration variant)* — Whenever this model loses 1 or more Wounds in a phase (from any source — melee, ranged, magic, template, breath, anything), roll **one D6 per Wound lost** at the *end of that phase*. For each result of **4 or higher**, immediately heal **1 Wound** (capped at the Hydra's starting W of 8). The Hydra's many heads regrow with frightening speed — sever one and another rises in its place. **Unlike standard Regeneration** (per §8), this rule is **not negated by Flaming attacks** — even fire cannot stem the regrowth, only outpace it; the heads grow back through cauterised stumps. **Damage table interaction:** Wounds are applied first (potentially reducing the Hydra into a lower damage tier mid-phase), then Regrowth rolls at end of phase (potentially restoring the Hydra back into a higher tier). The damage table state is re-checked after Regrowth resolves.
- **Many Heads** *(War Hydra unit identity rule)* — this model's Heads-and-Jaws **Attacks equal its current Wounds remaining**. At full Wounds (W 10), the Hydra strikes with A 10 — every functional head snapping at the foe in a single combat round. As Wounds are lost the heads diminish one-for-one, and at W 1 the Hydra has only a single functional head left. **The Hydra's threat scales directly with its biological state**: devastating at full health, manageable at low health, fluctuating in between as Multi-Headed Regrowth restores heads between phases. Damage taken in a phase potentially reduces A for return-strikes within that phase; end-of-phase Regrowth potentially restores A for subsequent phases. **A is recomputed dynamically** — there is no fixed damage-table; the rule is "look at the Hydra's current W and that's its A." Lore-direct expression of the multi-head mechanic: every head matters.

## Weapon Profiles

### Close Combat

- **Heads-and-Jaws** *(natural, multi-head — A = current W per Many Heads)* — **3" reach** | **A = current Wounds remaining** (up to A 10 at full Wounds) | **S 5** | **AP -1** | **D 1** | **Poisoned Attacks** (per §8) — multiple serpentine heads striking together on long necks. **3" reach** reflects the Hydra's exceptional reach — the long necks strike past front rank, over walls, around corners; only a few weapons in the codebase match this. **S 5 / AP -1** captures sharp fangs rending — strong enough to wound T 4 on 3+, T 5 on 4+; AP -1 cuts through light armour but not full plate. **Poisoned Attacks (+1 to-Wound)** captures the venomous bite of the multi-head serpent — every head carries the same Hydra-blood toxin (lore-myth: the classical Hydra's blood is poisonous; the Druchii breeding programmes enhance this property). The variable A (1-10) is the *Many Heads* mechanic above; at full Wounds the Hydra strikes a flurry of ten venomous bites, devastating against any target whose T is wound-able at S 5 + Poisoned. `[Natural]`

### Ranged

- **Fiery Breath** *(natural Breath Weapon)* — **Flame Template** | **S 5** | **AP -1** | **D 1** | **Flaming** | **Slow to Fire** | **Scatter (Artillery Die)** — the iconic Hydra signature, "belches smoke and fire." The Flame Template covers a cone projected from the model's front arc (per §7.4 templates). **Flaming** triggers the standard interactions (negates Regen on targets, Flame-panic on US 2+ beast units — though the Hydra is itself US =W = 8, so its own attacks are immune to the Flame-panic effect by the "any Flaming weapon in profile" clause per §8). **Slow to Fire** means the Breath cannot be used as a Stand-and-Shoot reaction to enemy charges. **Scatter Artillery Die** models the imprecision of belching flame at range — a single Hydra is not a sniper. Useful against tight formations and especially against Flammable / Forest-Spirit / wooden-bodied enemies. `[Breath Weapon]`
