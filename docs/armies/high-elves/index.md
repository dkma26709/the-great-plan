# High Elves


> The Asur of Ulthuan. Ten thousand years of perpetual war against Druchii, Daemons, and the lesser threats of the world have honed their tactics to a perfection no younger race can match. Every Asur unit is the product of millennia of compressed training — citizen-soldiers at the rank-and-file, warrior-cults at the elite tier, master-craftsmen across both.

## Status

**Currently classed as §18 Cross-Faction Reference** — a single representative unit (High Elf Spearmen) at present, with full-faction promotion deferred until the roster is broader. This document is the design reference for future Asur unit drafts: it captures the philosophy, axes, and constraints that should hold across the faction so each unit's design loop starts from a shared baseline.

**Drafted units:** [High Elf Spearmen](units/high-elf-spearmen.md), [Swordmasters of Hoeth](units/swordmasters-of-hoeth.md), [War Lions](units/war-lions.md), [Sun Dragon](units/sun-dragon.md), [Moon Dragon](units/moon-dragon.md), [Star Dragon](units/star-dragon.md), [Flamespyre Phoenix](units/flamespyre-phoenix.md), [Frostheart Phoenix](units/frostheart-phoenix.md), [Arcane Phoenix](units/arcane-phoenix.md).

**Asur Phoenix (three variants):** [Flamespyre Phoenix](units/flamespyre-phoenix.md) (Young, +131 mount-adder, Wildfire 6" AoE damage), [Frostheart Phoenix](units/frostheart-phoenix.md) (Aged, +140 mount-adder, Cold Aura heavy debuff), [Arcane Phoenix](units/arcane-phoenix.md) (Magic-attuned, +126 mount-adder, Emberstorm Movement-phase template drop). All three share *mid-Monster Hero-mount biology* (W 7, MA 5 / MD 5, S 4) with **distinctive NA**: Flamespyre none, Frostheart 5+, Arcane none. All three share *Fly 8, Magical Attacks, Fiery Rebirth* (resurrection on 4+ at half W), and **Attuned to the Winds** *(variable Ward Save scaling with Magic phase D6 roll — 1-2 no Ward / 3-4 6+ / 5 5+ / 6 4+)*. The Phoenix is the *magical counterpart* to the pure-biology Dragons — sacred to Asuryan, biologically infused with firmament-fire. Mount options for Anointed of Asuryan Hero characters (pending separate character draft). Lore: aging Flamespyres cool into Frostheart form; the Arcane is a distinct magic-attuned variant drawn from Asuryan's side when the Winds howl. Framework documented in `Flamespyre Phoenix/design.md`.

**Asur Dragons (three age tiers):** Sun Dragon (Young, +169 mount-adder, W 8, NA 5+), Moon Dragon (Mature, +323 mount-adder, W 10, NA 4+), Star Dragon (Ancient, +511 mount-adder, W 12 super-apex, NA 3+). All share the *pure Dragon biology baseline* documented in `Star Dragon/design.md` — Fly 8, Terror, Scaly Skin (scales with age tier), Breath Weapon (Solar / Lunar / Solarflare with scaling S/AP). **No Magical Attacks, no faction overlays on the mount itself** — the Asur Dragons are the *canonical Dragon baseline* in the codebase. Faction rules (Disciplined, Elven Grace, Martial Prowess) come from the *rider's* profile and project onto the combined model per §1. Other faction Dragons (Black Dragon, Chaos Dragon, Zombie Dragon, Forest Dragon, Bone Dragon, etc.) will modify the breath weapon and add their own faction-specific identity rules on top of this baseline. Mount options for Caledorian Princes, Dragon Princes, Phoenix Kings, and other Asur Lord-tier characters (all pending separate character drafts).

## Cultural axis

Within the elf species, three sub-factions share biology but warp the cultural axis differently:

| Sub-faction | Cultural identity | MA / MD axis | Recovery trait |
|---|---|---|---|
| **Asur** (High Elves) | Disciplined citizen-soldiers, ten-millennia drill, warrior-cults at elite tier | **MA ≈ MD** (disciplined-balanced) | **Disciplined** baseline |
| **Druchii** (Dark Elves) | Khainite raiders, frenzied bloodlust, slave-society militarism | **MA > MD** (frenzied-attacker) | Often Frenzy / cult-specific |
| **Asrai** (Wood Elves, pending) | Forest-rangers, ambush-hunters, kite-and-fade | **MA < MD** (skirmisher-evader) | Likely neutral or skirmisher-specific |

Asur sit at the disciplined-balanced pole. Their elites do **not** scale offensively at the expense of defence (that's the Druchii direction) — they scale via more attacks, higher I, and specialised one-hit mechanics like Killing Blow, while maintaining a balanced MA/MD.

## Stat patterns

Baseline rank-and-file Asur (High Elf Spearman as the reference):

| M | MA | MD | BS | S | T | W | I | A | Res | NA |
|---|----|----|----|---|---|---|---|---|----|----|
| 5 | 4 | 4 | 4 | 3 | 3 | 1 | 5 | 1 | 9 | — |

**Cross-faction +1 Res convention:** Asur carry **Res 9 at rank-and-file** — one above the elf species baseline of 8. Same convention applied to Empire State Troops and Bretonnian Knights (the *disciplined* factions). **Not** applied to Druchii or Greenskins; Druchii are Frenzied-volatile rather than steady. The +1 reflects the ten-millennia-of-discipline framework: an Asur Spearman holds his line more steadily than the underlying elf biology would suggest.

**Stat ladder for Asur units** *(drafted or expected — updated 2026-05-13 with the Swordmasters draft and War Lions draft; Swordmasters pushed cult-elite stats to the apex of the projection band, War Lions established the Warbeast tier)*:

| Tier | Indicative M | MA | MD | I | Res | Notes |
|---|---|---|---|---|---|---|
| **Core rank-and-file** | 5 | 4 | 4 | 5 | 9 | Spearmen *(drafted, 12 pts)*, Archers, Lothern Sea Guard |
| **Elite cult-infantry** | 5 | 5-7 | 5-7 | 6-7 | 9-10 | Swordmasters *(drafted, 27 pts — apex of band at MA/MD/I 7, Res 10)*, Phoenix Guard, White Lions |
| **Warbeasts (Cult of Chrace)** | 7 (8 effective via Skirmishers) | 5 | 4 | 5 | 6 | War Lions *(drafted, 24 pts — W 3 Skirmisher pack-hunter with Pride Hunter vs Infantry + Thick Pelt 5+ save vs ranged only; non-elven biology so no Elven Grace / Martial Prowess)* |
| **Mounted Core** | 8-9 (mount) | 4 | 4 | 5 | 9 | Silver Helms, Ellyrian Reavers |
| **Mounted elite** | 9 (mount) | 5 | 5 | 6 | 9 | Dragon Princes |
| **Hero characters** | — | 6 | 6 | 7-8 | 10 | Anointed, Loremaster of Hoeth, Mages |
| **Lord characters** | — | 7-8 | 7-8 | 8-9 | 10 | High Elf Prince, Archmage |

## Biological constraints

The shared elf-species ceiling (per §13) is hard:

- **T 3 / W 1 at rank-and-file** — never raised by elf-cultural rules. Asur elites get more attacks, higher MA/MD, sometimes Killing Blow or Always Strikes First; they **do not** get T 4 or W 2.
- **No Natural Armour** — Asur protection comes from worn armour (ithilmar mail), Elven Grace, and Martial Prowess; never from intrinsic hide.
- **Hero-tier W cap 3, Lord-tier W cap 4-5** — Asur Princes are individually formidable but cannot match a Saurus Oldblood's biological bulk.
- **No Monstrous Infantry tier** — elf-bodied units stay slim. Asur reach into Monster-class via *mounts* (Dragons, Manticores, Great Eagles), never via the elf body itself.

## Faction-wide rules

All rank-and-file and most elite Asur **elven** units carry the following at minimum (the rules are *biological* to the elf — non-elven Asur units like War Lions, Great Eagles, and warhorse mounts do **not** inherit them):

- **Disciplined** (per §8) — Asur are drilled professional soldiery without exception. +1 to Recovery rolls.
- **Elven Grace** (per §8 *Defence*) — Ward 6+ in melee vs attacks at the elf's I or lower. Cross-elf rule — shared with Druchii, and expected for Asrai pending the Wood Elf draft.
- **Martial Prowess** (per §8 *Combat*) — reroll to-Hit 1s in melee. **Asur-specific.** The accuracy axis of the elf-prowess pair.

**Non-elf Asur units** (War Lions and similar Warbeasts; warhorse mounts; Great Eagles when drafted) carry the **Asur** keyword (for faction-mechanic interactions) but **not** the cross-elf biological rules above. They may carry their own species-appropriate identity rules (War Lions carry Pride Hunter; Great Eagles will carry Fly + bird-of-prey rules; etc.).

**Druchii prowess axis (for contrast):** the Druchii carry **Murderous Prowess** (reroll to-Wound 1s) — the lethality axis. The two prowess rules are mutually exclusive: an Asur unit carries Martial Prowess, never Murderous; a Druchii unit carries Murderous, never Martial. This is the cleanest mechanical expression of the Asur/Druchii cultural schism — same elf reflex, channelled through discipline (Asur, blows land more often) versus through Khainite ritual (Druchii, blows wound deeper). Future Druchii unit drafts inherit Elven Grace + Murderous Prowess; future Asur drafts inherit Elven Grace + Martial Prowess + Disciplined.

## Elite-tier scaling rules

When scaling an Asur unit above the rank-and-file baseline, the design ladder is:

1. **Increase MA, MD, I together** (skill goes up, not just one side). Swordmasters and Phoenix Guard step from MA/MD 4 to MA/MD 5-6, I 6-7.
2. **Increase A from 1 → 2** at elite cult-infantry tier. Asur elites are *prolific*, not just *accurate*.
3. **Add one specialised offensive rule** — typically **Killing Blow (Any, X)** for one-strike-of-perfection units (Swordmasters), **Frenzy-equivalent** for cult-specific units that justify it (Phoenix Guard's silent-killing-frenzy reading, if drafted), or **Always Strikes First** if lore demands an apex-Initiative read.
4. **Never increase T or W on the elf body.** Cap is biological. Increase Res to 10 for cult-trained elites (Phoenix Guard's wordless discipline justifies it).
5. **Better armour upgrade pathway** — heavy armour standard, sometimes full plate for cult-elite (Phoenix Guard ceremonial plate).

The visible identity that should emerge: an Asur elite is *better at being an elf*, not *less of an elf*. An Asur Swordmaster is a faster, more accurate, more prolific Spearman; he is not a tankier Spearman.

## Equipment patterns

- **Asur Spear** (1H Reach, 2") — drilled phalanx weapon; second-rank-stab is the formation drill. The Spearmen baseline.
- **Longbow** — most Asur infantry carry one alongside their melee kit (Sea Guard's hallmark; standalone for Archers). Asur longbow is exquisite-craft tier, materially better than human warbows of the equivalent role — but lore-true to Asur is *steady marksmanship* not *apex archery* (the latter belongs to the Asrai Glade Bow tradition, not Asur).
- **Elite two-handers** — Swordmasters of Hoeth wield ithilmar greatswords; White Lions axes (great weapons with anti-cavalry framing); Phoenix Guard ceremonial halberds. All 2H, all elite-tier; the elf elite is comfortable in two-handers because high I and Elven Grace partly offset the loss of shield.
- **Heavy armour standard at elite tier** — Phoenix Guard and Dragon Princes wear full plate. Cult-tier elf does not stint on protection.
- **No gunpowder, no crossbows.** Asur reject industrial weaponry on cultural grounds; the Druchii repeater-crossbow tradition does not transfer.

## Magic

**High Magic** is the Asur faction lore — the disciplined ordering of all eight Winds rather than channelling individual lores. Pending dedicated drafting, but the design hooks are:

- Asur Mages are common at Hero tier; Archmages and Loremasters of Hoeth at Lord tier.
- High Magic should be drafted with a *defensive-buff and dispel-strength* emphasis, distinct from the *offensive-burst* of the eight Winds (Fire, Death, etc.) and from the *aggressive corruption* of Druchii Dark Magic.
- A High Magic caster should be able to *enable* the Asur line (buff Elven Grace, enable rerolls, project Magic Resistance) more often than blast enemies off the board.
- **Loremaster of Hoeth** is the iconic apex — a Lord-tier mage with access to all eight Winds lores plus High Magic. Pending design.

## Mounts and monsters

- **Great Eagles** — Asur-specific flying units and skirmish-monsters. Sentient noble birds of the Annulii Mountains; lore-true Asur allies, not subjects.
- **Manticores** — Hero / Lord apex mounts shared with Druchii. Less Asur-anchored than Eagles or Dragons but lore-canonical for certain Princes.
- **Dragons** — apex Lord mount. Asur-trained Dragons are the Star Dragons, Moon Dragons, Sun Dragons (age-tiered) — the Asur Prince-on-Dragon is the faction's apex battlefield commander.
- **Bolt Throwers** (Eagle Claws) — Asur's only war-machine tradition. Light, twin-bolt platforms; no cannons, no stone throwers. Reflects the cultural rejection of heavy industrial warfare.

## Pricing notes

**Pass 9 framework (2026-05-07)** — all Asur units re-derive under §13 with the **0.8× global scaling factor**. Pure 0.8× of WAP printed prices under-prices Asur because the +1 Res convention and Elven Grace + Martial Prowess + Disciplined stack are not in the WAP baseline. The framework correction produces:

- Asur Spearman 12 pts/model (vs WAP ~10 at 1.0× → 8 at 0.8× pure-scale; framework 12 reflects the high-stat compound).
- Swordmaster of Hoeth 27 pts/model (apex stat block at MA/MD/I 7, Res 10, heavy armour, Killing Blow (Any, 4), 5+ Ward vs non-template ranged, Magical Attacks precision-cleaver greatsword).
- War Lion 24 pts/model (Warbeast Skirmisher pride, S 5 T 4 W 3, AP -1 claws, Pride Hunter vs Infantry, Thick Pelt 5+ save vs ranged only; non-elven biology — no Elven Grace / Martial Prowess inheritance).
- Expected Asur ladder for undrafted units *(updated 2026-05-13 to reflect Swordmasters' apex stat block and War Lions' Warbeast-tier — the user's design preference is to push cult-elites toward the upper end of the band)*: Sea Guard ~14-16 / Phoenix Guard ~26-32 (silent-frenzy + full plate) / White Lions ~22-26 / Silver Helms ~22-26 / Dragon Princes ~35-42 / Prince on Dragon ~apex / Lion Chariot of Chrace ~50-70 (Chariot tier, pending §1 Chariot type) / Great Eagle ~apex-Warbeast (Fly + Eagle-tier Monster mount).

**Apply at draft:** trust the framework re-derivation over the WAP printed price when they disagree. The framework gives the right ladder position relative to Empire State Troops (6-8 pts), Saurus Warriors (10 pts), and Chaos Warriors (16 pts). Document any framework-versus-legacy disagreement in the unit's design diary; the framework is the authority during Pass 8+.

## Cross-faction comparators

Useful anchors when drafting an Asur unit and deciding tier placement:

| Comparator | Why it's useful |
|---|---|
| **Empire Greatsword (Disciplined human elite)** | Same disciplined-balanced design valence, human-bodied. An Asur Swordmaster should outclass a Greatsword on MA, MD, I, and on Elven Grace + Martial Prowess; the Greatsword wins on T and W. Pricing: Asur Swordmaster should sit meaningfully above the Greatsword. |
| **Saurus Warrior (Cold-Blooded disciplined)** | Same price tier as Spearman (10 pts vs 12 pts) but biologically opposite — Saurus tanks via T/W, Spearman tanks via I + Ward + reflex. Direct skill-vs-bulk trade-off. |
| **Chaos Warrior (mortal elite top of human-bodied tier)** | The ceiling for non-elf elite infantry pricing. An Asur cult-elite (Phoenix Guard, Swordmasters) should approach but not exceed Chaos Warrior pricing for comparable defensive density; Asur compensates in skill density. |
| **Witch Elf (Druchii frenzied-attacker)** | The contra-axis elf comparator. Same biology, opposite cultural axis: Witch Elf MA 5 / MD 3 + Frenzy versus Spearman MA 4 / MD 4 + Disciplined. Useful when validating that an Asur draft is sitting on the correct axis. |

## Drafting hooks

Open Asur design questions, captured here for future unit passes:

- **High Magic mechanic** — pending. Likely a buff/dispel-anchored lore distinct from the eight Winds. Drafted Asur caster units (Mages, Archmages, Loremaster of Hoeth) will surface specifics.
- **Phoenix Guard silent-frenzy reading** — whether Phoenix Guard carry Frenzy (the *silent dance* readings) or a custom rule that captures the ritual-violence aspect without Druchii overlap.
- **Star Dragon / Moon Dragon / Sun Dragon age-tier mount stat ladder** — apex mounts; framework re-derivation pending.
- **Bolt Thrower** — light Asur war machine, twin-bolt fire mode versus single-bolt anti-monster mode (per WAP). Whether to model the two modes as separate weapon profiles or a single profile with a switch.
- **Loremaster of Hoeth** — Lord-tier apex mage with access to all eight Winds; pricing is challenging because the spell ceiling is unusually high.
