# Trolls

> Greenskin-allied biology — large humanoid creatures of Chaos-tainted origin, **about the size of an Ogre**: M 6 / T 4 / W 7 / S 5 / Stupid / Regen. Trolls are recruited into Waaagh!s through the simplest transaction in Greenskin society: the Warboss promises food (Men, Dwarfs, mounts), and the Trolls march to where the food is. Each Troll regenerates damage at a frightening rate — "severed limbs and heads simply regrow from the stumps, and even the most grievous damage can be regenerated within a day" — and "fire is the only known weakness" to this regeneration. Trolls fight with **fists and maw** as their primary weapons; the iconic *acid-vomit* attack belongs to **River Trolls** (a future sub-variant), not to Common Trolls. The brute also has the option to wield a massive **club, mattock, or other Great Weapon**, trading some of its multi-attack output for devastating single strikes — but the heavy weapon slows the already-dim Troll to a crawl (**-2 Initiative when used**). **Stupidity** is the unavoidable tax: Trolls are dim, easily distracted, and slow to react. **Promised Feeding** is the iconic mitigation — a friendly Greenskin character within 6" provides the imperative direction the Troll lacks, and the unit ignores Stupidity for that turn. Without character supervision, the Troll lumbers forward toward the nearest enemy regardless of tactical sense — sometimes useful, often catastrophic. The lore-explicit *Trolls-as-Greenskin-allies* framing: not Orcs, not Goblins, but recruited into the faction list via the **Animosity** trait and the food-bond with Greenskin characters.

## Profile

| M | MA | MD | BS | S | T | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|----|-----|----|
| 6 | 4 | 2 | 0 | 5 | 4 | 7 | 2 | 5 | 2 | 3 |

**Points:** 65 per model *(framework derivation under §13: stat-baseline 11.75 + rules ~4.0 + equipment ~3.0 = 18.75 raw × wound factor 4.36 (W 7) × 0.8 scaling = 65.4 → 65; see `design.md` for full working)*

**Unit size:** 3+

**Unit type:** Monstrous Infantry

**Natural Armour:** 5+ (tough Troll hide — augmented by the constant regrowth scarring)

**Base Size:** 40mm × 40mm

**Keywords:** Greenskin, Troll, Monstrous Infantry, Rare

## Equipment

- **Equipment (default):** Hands and Maw (natural melee). No worn equipment, no armour beyond Troll hide.

## Special Rules

- **Animosity** *(Greenskin-wide faction trait — see §8 Psychology)*. D6 at start of each Movement phase when out of combat; on a 1, sub-roll D6 determines whether the unit charges nearest enemy or takes D3 self-hits at S 5. *(Trolls' Animosity-manifestation is "distracted-driven" — the dim brutes forget what they were doing or pick fights with each other over the last piece of food.)*
- **Stupidity** *(Psychology — see §8)*. The Troll is slow-witted, easily distracted, and not bright enough to follow complex orders. At the start of the unit's activation in the Movement phase, it must Charge / Advance toward nearest enemy / Advance aimlessly per §8. Cannot March, cannot Rally unless required. *(Mitigated by Promised Feeding — see below.)*
- **Regeneration (4+)** *(Defence — see §8)*. 4+ Ward Save against unsaved wounds, representing the Troll's frightening regenerative biology. **Negated by Flaming attacks** — fire is the only known weakness to Troll regrowth (a wound from a Flaming attack skips the Regeneration save entirely; other ward sources still apply). Stacks with other ward sources under standard Ward Save Stacking rules.
- **Fear** *(Psychology — see §8)*. At LiS 2, the Fear aura projects to **(6 + 2)" = 8"**. A pack of Ogre-sized humanoid creatures that regenerate damage and vomit acid registers as terror on any battlefield.
- **Promised Feeding** *(Troll unit identity rule — Stupidity mitigation)* — if any friendly model with the **Greenskin Character** keyword is within **6"** of any model in this unit at the start of the Movement phase, this unit **ignores Stupidity this turn**. *Lore-true:* Greenskin tribes recruit Trolls "by promising opportunities to feed on Men, Dwarfs, and mounts." A Warboss, Big Boss, or Shaman within shouting distance provides the imperative direction the Troll lacks; when isolated, the Troll's biology reverts to dim wandering. Satisfies the §8 Stupidity *mitigation condition* design requirement. *(Note: Promised Feeding does not suppress Animosity — even with a character nearby, the Troll still rolls Animosity, since Animosity is faction-wide-trigger rather than intelligence-driven.)*

## Options

**Equipment swap option (replaces Hands and Maw, pick at most one):**
- **Great Weapon** (+2 pts/model) — replaces the default Hands and Maw profile. The Troll's hands now wield a massive club, mattock, ship's anchor, uprooted tree, or other heavy improvised weapon. The brute hits **harder per swing** but **slower overall** — full profile in Weapon Profiles below.

**No worn armour options.** Trolls do not wear armour; Troll hide + Regeneration is their entire defence.

**No command options.** The Troll pack is a dim brute squad — no Boss, no Standard, no Musician. Command direction comes from the off-stage Greenskin character via Promised Feeding.

*(Future expansion: Stone Troll variant — NA 4+ + Magic Resistance; River Troll variant — Aquatic + Strider Water + Acidic Vomit ranged; Chaos Troll variant — Mark of Chaos options, Chaos-faction-aligned. Held for future Troll-variant drafts.)*

## Weapon Profiles

### Close Combat

- **Hands and Maw** *(natural, default)* — 1" reach | **A 3** | S 5 | AP 0 | D 1 — fists pound, maw bites. Three swings per Troll per round reflects the multi-limb thrashing style — Trolls don't strike with skill but they strike often. **S 5** is the Troll's biological strength (Ogre-tier brawn). **AP 0** captures the unfocused fist-and-bite (no edge, no point) — Trolls don't pierce armour, they batter it. Combined with the multiple swings, per-round damage output is consistent against light-armoured infantry but blunted against heavy armour. `[Natural]`

- **Great Weapon** *(option, 2H — replaces Hands and Maw)* — 1" reach | **A 2** | S+2 (= S 7) | AP -2 | D 1 | Two-Handed | **-2 Initiative when used** — heavy improvised weapon (huge club, mattock, ship's anchor, uprooted tree). Trades one of the Troll's multi-attack swings for crushing single-strike power. **S 7** wounds T 4 on 2+ and T 5 on 3+; **AP -2** strips light and medium armour. The downside is severe: **-2 I** brings the Troll's effective Initiative to **0** when swinging the Great Weapon — the brute strikes after nearly everything in the game, taking return-fire first. **Most charging enemies will hit the Troll before the Troll swings.** The Great Weapon is the right choice when the Troll *expects to outlast* the incoming attacks (via Regen + W 7) and wants to deliver a decisive cleave; the default fists are better when the Troll needs to strike quickly or against numerous low-T targets. `[2H]`
