# Orcs & Goblins


> The Greenskin race. Fungal-born, perpetually itching for a fight, individualistic to the point of self-destructive squabbling. Where Asur are *disciplined-skill*, Druchii are *frenzied-lethal*, and Lizardmen are *bred-warrior-cult*, the Greenskins are **love-the-fight-but-don't-listen**. Every Greenskin unit's tactical contribution is genuine but unreliable: the army that *gets* into combat thrives there; the army that needs to *manoeuvre* before combat suffers from Animosity squabbling and Undisciplined recovery floors. The faction's defining tension is between the *brawl-power* it brings to the table and the *positional unreliability* it accepts as the cost.

## Status

**Currently classed as §18 Cross-Faction Reference** — two representative units drafted at present (Orc Boyz Core + Forest Goblin Arachnarok Spider Rare Monster), with full-faction promotion deferred until the roster is broader. This document is the design reference for future Greenskin unit drafts: it captures the philosophy, sub-tribe axes, and constraints that should hold across the faction so each unit's design loop starts from a shared baseline.

**Drafted units:** [Orc Boyz](units/orc-boyz.md), [Big 'Un Orc Boyz](units/big-un-orc-boyz.md), [Savage Orc Boyz](units/savage-orc-boyz.md), [Common Goblins](units/common-goblins.md), [Common Goblin Archers](units/common-goblin-archers.md), [Night Goblins](units/night-goblins.md), [Goblin Wolf Riders](units/goblin-wolf-riders.md), [Forest Goblin Spider Riders](units/forest-goblin-spider-riders.md), [Squig Hoppers](units/squig-hoppers.md), [Squig Herd](units/squig-herd.md), [Goblin Spear Chukka](units/goblin-spear-chukka.md), [Orc Boar Chariot](units/orc-boar-chariot.md), [Goblin Wolf Chariot](units/goblin-wolf-chariot.md), [Snotling Pump Wagon](units/snotling-pump-wagon.md), [Forest Goblin Arachnarok Spider](units/forest-goblin-arachnarok-spider.md), [Trolls](units/trolls.md), [Stone Trolls](units/stone-trolls.md), [River Trolls](units/river-trolls.md), [Black Orcs](units/black-orcs.md), [Orc Boar Boyz](units/orc-boar-boyz.md), [Savage Orc Boar Boyz](units/savage-orc-boar-boyz.md), [Wyvern](units/wyvern.md), [Giant](units/giant.md), [Mangler Squig](units/mangler-squig.md).

## Cultural axis — three sub-species, one faction

Within the Greenskin race, three biologically distinct sub-species share the faction list and Animosity but differ on almost every other axis:

| Sub-species | Cultural identity | Combat axis | Morale floor | Faction-wide trait |
|---|---|---|---|---|
| **Orcs** | Brawl-from-the-front, large brutish warriors, fungal-pain-tolerant | **MA > MD asymmetric** (swing hard, get hit hard) | Res 7 baseline (love fighting, lack discipline) | **Animosity** + **Loves a Scrap** + Undisciplined (except Black Orcs) |
| **Goblins** | Cowardly skulkers, stab-from-behind, swarm-volume | **MA < MD** (bad at fair fights, slippery to pin) | Res 5-6 baseline (cowardice is the species fingerprint) | **Animosity** + **Undisciplined** + **No Loves a Scrap** |
| **Snotlings** | Mushroom-creatures, swarm-fodder, half-Goblin intelligence | Negligible combat | Res 4 (swarm-tier, no individual morale) | **Animosity** + Swarm-type |

The **MA / MD asymmetry inverts** across the sub-species: Orcs lean attacker (MA > MD), Goblins lean evader (MA < MD). This is the cleanest mechanical expression of "Orcs love a fight, Goblins do not."

Within the Orc sub-species, four cult-equivalent tiers exist (parallels Asur cult-tiers but on the brawl axis):

| Orc tier | MA / MD | W / Save | Morale trait | Identity | Example unit |
|---|---|---|---|---|---|
| **Common (Boyz)** | 4 / 3 | 2 / light armour cap | **Undisciplined** | Brawl-from-the-front rank-and-file | Orc Boyz *(drafted, 9 pts)* |
| **Big 'Uns** | 4 / 3 | **3** / medium armour cap, S 5 | Undisciplined | Elite Boyz survivors, +1 A always-on | Pending |
| **Black Orcs** | 5 / 4 | **3** / **heavy armour, Disciplined + Stubborn-leaning** | **Disciplined** *(the only Orc exception)* | Disciplined-elite, heavy-armour, two-weapon kit | Pending — the natural Asur Swordmasters / Druchii Executioners counterpart |
| **Savage Orcs** | 4 / 3 | 2 / **no armour, Frenzy + Ward 6+ war-paint** | Undisciplined + Frenzy | Frenzied glass-cannon Orcs (parallel to Witch Elves' frenzied-cult) | Pending |

Within the Goblin sub-species, three sub-tribes exist (regional / cultural differentiation rather than tier-ladder):

| Goblin sub-tribe | Distinguishing toolkit | Magical access | Example unit |
|---|---|---|---|
| **Common** | Open-plain skulkers, bows / slings / spears | Waaagh! Magic ("Big Waaagh!") | Pending |
| **Night** | Subterranean fungus-eaters, **Fanatics** (suicide weapons), Squig Hoppers, darkness-affinity | Night Goblin Shaman ("Little Waaagh!" — mushroom-induced) | Pending |
| **Forest** | Spider-cult, **Wall-crawler** mounts, Poisoned Attacks pervasive | Spider God lore (pending §11 draft) | Forest Goblin Arachnarok Spider *(drafted, 325 pts)* |

## Stat patterns

**Orc baseline** (per §13):

| M | MA | MD | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 4 | 4 | 3 | 3 | 4 | 4 | 2 | 2 | 1 | 7 | — |

**Goblin baseline** (per §13):

| M | MA | MD | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 4 | 2 | 3 | 3 | 3 | 3 | 1 | 3 | 1 | 5 | — |

**Cross-faction Res convention (deliberately NOT applied to Greenskins).** Empire / Bretonnia / Asur / Druchii / Dwarfs receive a +1 Res over the WAP baseline (the "disciplined-faction" convention reflecting cross-faction calibration of the stress-system). **Greenskins do not get this bump** — Orc Res 7 and Goblin Res 5-6 stay at the WAP baseline. Greenskins love combat but aren't drilled to a stoic morale standard; the cross-faction convention is for *disciplined* factions specifically, not for any-faction-with-elite-tier. Lore-true: an Orc unit panics if pushed beyond its Loves-a-Scrap stress relief; a Goblin unit panics readily. This is the species fingerprint and is preserved across all Greenskin units.

**Stat ladder for Greenskin units** (drafted or expected):

| Tier | Indicative M | MA | MD | S | T | W | I | Res | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Snotling Swarm** | 4 | 2 | 2 | 2 | 2 | =W | 3 | 4 | Swarm-tier, no individual morale |
| **Common Goblins (Core)** | 5 | 2 | 3 | 3 | 3 | 1 | 3 | 5 | Common Goblins *(drafted, 4 pts — M 5 species-wide call vs 8e M 4 canon for skulker identity, Stab in the Back +1 to Wound vs rear/Shaken/Wavering, Cowardly Numbers Stubborn-while-20+ / -1 Res below half, No Loves a Scrap)*; Common Goblin Archers *(drafted, 5 pts Shortbow default / 4 pts Sling swap — Stab in the Back applies to ranged attacks, Shortbow profile established as first in ruleset 18" S 3 AP 0)* |
| **Night Goblins (Core)** | 5 | 2 | 3 | 3 | 3 | 1 | 3 | 5 | Night Goblins *(drafted, 4 pts + 0-3 Fanatics @ +20 pts each — Mushroom Madness Animosity sub-table replaces standard; Fanatic mini-unit M 2D6\" / W 1 / S 5 AP -2 D 2 D6 auto-hits per pass / artillery die for direction / removed on 2D6 doubles; single entry with HW / Spear / Shortbow / Sling loadout options)* |
| **Common Orcs (Core)** | 4 | 4 | 3 | 4 | 4 | 2 | 2 | 7 | Orc Boyz *(drafted, 9 pts)* |
| **Big 'Uns** | 4 | 4 | 3 | 4 | 4 | 3 | 2 | 7 | Big 'Un Orc Boyz *(drafted, 14 pts — S 4 unchanged from Boyz per cross-faction ladder coherence with Black Orcs S 4 / Saurus S 4; W 3, +1 A always-on stacks with Loves a Scrap, Medium armour cap, full Boyz weapon kit, unit size 10+)* |
| **Black Orcs (disciplined-cult elite)** | 4 | 5 | 4 | 4 | 4 | 3 | 3 | 8 | Black Orcs *(drafted, 29 pts — only Disciplined Orc; Stubborn + Quell Animosity 6" aura + Armed to da Teef per-Combat-phase weapon switch across Choppa+Shield / Pair of Choppas / Great Weapon)* |
| **Savage Orcs (frenzied)** | 4 | 4 | 3 | 4 | 4 | 2 | 2 | 7 | Savage Orc Boyz *(drafted, 11 pts — stat baseline identical to Common Boyz; differentiation via intrinsic Frenzy (F4 fingerprint) + War-Paint Ward 6+ always-on + locked no-armour/no-shield. Same weapon kit as Boyz reflavoured. Witch Elves cross-faction parallel at the frenzied-glass-cannon design axis.)* |
| **Goblin / Orc Cavalry** | 7-9 (mount) | 4 / 2 | 3 | 4 / 3 | 4 / 3 | 2 / 1 | 2-4 | 7 / 5 | Orc Boar Boyz *(drafted, 15 pts — Orc-on-War-Boar, Tusker Charge Impact D3 at S+1 AP-1, mount NA 6+ tough hide)*; Savage Orc Boar Boyz *(drafted, 15 pts — Savage Orc on War Boar, Frenzied glass-cannon variant of Orc Boar Boyz: intrinsic Frenzy + War-Paint Ward 6+ + locked-no-rider-armour + Tusker Charge Impact inherited)*; Goblin Wolf Riders *(drafted, 8 pts — Common Goblin on Giant Wolf, Fast Cavalry, mount M 9 / S 3 / no NA)*; Forest Goblin Spider Riders *(drafted, 10 pts — Forest Goblin on Giant Spider, Fast Cavalry + Wall-crawler (promoted to §8) + Poisoned Attacks unit-wide, mount M 7 / S 3 / T 3 / NA 6+ chitin / Spider Bite A 2 multi-leg-and-fang weapon profile; Stab-in-the-Back + Poisoned stacks for +2 to Wound vs Wavering targets)*; Squig Hoppers *(drafted, 13 pts — Night Goblin on Cave Squig, Random Movement 3D6\" replacing M, Massive Mouth A 2 S 5 mount bite, no Fast Cav)* |
| **Troll (Monstrous Infantry)** | 6 | 4 | 2 | 5 | 4 | 7 | 2 | 5 | Trolls *(drafted, 65 pts — Ogre-sized biology, Stupid with Promised Feeding mitigation + Regen 4+ Flame-negated + Fear; optional Great Weapon at -2 I)* |
| **Giant (Monster)** | 6 | 3 | 1 | 7 | 5 | 6-8 | 1 | 6 | Pending — drunken / unstable apex |
| **Arachnarok (Forest Goblin Monster)** | 8 | 4 | 4 | 5 | 6 | 18 | 4 | 7 | *Drafted, 325 pts* — Mixed Unit with Crew |
| **Orc Shaman / Goblin Shaman (Hero caster)** | — | 4 / 3 | 3 | 4 / 3 | 4 / 3 | 2 / 1 | 2-3 | 7-8 | Pending — Waaagh! Magic |
| **Orc Warboss (Lord)** | — | 6 | 5 | 5 | 4 | 4 | 3 | 8 | Pending |

## Biological constraints

Hard cultural / biological ceilings that apply across the faction:

- **No Natural Armour at rank-and-file** — Orc and Goblin biology relies on worn armour and shields; the fungal-tinged hide is tough enough for W 2 / T 4 (Orcs) but doesn't provide NA. Trolls (Monstrous Infantry-tier) and Squigs (Beast-tier) have inherent armour-equivalents via biology, but those are Greenskin-allied not Orc/Goblin baseline.
- **I capped low** — Orc I 2 baseline, Goblin I 3, Snotling I 3. The Greenskin biological fingerprint is *swing hard but slow* (Orcs) or *slippery-but-not-fast* (Goblins). Apex Greenskin characters reach I 3-4 max; never apex-Initiative.
- **No species-wide morale-aura abilities** — Greenskins are individualistic; no "Inspiring Presence" baseline. Characters provide command at their own auras but the species doesn't project regiment-cohesion bonuses.
- **Magic surfaces only at the Shaman tier** — no rank-and-file Greenskin caster biology. Orc Shamans, Goblin Shamans, Night Goblin Shamans, Forest Goblin Shamans (Spider God) — all Hero/Lord tier characters.
- **Heavy armour reserved for elite tier** — Common Orcs cap at light armour + shield. Black Orcs are the exception (heavy armour standard).
- **Greenskin morale floor: Animosity always rolls.** Even Disciplined Black Orcs roll Animosity (lore: a Black Orc squabble is "Get on with it!" rather than "I'm bored of waiting" — different manifestation, same trigger).

## Faction-wide rules

All Greenskin units carry at minimum:

- **Animosity** (per §8 *Command and Coordination*) — at the start of each Movement phase, roll D6 for the unit *if not currently in melee*. On a **1**, sub-roll D6: 1-3 forces a charge against nearest visible enemy (fallback to self-hits if no target); 4-6 the unit takes D3 hits at S 4 as Greenskins turn on each other. The iconic Greenskin unpredictability tax — roughly 1-in-6 per unit per turn loses positional control or absorbs self-inflicted casualties.

**Orcs additionally carry** (per §8 *Resolve and Command*):

- **Loves a Scrap** — at the end of each Combat phase the unit was engaged in melee, the unit removes 1 stress. AND if the unit was engaged in melee combat at the end of the previous turn, it gains +1 Attack on a single weapon profile this turn (per the +1-attack convention). The momentum of the brawl carries forward.

**Goblins explicitly do NOT inherit Loves a Scrap.** Goblins do not enjoy combat — brawling drains them, doesn't refresh them. The faction-wide Greenskin trait does not apply at the Goblin sub-species level. This is the cleanest mechanical expression of "Orcs love a fight, Goblins do not."

**Default Greenskin recovery trait — Undisciplined** (-1 to Recovery rolls). Applies to rank-and-file Orcs, all Goblins, Snotlings. **Black Orcs are the only Orc exception — they carry Disciplined instead** (the cult of Gork-and-Mork drill-warriors).

## Sub-tribe scaling rules

When scaling Greenskin units above the rank-and-file baseline, the design ladder by sub-tribe is:

**Orcs (Common → Big'Un → Black → Savage):**
1. **Big 'Uns** — W 2 → W 3, S 4 → S 5, +1 A always-on (no need for Loves a Scrap momentum to trigger). Same MA/MD asymmetry, same Undisciplined.
2. **Black Orcs** — the **disciplined-cult-elite branch**. MA 4 → 5, MD 3 → 4, W 2 → 3, heavy armour standard, **Disciplined** (only Orc unit to break the Undisciplined faction-wide), often Stubborn or carrying anti-stress mechanics. Two-weapon kit (great weapon + paired choppas) common. The cross-faction parallel: Asur Swordmasters (disciplined-cult skill), Druchii Executioners (disciplined-cult lethality), Black Orcs (disciplined-cult brutality).
3. **Savage Orcs** — the **frenzied-cult branch**. W 2 unchanged, but no armour, **Frenzy** intrinsic, **Ward 6+ war-paint** (defensive war-paint magic — biological-ritual rather than item-based). Cross-faction parallel: Witch Elves' frenzied-Khainite glass-cannon profile.

**Goblins (Common → Night → Forest):**
1. **Common Goblins** — baseline rank-and-file. MA 2 / MD 3, Res 5-6, light armour cap, shortbow / sling / spear / shield.
2. **Night Goblins** — sub-tribe, not a tier-up. W 1 still, but **Fanatics** (chained-mushroom-dosed suicide weapons, released before contact) + Squig Hoppers (Squig-mounted Fast-Cavalry) + darkness-affinity (Cave Combat modifier per future §6.5 expansion). Mushroom-Frenzy variants at Hero tier.
3. **Forest Goblins** — sub-tribe, spider-cult. **Wall-crawler** mounts (Spider Riders / Arachnarok), **Poisoned Attacks pervasive** (spider-pit-venom from spider biology), Spider God magical lore (faction-flavoured Waaagh! Magic variant).

**Greenskin-allied biology** (different species, same faction list):

- **Trolls** *(drafted, 65 pts)* — Monstrous Infantry, Ogre-sized biology (M 6 / T 4 / W 7 / S 5 / I 2 / NA 5+). **Regen 4+** (Flame-negated, lore-true) + **Stupid** (mitigated by **Promised Feeding** — Greenskin character within 6" suppresses Stupid) + **Fear**. Hands-and-Maw default (A 3 / S 5 / AP 0); **Great Weapon option** at +2 pts (S+2 / AP -2 / -2 I when used). Sub-variants drafted: **Stone Trolls** *(80 pts — NA 4+ petrified hide + Magic Resistance (2) per §8)* and **River Trolls** *(80 pts — Aquatic + Strider (Water) + Acidic Vomit short-range natural ranged attack: 6" / A 1 / S 5 / AP -2 / D 1 / auto-hits despite BS 0, once per Shooting Phase per Troll)*. **Chaos Trolls deferred to the Warriors of Chaos faction list** (Mark of Chaos options fit the WoC roster more naturally than the Greenskins one).
- **Giants** — Monster-tier. **Drunken / Stubborn-leaning**, multiple chart-based attack profiles (throw, jump-up-and-down, swing-with-club), randomly-resolved attacks.
- **Squigs** — chaos-fungus creatures. Mangler Squigs (Monster), Squig Hoppers (Goblin-mounted Fast-Cavalry), Squig Herds (handler-driven swarm).
- **Snotlings** — Swarm-tier, board-presence not damage-dealers.
- **Wyverns** *(drafted, +84 pts mount-adder)* — apex Greenskin flying Lord-mount. Monster Mount profile (M 4 ground / Fly 8" / MA 4 / MD 3 / S 5 / T 5 / W 6 / I 4 / Res 7 / NA 5+). **Crash-Landing Feast** charge-only AoE (D3 free Bite attacks at S 5 AP -1 D 1 vs an enemy unit within 1" of charge target, before main charge resolves — captures "lands in the middle of an enemy unit and feasts upon their flesh" as a bystander-damage event). **Poisoned Tail Sting** weapon (3" reach, A 1, S 4, AP 0, Poisoned — strikes past front-rank into characters or high-T targets where Poisoned +1-to-Wound matters most). Pure Monster Mount profile; Lord rider is the Orc Warboss (pending) or Great Shaman (pending) draft. The iconic Greenskin Lord-on-Monster.
- **Boars** — Cavalry mounts for Orc Boar Boyz / Boar Boy Big 'Uns.
- **Wolves** — Common Goblin Wolf Riders' mount.

## Equipment patterns

- **Choppa** *(default Orc 1H weapon)* — heavy cleaver, AP -1 baseline. The iconic Greenskin weapon-identity vs generic hand weapon. Cleaver-weight bites through light armour.
- **Pair of Choppas** *(option)* — two cleavers, +1 A on the weapon profile, loses shield.
- **Spear** *(option)* — 2" reach, AP 0 (sideways trade vs Choppa's AP -1). No charge-defence bonus (Orcs are not drilled phalanx fighters).
- **Great Choppa** *(option)* — 2H, S+2 (= S 6 for Orc), AP -1 held (the Orc weapon ladder is "+S not +AP" past Choppa baseline). Carries a -1 Initiative penalty when used — heavy cleaver slows the swing.
- **Bows / Slings** *(Goblin baseline ranged)* — short-bow standard, sling cheaper alternative. Forest Goblins use Poisoned bows.
- **Shortbow** *(Forest Goblin / Common Goblin)* — light bow, low Strength, supplemented by Poisoned Attacks for Forest Goblins.
- **Heavy armour at Black Orc tier only.** Rank-and-file Orc Boyz cap at light armour + shield. Goblins cap at light armour. Savage Orcs use **no armour** (cultural).
- **War-paint (Savage Orcs)** — biological-ritual Ward 6+ in place of armour. Pending Savage Orc draft for full mechanic.
- **Fanatics (Night Goblin)** — chained suicide-weapons; pending Night Goblin draft.

## Magic

**Waaagh! Magic** (the lore of conflict and brute psychic-momentum) — channelled through Orc Shamans and Goblin Shamans. Pending §11 dedicated lore drafting, but the design hooks are:

- **Big Waaagh!** — the Orc / Common Goblin Shaman's tradition. Spells should emphasise *aggression amplification*, *attack-boost auras*, *enemy-disruption-via-momentum*. The Shamans do not *master* Waaagh-energy so much as *survive their attempts to channel it* — Orc Shamans risk their heads exploding if a cast goes wrong (Miscast-on-self mechanic per WAP convention).
- **Little Waaagh!** — Night Goblin Shaman variant, channelled via mushroom-induced visions. Characteristically chaotic; spells lean *unpredictable* / *random-target* / *self-affecting*.
- **Spider God lore** — Forest Goblin Shaman tradition (pending separate §11 draft). Venom-themed, web-attacks, swarm-summoning. Distinct from Big Waaagh! / Little Waaagh!.
- **Orc Great Shaman (Lord-tier caster)** — apex Greenskin spellcasting. Pending design.
- **Goblin Great Shaman (Lord-tier caster)** — Goblin caster apex. Pending.

## Mounts and monsters

- **War Boars** — Cavalry mount for Orc Boar Boyz / Boar Boy Big 'Uns. Aggressive, charging-focused; Boar Boyz get charge-impact bonuses per WAP.
- **Giant Wolves** — Common Goblin Wolf Rider mount. Fast Cavalry, harassment role.
- **Giant Spiders** — Forest Goblin Spider Rider mount (Cavalry-tier) and Arachnarok (apex Monster). Wall-crawler mount mechanic — terrain-immune.
- **Squigs** — Squig Hoppers (Goblin-mounted Fast-Cavalry-equivalent), Mangler Squigs (Monster-tier rolling suicide weapon), Squig Herds (handler-driven swarm).
- **Trolls** *(drafting next)* — Monstrous Infantry, fielded by both Orc and Goblin armies. Sub-variants by terrain (Common / Stone / River / Chaos).
- **Giants** *(drafted, 287 pts)* — Greenskin-allied super-apex Monster, drunken combat, chart-randomised attack profiles. W 12 / S 6 / T 5 biology *(W 12 reflects that "wounds is the Giant's defence" — no NA, low MD 2, raw mass is the survival layer)* with **dual-table Random Attack** (D6 each Combat phase, Small Enemies table for US ≤ 3 targets / Big Enemies table for US 4+ Monsters; six distinct results per table — Yell and Bawl / Pick Up and Eat or Grapple and Crush / Jump Up and Down / Swing With Club / Thump With Club / 'Eadbutt with next-round A-reduction debuff). Stupidity + Stubborn, Fall Over death-rattle. Cross-faction usable by Chaos (with future Mark-of-Chaos variants), Mercenary, and Dogs of War lists.
- **Wyverns** — apex Greenskin flying mount; Orc Warboss on Wyvern is the iconic Greenskin Lord-on-Monster.
- **Forest Goblin Arachnarok Spider** *(drafted)* — apex Forest Goblin Monster (W 18 Mixed Unit with Goblin Crew). Per Druchii War Hydra comparison: bigger absolute scale, different biology (chitin + venom vs serpentine + Regrowth).

## Pricing notes

**Pass 8 framework (0.8× scaling).** Greenskins re-derive under §13 with the global scaling factor. Sample anchor points:

- **Orc Boyz 9 pts/model** (drafted). Choppa AP -1, faction-wide Animosity + Loves a Scrap, MA 4 / S 4 / T 4 / W 2 / Res 7.
- **Forest Goblin Arachnarok Spider 325 pts/bundle** (drafted). Mixed Unit (Spider + 8 Crew). Apex Monster price.

**Expected Greenskin ladder for undrafted units:** Common Goblins ~4-6 / Night Goblins ~5-7 / Big 'Uns ~13-15 / Black Orcs ~18-22 / Savage Orcs ~10-12 / Boar Boyz ~14-16 / Wolf Riders ~7-10 / Trolls *(drafting — projected ~50-70 pts/model based on Monstrous-Infantry biology + Regen + Stupid)* / Giants ~250-300 / Mangler Squigs ~75-100 / Squig Hoppers ~12-15.

**Apply at draft:** trust the framework re-derivation. Greenskins' Animosity is a *negative-cost* rule (-1 raw); Loves a Scrap is *positive-cost* (~+3 raw); Undisciplined is *negative-cost* (-0.5 raw). The faction's pricing reflects the wash-and-spike rule density rather than apex stat stacks.

## Cross-faction comparators

Useful anchors when drafting a Greenskin unit:

| Comparator | Why it's useful |
|---|---|
| **Saurus Warriors (Lizardmen Core)** | The kin-comparator in the "tough biology" category. Both T 4 W 2-3; Saurus has Cold-Blooded + Disciplined + Stubborn + Predatory Fighter, Orcs have Animosity + Loves a Scrap + Undisciplined. Saurus 29 pts vs Orc Boyz 9 pts — the 20-pt gap reflects the Saurus's Pack Cohesion + 4+ combined save + better discipline / morale floor versus the Orc's lower cost-floor and chaotic-unreliability tax. |
| **Chaos Warriors (Mortal Chaos baseline)** | The "elite human-tier" comparator. Chaos Warriors 16 pts vs Orc Boyz 9 pts — same T 4 / W 2, Chaos wins on MA / MD / save / Will of Chaos; Orcs win on cheaper baseline + Loves a Scrap momentum +1 A. Black Orcs (pending, projected 18-22 pts) sit at Chaos Warrior tier — the disciplined-elite Greenskin parity. |
| **Bretonnian Men-at-Arms (peasant rank-and-file)** | The "cheap rank-and-file" comparator. Men-at-Arms ~5 pts vs Orc Boyz 9 pts — Orc Boyz nearly doubles the cost for +1 W, +1 MA, AP -1 weapon, Loves a Scrap. The Greenskin baseline is genuinely above peasant-tier human even before sub-tribe scaling. |
| **Witch Elves (Druchii frenzied-cult)** | The frenzied-glass-cannon comparator. Witch Elves 13 pts vs Savage Orcs (pending, projected 10-12) — same Frenzy-no-armour design pattern, but Witch Elves bring Murderous Prowess + Elven Grace + Poisoned + Hatred (HE) + Daughters of Khaine to compensate for biology fragility, where Savage Orcs bring Animosity + War-paint Ward 6+ + Loves a Scrap + Orc T 4 / W 2 brawl-power. Different routes to the same glass-cannon-attacker valence. |
| **Salamander (Lizardmen Mixed Unit beast)** | The "beast + handlers" comparator. Salamander 68 pts bundle vs the **Troll** projection (Monstrous Infantry, ~50-70 pts/model). Both have unusual biology in a normal-stat army; Salamander has a breath weapon, Troll has vomit + Regen. Different unit-types (Mixed Unit beast vs Monstrous Infantry) but adjacent design space. |

## Drafting hooks

Open Greenskin design questions, captured here for future unit passes:

- **Waaagh! Magic lore** — pending §11 lore-draft. Big Waaagh!, Little Waaagh!, Spider God variants. Should be drafted before Shaman characters.
- **Fanatics mechanic** — Night Goblins' iconic suicide-weapon. Pre-engagement release, random direction, S 5 + Multiple Wounds attacks. Held for Night Goblin draft.
- **Wall-crawler keyword** — Forest Goblin terrain mechanic. Currently exists on Arachnarok profile; needs §8 promotion when Spider Riders are drafted.
- **War-paint Ward 6+ (Savage Orcs)** — biological-ritual defence in place of armour. Mechanically a Ward Save tied to the unit (lost if certain conditions break, per WAP).
- **Stupidity (Trolls and other dim-witted Greenskin biology)** — §8 Stupidity rule exists in framework (-2.5 raw). Trolls draft will exercise it. Question for the draft: does Stupid suppress on proximity to characters (parallel to Cold One Knights' Stupid-suppression)?
- **Black Orc disciplined-elite identity** — needs careful design call. Black Orcs are *the only Disciplined Orc* — what's their unique mechanical identity beyond Disciplined? Multiple weapon-swap toolkit per WAP; or anti-Animosity-aura for nearby units; or both.
- **Wyvern-mounted Warboss** — Wyvern profile drafted ([Wyvern/profile.md](units/wyvern.md), +84 pts mount-adder). **Orc Warboss character** still pending — will pay the +84 adder for the Wyvern mount option.
- **Greenskin faction-promotion threshold** — currently §18 cross-faction reference with 3 drafted. Threshold to full §-numbered faction is roughly 8-10 units with full FoC coverage. Likely candidates for the next 5-6 unit drafts: Black Orcs, Night Goblins, Common Goblins, Big 'Uns, Wolf Riders, Orc Shaman.

- **Great Weapon Initiative-penalty principle** *(system-wide convention surfaced during the Troll draft — captured here as a drafting hook for future faction passes)* — most great weapons should carry an Initiative penalty (-1 I typically; -2 I for very heavy / clumsy variants like Troll Great Weapons) rather than being straight upgrades over the baseline weapon. Cult-trained / master-craft exceptions explicitly waive the penalty (Asur Swordmasters' Hoeth-Forged Greatsword via the Swordmasters identity rule; Chaos Warriors' Chaos Great Weapon via the "chaos craft" exception). The principle ensures Great Weapon ≠ "+S +AP free" — the trade-off is consistent damage uplift in exchange for strike-order disadvantage. Audit future Great Weapon profiles against this principle; existing units may need a retrofit pass when convenient.
