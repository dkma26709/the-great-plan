# §8 Special Rules Glossary


Special rules appear on unit profiles, weapons, and abilities. All universal rules are catalogued here, organised by category. Army- or unit-specific rules (e.g., a specific monster's signature ability) remain inline on the relevant profile; only rules likely to appear on multiple units across multiple armies are defined here.

### Psychology

The keyword **Psychology** tags rules that represent effects on a unit's mental state. A unit with **Immune to Psychology** ignores the effects of all rules tagged Psychology — stress triggers and behavioural impositions from such rules do not apply. Normal stress accumulation from mechanical sources (losing combat, taking wounds, etc.) still applies.

#### Fear *(Psychology)*

This unit radiates Fear. Any enemy unit with a model within **(6 + LiS)"** of any model in this unit suffers **+1 stress**, checked **at the end of the Movement phase** — applied once per turn to each enemy unit in range at that moment. Fear does not stack with other Fear sources. A unit that causes Terror is immune to Fear. A unit within range of both Fear and Terror sources suffers only the Terror effect.

#### Terror *(Psychology)*

This unit radiates Terror. Any enemy unit with a model within **(6 + LiS)"** of any model in this unit suffers **+2 stress**, checked **at the end of the Movement phase** — applied once per turn to each enemy unit in range at that moment. Terror does not stack with other Terror sources. A unit that causes Terror is immune to both Fear and Terror. A unit within range of both Fear and Terror sources suffers only the Terror effect; a unit that causes Fear but not Terror is still affected by Terror from another source.

#### Frenzy

This unit is in the grip of animal rage. While Frenzied (the **F4 fingerprint**):

- **+1 Attack** on a single weapon profile of the model's choice (per the +1-attack convention — single profile, not all profiles)
- **+1 MA** — the rage sharpens the offensive edge; blows land more often
- **-1 MD** — the rage dulls defensive instinct; the unit is easier to strike in return
- **Must declare a charge** against the nearest visible enemy within charge range during its Movement phase, if able
- **May not voluntarily disengage** from combat
- **Must Follow up** when an enemy Falls Back from combat (no Hold option, per §4 Fall Back)
- **Must pursue** when an enemy voluntarily moves out of melee reach during the Movement phase (per §4 Pursuit)
- **Immune to Psychology**
- **Suppresses the state effects of Wavering and Broken** — ignores the -1 to-hit, cannot-charge, and fleeing behaviour while Frenzied. Stress still accumulates and thresholds are still crossed, but the rage carries the unit through

Frenzy is **lost permanently** when the unit loses a combat round (strict loss — ties do not count), or when the unit is actually forced to flee due to being Broken. Once lost, Frenzy does not return except via specific rules that state otherwise. The F4 fingerprint (offensive committment + defensive cost) ensures Frenzy is a high-volatility identity rule — the Frenzied unit hits harder *and* gets hit harder, both directions of the lore-true intensity.

#### Stubborn *(Psychology-adjacent)*

This unit ignores the **state effects** of Shaken and Wavering — the MA / MD / BS penalties and the cannot-charge restriction do not apply. Stress still accumulates normally and the Broken threshold still applies. A Stubborn unit fights at full effectiveness until it finally shatters.

#### Skittish

This unit's **stress thresholds are each shifted down by 1** — Shaken triggers at Res − 5 (instead of Res − 4), Wavering at Res − 3 (instead of Res − 2), Broken at Res − 1 (instead of Res). The unit reaches each morale state one stress earlier than its Resolve would normally suggest. Behavioural nervousness — physically tough but panics readily under pressure. Stacks cleanly with Cold-Blooded (which modifies stress *count* on incoming/recovery, not thresholds).

#### Cold-Blooded

A creature trait — applies to Lizardmen (faction-wide), Dark Elves' War Hydra, and any other cold-blooded biology drafted into the ruleset. Two effects:

- **Slow to register.** Incoming stress is **reduced by 1** (minimum 1). Each stress trigger applies one less than it would for warm-blooded creatures.
- **Slow to fade.** Recovery rolls are **reduced by 1** (minimum 1). Each Recovery sub-phase, the cold-blooded unit sheds one fewer stress than its baseline D3 + modifiers would otherwise produce.

Cold-Blooded captures the reptilian *slowed reaction time in either direction* — not raw resilience (that's Stubborn or high Resolve). A Saurus may still break under sustained pressure; Cold-Blooded just makes each shock take longer to register and longer to forget. Stacks cleanly with Skittish (which modifies thresholds, not stress count) and with Disciplined / Undisciplined (which modify Recovery, applying after Cold-Blooded's -1).

#### Disciplined

A creature/unit trait — applies to drilled veterans, professional soldiery, formation-trained warriors. **+1 to Recovery rolls.** The Disciplined unit recovers from stress slightly faster than baseline through training, command-and-control, and steady morale.

**Typical units:** Saurus Warriors, Saurus Temple Guard, Empire Greatswords, Reiksguard, Bretonnian Knights of all vows, Dwarf Warriors, Chaos Warriors, professionalised elite-Core. Most rank-and-file units carry **neither Disciplined nor Undisciplined** — baseline D3 Recovery is the default; the trait is a flag for genuinely-elite cases, not an exhaustive bin.

#### Undisciplined

A creature/unit trait — applies to rabble, conscripts, peasant levy, feral units. **-1 to Recovery rolls** (floor 1 — Recovery never goes below 1).

**Typical units:** Bretonnian Men-at-Arms, Bretonnian Longbowmen, Goblins (when drafted), Beastmen (when drafted), Orc Boyz, Skeleton Warriors. Most rank-and-file units carry neither — baseline D3 is default; Undisciplined is a flag for genuinely-rabble cases.

**Saurus interaction note:** Saurus Warriors carry both **Disciplined (+1)** AND **Cold-Blooded (-1 Recovery)** → net **0** Recovery modifier. Tracks lore: drilled spawn-brothers offset the cold-blooded slow-fade. Kroxigor carry **Cold-Blooded only** (no Disciplined — dim brute) → net **-1** Recovery, full slow-fade penalty.

#### Animosity *(Greenskin-wide faction trait)*

At the start of each Movement phase, **roll D6** for the unit. The roll is **only made if the unit is not currently engaged in melee combat** — units in melee are too occupied to squabble. On a **1**, the unit's natural aggression breaks discipline. **Roll D6 again** to determine which way the squabble breaks:

- **1-3** — *"Get Stuck In!"* The unit **must declare a charge against the nearest visible enemy** in charge range this Movement phase. If no charge is possible (no visible enemy in range), treat as result 4-6 instead — the bottled-up aggression turns inward.
- **4-6** — *"Did You Spill My Pint?"* The unit takes **D3 hits at the unit's own Strength** (AP 0, D 1) as Greenskins turn on each other. Standard saves apply. Casualties allocated by the controlling player. The unit may move normally this Movement phase.

Iconic Greenskin unpredictability — the unit might surge forward when the player wanted them to hold, or brawl among themselves when the player wanted them to flank. The cost of fielding Greenskins: roughly 1-in-6 per unit per turn the player loses positional control or absorbs self-inflicted casualties.

**Sub-species manifestation** (narrative, not mechanical):
- **Orcs** — bloodlust-driven; the squabble is fists-and-choppas turned on whoever's closest.
- **Goblins** — panic-driven; "abject in-fighting" — scrawny goblins biting and clawing each other in confusion.
- **Snotlings** — distracted-driven; the swarm forgets what it's doing and scatters momentarily.

The mechanical effect is identical across all Greenskin sub-species; the narrative manifestation differs by sub-tribe.

**Applies to: all Greenskin units** — Orcs, Goblins, Snotlings, and Greenskin-allied biology (Trolls, Squigs, Giants when drafted). Even Disciplined Black Orcs roll Animosity (lore: a Black Orc squabble is "Get on with it!" rather than "I'm bored of waiting" — different manifestation, same trigger).

**War Machine exception** *(2026-05-19)*: Greenskin **War Machines** (Goblin Spear Chukka, Goblin Rock Lobber when drafted, Doom Diver Catapult when drafted, and any future Greenskin War Machine entries) **do not roll Animosity**. The rule's force-charge sub-result requires movement actions the unit cannot perform (War Machines cannot Charge), and the Crew when operating the machine are too engaged with loading/aiming to squabble. Unit-profile-level qualification — individual War Machine entries will state "No Animosity" explicitly in their Special Rules section.

**Sub-tribe sub-table variants.** Specific Greenskin sub-tribes replace the standard 1-3 / 4-6 sub-table above with their own variant. Currently drafted:

- **Mushroom Madness** *(Night Goblin sub-tribe)* — replaces the standard sub-table with a six-result D6 table (Pretty Lights / "'Ere We Go!" / Bickerin' / Mushroom Frenzy). See the Night Goblins unit profile for the full table. Sub-tribe-wide: all Night Goblin keyword units (Night Goblins, Night Goblin Shaman, Night Goblin Big Boss, Night Goblin Squig Hoppers, etc.) roll on Mushroom Madness instead of the standard sub-table.

Forest Goblin and Savage Orc sub-tribe variants pending separate drafts.

#### Loves a Scrap *(Orc-specific faction trait — Greenskin sub-species split)*

Two effects:

1. **Stress relief on engagement.** At the end of each **Combat phase** in which this unit was engaged in melee, the unit removes **1 stress**. Brawling physically calms Orcs — every round of combat bleeds tension off the unit, and the squabbling-Animosity dissipates the moment there's a real fight to have.

2. **Sustained-combat momentum.** If this unit was engaged in melee combat at the end of the previous turn, the unit gains **+1 Attack** on a single weapon profile of each model's choice this turn (per the +1-attack convention — single profile, not all profiles). The momentum of the brawl carries forward — Orcs warm up to the fight and hit harder the longer it lasts.

**Applies to: Orc-sub-species Greenskins** — Common Orcs (Boyz), Big 'Uns, Black Orcs, Savage Orcs, Boar Boyz, Orc characters. **Goblins explicitly DO NOT inherit Loves a Scrap.** Goblins do not enjoy combat — brawling drains them, doesn't refresh them. The Greenskin faction split at the Orc/Goblin sub-species boundary is the cleanest mechanical expression of "Orcs love a fight, Goblins do not." Goblin units carry **Animosity** and **Undisciplined** but no Loves a Scrap. Greenskin-allied biology (Trolls, Squigs, Giants) likewise do not inherit Loves a Scrap — they may carry Animosity but not the Orc-specific brawl-bonus.

Pairs thematically with Animosity: an Orc unit that *isn't* fighting accumulates problems (Animosity squabbles, no momentum bonus), while one that *is* fighting bleeds stress off naturally and ramps up its attack output. Player incentive: keep the Boyz engaged.

#### Resolute *(Dwarf-wide faction trait)*

When this unit would convert **combat resolution loss to stress** (per §5 — losing combat causes the loser to take stress equal to the CR difference), the unit **subtracts 1** from the converted total (minimum 0). The dwarf phalanx absorbs the indignity of losing slightly better than other races.

Translates the WAP "lose by 1 less" Break-test mechanic to our stress-based combat-resolution system. Lore-grounded in the iron-stoic Dwarf identity — even when losing the field, the Dawi don't crack as fast as mortal humans or panicky Goblins.

**Applies to: all Dwarf units** (faction-wide species trait — including Slayer Cult, Thunderers, Ironbreakers, Hammerers, characters, war-machine crews). Stacks cleanly with Stubborn (state-effect immunity) and Disciplined (Recovery +1) — three separate morale-resilience layers, all Dwarf-faction-wide.

#### Trait Reference Table *(faction-wide trait assignments — broad-strokes; refined per-unit in retrofit pass)*

Cross-faction reference for which units carry **Disciplined** / **Undisciplined** / **Cold-Blooded** baseline traits. Used during the structural retrofit pass to assign Recovery modifiers without touching every profile individually. Per-unit refinements (e.g., a specific Skink unit being more nervous than baseline) come in the detailed retrofit pass.

| Faction | Disciplined units | Undisciplined units | Cold-Blooded units |
|---------|-------------------|----------------------|---------------------|
| **Lizardmen** | Saurus Warriors, Saurus Temple Guard, Saurus characters (Oldblood, Scar-Veteran), Aggradon Lancers, Horned One Riders | — | **All Lizardmen units** (faction-wide trait — Saurus, Skink, Kroxigor, Saurian beasts, Slann) |
| **Empire** | All State Troops (Halberdiers, Handgunners, Swordsmen, Spearmen, Crossbowmen — drilled-daily professional standing army), Greatswords, Reiksguard, Imperial Knights, Demigryph Knights, Wizard Lord, Imperial General, Empire characters | — | — |
| **Bretonnia** | Knights of the Realm, Knights Errant, Questing Knights, Pegasus Knights, Bretonnian Lord, Paladin, Damsel, Prophetess | Men-at-Arms, Longbowmen, Bidowers, Field Trebuchet crew | — |
| **Ogre Kingdoms** | Tyrant, Bruiser, Slaughtermaster (commander tier — drilled by violence rather than discipline) | Ogre Bulls (rabble), Gnoblar units (when drafted) | — |
| **Vampire Counts** | Vampire Lord, Vampire characters, Grave Guard | Skeleton Warriors, Zombies (rabble baseline; Undead-specific morale rules layer on top) | — |
| **Dark Elves (§18)** | Witch Elves (Khainite-trained — but Frenzy fingerprint suggests neutral baseline; flagged for refinement in detailed pass) | — | — |
| **High Elves (§18)** | High Elf Spearmen (millennia-trained citizen-soldiers) | — | — |
| **Dwarfs (§18)** | Dwarf Warriors (every adult is drilled in formation), elite Dwarf units | — | — |
| **Greenskins (§18)** | — | Orc Boyz, Forest Goblin Crew (and any other Greenskin rank-and-file when drafted) | — |
| **Warriors of Chaos (§18)** | Chaos Warriors (Will of Chaos already grants reroll-recovery; Disciplined would double-stack — leave neutral baseline; refine in detailed pass) | — | — |
| **Tomb Kings (§18)** | Tomb Guard Crew (drilled-veteran undead) | — | — |

**Note on net Recovery effects:**
- **Saurus Warriors** = Disciplined + Cold-Blooded = net 0 (baseline D3 Recovery)
- **Skink Cohort / Skirmishers** = Cold-Blooded only = net -1 (D3 minus 1, floor 1)
- **Kroxigor** = Cold-Blooded only = net -1
- **Slann** = Cold-Blooded only = net -1 (toad-cold metabolism; Recovery -1 on a Lord-tier Resolve floor)
- **Bretonnian Knights** = Disciplined = net +1 (D3 + 1)
- **Bretonnian Men-at-Arms** = Undisciplined = net -1
- **Empire State Troops** = Disciplined = net +1 (D3 + 1) — all five State Troops (Halberdiers, Handgunners, Swordsmen, Spearmen, Crossbowmen) carry Disciplined per pass 2; daily-drilling lore captured. State Troops rule (reroll near General/BSB) layers on conditionally
- **Empire Greatswords** = Disciplined + Professional Soldiers (auto-reroll) = effectively very high Recovery floor
- **Chaos Warriors** = Will of Chaos (reroll recovery) = effective +1 Recovery via reroll, Disciplined would double-up; leaving neutral baseline avoids the stack

This table is the global reference for faction trait assignment. Per-unit overrides (specific Lizardmen unit not Cold-Blooded for some lore reason, etc.) handled in the detailed retrofit pass.

#### Unbreakable

This unit does not accumulate stress, cannot become Shaken, Wavering, or Broken, and is **Immune to Psychology**. State effects never apply. The unit fights at full effectiveness until physically destroyed.

#### Immune to Psychology

This unit ignores the effects of all rules tagged Psychology (Fear, Terror, and others with the Psychology keyword). Stress triggers or behavioural impositions from such rules do not apply.

#### Stupidity *(Psychology)*

The unit is slow-witted, easily distracted, or simply not bright enough to follow complex orders without direction. At the start of the affected unit's activation in the Movement phase, it must take **one** of the following actions, and nothing else, that phase:

- **Charge** the nearest valid enemy within charge range (must declare if eligible), OR
- **Advance** its full M directly toward the nearest visible enemy, OR
- If no enemy is visible, **Advance** its full M — the unit may wheel, pivot, and turn freely as it lumbers (it is aimless, not stuck on a rail).

Restrictions while Stupidity is active this turn:

- Cannot **March**
- Cannot **Rally** unless required by Broken status
- Voluntary **wheels and pivots are permitted** during any Advance
- Ranged weapons may still be fired in the Shooting phase at the normal move-and-shoot penalty (Quick to Fire relieves as usual)

Sub-phase timing: the forced **Charge** is declared in the Charges sub-phase (§7.2a) like any other charge; a forced **Advance** resolves in the Normal Movement sub-phase (§7.2b).

**Design requirement.** A unit bearing Stupidity must be balanced against the loss of tactical control by at least one of:

- A **mitigation condition** (e.g., proximity to a specific ally, a character with a relevant rule)
- A **compensating benefit while Stupidity is active** (Fear/Terror aura, combat bonus on the forced advance, Immune to Psychology)
- **Raw strength** sufficient to absorb the tactical clumsiness

Stupidity without any of the above is a dead rule — the loss of control must be paid for with upside somewhere.

#### Unstable *(Psychology)*

This unit ignores the state effects of Shaken, Wavering, and Broken — no to-hit penalty, no cannot-charge, no mandatory flee. The unit **cannot be Rallied** (there is no morale to restore). Instead, whenever this unit's current stress would exceed its Res, each point of excess stress is immediately converted to **1 wound (no save of any kind)** dealt to the unit, and stress is capped at Res.

The mass does not panic — it bleeds. Pressed hard enough, and fast enough, the unit simply scatters until there is nothing left. Removed from play when its wound pool reaches zero, as any other unit.

#### Undead *(unit keyword)*

A unit with the **Undead** keyword is animated by necromantic will, not biological will, and operates by a different stress paradigm than living units. The keyword grants the following package:

1. **Has Unstable, with one variant — end-of-Combat-phase resolution.** The Unstable mechanic above applies, except that **stress is not capped at Res during the turn**. Stress accumulates freely from any source. At the **end of each Combat phase**, if the unit's stress is over Res, the excess (current stress − Res) is immediately converted to **wounds** (1 wound per point over, no save of any kind) dealt to the unit, and stress drops to Res. Wounds are allocated to any models in the unit per the controlling player's choice. The lore name for this is **Crumble** — bones collapse and rotting flesh dissolves where the necromantic binding gives out. *(Tactical consequence: Necromancy spells in the Magic phase that remove stress can intervene before the Crumble resolves; this is a deliberate lever for the Vampire / Necromancer player.)*

2. **No psychology-source stress.** Undead do not accumulate stress from **Fear, Terror, friendly-unit-destroyed-within-6"**, or other psychology triggers — the dead do not fear, do not grieve. **However, Undead still accumulate stress from being a shooting target** (+1 per Shooting phase per §5) — this represents strain on the necromantic binding rather than psychological reaction. Stress from own-unit casualties and lost combat differentials accumulates normally per §5/§6.

3. **No retreat.** An Undead unit that loses a combat does not fall back — it holds its ground. In addition to the standard stress for losing (per §5), the unit takes **+1 stress per inch of the fall-back distance it refused** (the combat difference, up to the 6" fall-back maximum) — resolved exactly as a fully-blocked fall-back path per §4. The winner does not choose Follow up or Hold; no gap opens and the melee simply continues next turn. The necromantic anchor permits no retreat — the binding strains instead.

4. **Immune to Psychology.** Stupidity, Frenzy, Hatred-as-test, and other Psychology-rule triggers do not apply. The necromantic will commands directly; the bones don't have second thoughts.

5. **Cannot Rally** (inherited from Unstable; reiterated for clarity). Stress is removed only via the Start of Turn Recovery roll (per §5) or Necromancy spells (e.g., Invocation of Nehek). If the army's necromantic master falls and no spell support remains, an Undead unit can accumulate stress to fatal levels — the death-spiral is on theme: the master provides the drive and the magic; without him, the dead simply unwind.

### Command and Coordination

#### Command *(ability keyword)*

An ability tagged **`[Command]`** represents an order, signal, or rallying effect projected from a chain of authority — a general's voice carrying across a battle line, a banner held high, a horn or drum cadence, a champion calling cadence in a phalanx. `[Command]` abilities only affect **Formed units**. Loose units cannot receive `[Command]` effects: the man pacing alone in skirmish order does not hear his colour-sergeant, does not see the regimental drum-major's cadence, does not stand under the banner. He is on his own.

A `[Command]` ability that projects from a source with an area of effect (e.g., the General's Inspiring Presence within 12") **fails to apply** to any Loose unit in the area. The ability is not "wasted" — it can still affect Formed units in range — but the Loose unit is treated as outside the radius for that ability.

**`[Command]` projects from a source to a recipient.** The keyword applies to abilities where source and recipient are different units (typically a character's aura affecting friendly units within range). Unit-internal upgrades — Patrol Leader, Standard Bearer, Musician, Magic Standards borne by the unit's own model — are **not** `[Command]`. They apply to the unit they belong to regardless of formation state, because they *are* the unit, not orders projected onto it.

**`[Command]` is not magic.** Spells, magical auras, and divinely-projected effects are *not* `[Command]` even when they mimic the same shape (e.g., a "general's aura" cast from a spell lore). Magic operates on a different mechanical layer; Loose units feel magical effects normally.

**`[Command]` is not biology, devotion, or trait.** Faction-wide passive traits (Will of Chaos, Cold-Blooded, Animosity), psychological states (Frenzy, Hatred, Stupidity), and intrinsic identity rules (Pack Cohesion, Loves a Scrap, Elven Grace, Cohort Synchronicity) are *not* `[Command]`. A trait belongs to the unit; an order is projected onto it.

**Identified `[Command]` abilities** *(initial enumeration; new abilities tagged as drafted)*:

- **Inspiring Presence** *(General trait)* — friendly units within 12" treat Resolve as +1 for stress threshold purposes
- **Banner Discipline** *(BSB trait)* — friendly units within 12" gain +1 to Recovery rolls

Additional `[Command]` candidates surface during faction draft passes; auditing each character / Lord / shrine entry for command-projection effects is part of standard draft review.

### Combat

#### Hatred (X)

Where X specifies the hated target (a unit type, faction, keyword, or "All" for indiscriminate hatred). In the first round of each melee combat engagement against a hated target, the bearer may reroll failed melee to-hit rolls. Applies only in melee, only to the to-hit roll, only in the first round of a given engagement. If the unit later enters a fresh combat with a hated target (including re-engagement with the same unit), Hatred triggers again — it is about the heat of initial contact. Frenzy's charge requirement takes precedence over Hatred's preferences; Hatred is a bonus when circumstances allow it.

#### Martial Prowess

A model with this rule may **reroll to-Hit rolls of 1** in melee. The millennium-of-training reflex — every blow finds its target unless the elf himself fumbles. Faction-wide for **Asur** (High Elves), capturing the disciplined-accuracy cultural axis. The Druchii do **not** share this rule — their lethality emphasis is expressed via *Murderous Prowess* (below) rather than to-Hit reroll. **Asrai** (Wood Elves, pending draft) — prowess assignment deferred until the Asrai faction pass; either Martial or Murderous fits, and the call should be made when Asrai units are drafted.

Reroll applies to the melee to-Hit roll only — not to-Wound, not Strike-Order, not ranged. The reroll cannot itself be rerolled (per the standard reroll-once convention). Stacks cleanly with Hatred (which rerolls *failed* hits in round one); Martial Prowess covers the residual 1s after Hatred has consumed its first-round window.

#### Murderous Prowess

A model with this rule may **reroll to-Wound rolls of 1** in melee. The Druchii training emphasis — every blow is meant to kill, not merely engage. Faction-wide for **Druchii** (Dark Elves), capturing the lethality cultural axis. The Asur do **not** share this rule — their accuracy emphasis is expressed via *Martial Prowess* (above) rather than to-Wound reroll. The two are *parallel* faction-wide rules: same biological reflex framework, different cultural channel.

Reroll applies to the melee to-Wound roll only — not to-Hit, not Strike-Order, not ranged. Per the standard convention (cf. Predatory Fighter), the "1" is the **unmodified** natural die face — the reroll triggers regardless of any +/- modifiers that would have applied. The reroll cannot itself be rerolled (per the standard reroll-once convention).

#### Hunter's Prowess

A model with this rule may **reroll to-Hit rolls of 1 with ranged attacks**. Faction-wide for **Asrai** (Wood Elves), capturing the marksmanship cultural axis. The reflex framework that the Asur channel into melee accuracy (Martial Prowess) and the Druchii channel into melee lethality (Murderous Prowess), the Asrai channel into the bow — the apex longbow tradition of Athel Loren, the hunter's eye made manifest.

Reroll applies to the ranged to-Hit roll only — not melee, not to-Wound, not Strike-Order. The "1" is the **unmodified** natural die face — the reroll triggers regardless of any +/- modifiers that would have applied (a roll that needed a 3+ and came up a natural 1 with a -1 modifier still rerolls). The reroll cannot itself be rerolled (per the standard reroll-once convention). Stacks cleanly with weapon-specific rerolls (e.g., Quick to Fire) where both rules permit a reroll of the same die; the model picks which reroll source to apply (rerolls do not chain).

Asur, Druchii, and Asrai inherit one — and only one — of the three prowess rules: Asur **Martial Prowess** (melee to-Hit reroll-1s), Druchii **Murderous Prowess** (melee to-Wound reroll-1s), Asrai **Hunter's Prowess** (ranged to-Hit reroll-1s). The three are mutually exclusive across the elven sub-factions, modelling the same biological reflex framework expressed through three distinct cultural channels.

#### Killing Blow (Target, X)

On an unmodified wound roll of 6 against a model matching *Target*, this attack deals X damage instead of its normal Damage value. **Excess damage does not carry between models** — damage beyond what the wounded model can absorb is wasted. If multiple Killing Blow rules on the same attack match the target, use the most favourable.

Target can be a wound threshold (e.g., W ≤ 2, W ≥ 4), a unit type or keyword (e.g., Monster, Cavalry), a specific faction (e.g., Elves), or "Any" for no restriction.

#### Lightning Attacks

Attacks with this keyword ignore armour saves entirely. Ward saves (including Magic Resistance and Regeneration) still apply normally.

#### Armour-Seeking

An attack with this keyword resolves its **wound roll** against the target's armour rather than the standard Strength-vs-Toughness comparison. Each hit wounds on a D6 roll **equal to or higher than the target model's unmodified worn armour save value**.

*Worn armour* means armour derived from equipment — plate, mail, leather, shields, helmets, barding. **Natural Armour** (scales, hide, bone plates, or any armour save that is part of the model's body rather than its gear) does **not** count as worn armour for this rule.

- A target in 3+ worn armour is wounded on a **3+**.
- A target in 5+ worn armour is wounded on a **5+**.
- A target in 6+ worn armour is wounded on a **6+**.
- A target with **no worn armour** (whether unarmoured or relying purely on Natural Armour) **cannot be wounded** by Armour-Seeking attacks — the attack has no metal to find.

Armour-Seeking does not modify the armour save roll itself. The target still saves using its normal (or modified) armour value, including any Natural Armour component. The keyword changes only how the wound roll is resolved.

Strength and Toughness are irrelevant to the wound roll of an Armour-Seeking attack.

**Combined models (rider and mount):** Armour-Seeking reads the model's **best single worn-armour source at its face value** — the rider's worn armour or the mount's barding — ignoring Natural Armour and all combination/conversion steps. A model whose protection is purely Natural Armour (an unbarded beast with an unarmoured rider) cannot be wounded by Armour-Seeking.

#### Flaming

Attacks with this keyword have two effects:

- **Negate Regeneration** — wounds caused by Flaming attacks cannot be saved with Regeneration (other wards still apply)
- **Panic beasts** — a unit containing any model with **US 2 or higher** suffers +1 stress when targeted by a Flaming attack, once per phase regardless of how many Flaming attacks hit. **Exception:** a unit that has any Flaming attack in its own weapon profile is immune to this stress effect — its beasts are accustomed to fire

Flaming has no other inherent effect; its significance comes from rules that interact with the keyword.

#### Flammable

Attacks with the **Flaming** keyword targeting this unit reroll failed to-wound rolls. Represents units made of dry wood, oil-soaked cloth, straw, pitch, or otherwise susceptible to catching and spreading fire. Fire takes hold on the target and burns worse than a normal flame-hit would.

#### Breath Weapon

A keyword on weapon profiles that flags the attack as a **cone-exhalation attack** — gas, flame, frost, acid, venom, or other exhaled medium projected from a creature's mouth or throat. Distinguished from weapon-strike attacks (sword, axe, lance) by the delivery mechanism: a Breath Weapon is the creature's own exhalation, not a weapon swing.

Breath Weapons are typically ranged template attacks (Flame Template per §7 Templates) and often combined with **Flaming Attacks**, but neither is intrinsic — the Breath Weapon keyword itself does not carry built-in Flaming or Template attributes. The weapon profile lists those independently. The keyword is a **tag** that other rules can reference (e.g., immunity items, anti-dragon armour, cone-blast defensive auras) — distinguishing breath-attacks from weapon-Flaming attacks (a sword wreathed in flame is Flaming but not a Breath Weapon).

Currently used by: Salamander Spout Flames (§10 Lizardmen Armoury). Future units / items expected to use the keyword: Wyvern / Dragon breath, Chimera breath, Wyrmlance / Wyrmbreath Vial (Bretonnia magic items pending expansion), Skaven Warpfire Throwers, Plague Censer Bearer breath-cloud, etc.

#### Magical Attacks

A keyword applied to attacks (melee weapons, ranged weapons, spells, natural weapons). Attacks inherently have Magical Attacks if they come from:

- Spells (all spell effects)
- Magic items (enchanted weapons, artefacts, blessed gear)
- Bound magical effects (scrolls, totems, relics)

Other attacks have Magical Attacks only if explicitly stated.

Magical Attacks has no inherent mechanical effect on its own — its significance comes from rules that interact with the keyword (e.g., Ethereal, future anti-magic wards, undead or construct vulnerabilities). Anchor scaffolding, same pattern as Flaming.

#### Poisoned Attacks

Attacks with this rule gain **+1 to wound**. Poison does not care about size or toughness — a poisoned blade wounds easier whatever it touches.

#### Predatory Fighter

Unmodified melee to-hit rolls of 6 generate an additional attack. These additional attacks are resolved at the same Initiative step and cannot themselves generate further extras.

The predator-instinct biology also compels chase. When an enemy unit Falls Back from combat with this unit, this unit **must Follow up** (no Hold option, per §4 Fall Back). When an enemy unit voluntarily moves out of melee reach during the Movement phase, this unit **must pursue** (per §4 Pursuit). The chase is not a choice — and being baited out of position by a fast-disengaging opponent is a real downside of the rule, balancing the bonus-attack upside.

#### Pursuit Predator

A unit-or-character keyword bundling three "the chase doesn't end" effects driven by apex predator-instinct biology — the rule's wearer is markedly harder to disengage from than ordinary combat-loving units:

- **Forced Follow up.** When an enemy unit Falls Back from combat with this unit (per §4 *Losing Combat — Fall Back*), this unit **must Follow up** — the Hold option is removed. The chase is mandatory.
- **Wipeout free move.** If this unit wipes out an enemy unit in melee (all enemy models slain in the same combat round), it may immediately make a **free move of up to 6"** toward the nearest visible enemy unit. The kill instinct does not stop at the corpse pile.
- **Movement-phase pursuit upgrade.** This unit rolls **D6"** instead of the standard D3" for the §4 *Pursuit* reaction (when an enemy voluntarily disengages during the Movement phase). The apex-predator instinct turns the chase into a serious follow-up, not a token snap.

Stacks distinctly with **Predatory Fighter** (different keyword — extra attacks on melee 6s) and **Frenzy** (different keyword — also forces Follow up + Movement-phase pursuit, but at D3"). When multiple compulsion sources are active on the same unit, the "must Follow up" and "must pursue" clauses fire once per trigger (no double-pursuit); the D6" pursuit distance from Pursuit Predator is the better source and supersedes Frenzy's D3" if both are present.

Currently appears on: Carnosaur (mount profile, §10) and Wild Carnosaur (Rare standalone, §10). Forward-compatible with future apex-predator drafts (Hippogryphs, larger predators, certain Monster-tier units).

#### Impact *(weapon keyword)*

An attack profile with the Impact keyword may only be used on the turn the wielder successfully charges into combat. Impact attacks resolve **immediately on successful charge contact, within the Charges sub-phase (§7.2a)** — not in the Combat phase. Against each enemy model within the weapon's Reach of any charging model in base contact, resolve one attack using this profile. Strength equals the charging unit's Strength (or its mount's Strength if mounted). AP, Damage, and Reach are as listed in the profile. Damage does not carry between models. Failed charges produce no Impact attacks. Impact resolves only on the turn of the charge; subsequent Combat phase rounds use the unit's normal attack profiles.

Because Impact resolves in the Movement phase, casualties from Impact are removed before the Combat phase begins — a defender may have its formation broken or its front rank thinned before its own attacks are made. Wounds lost to Impact count against the Movement phase for the "2 wounds in a phase = +1 stress" trigger, and count toward the charger's side in that combat's CR total (per §4 *Combat Resolution*).

#### Always Strikes First

An attack with this rule resolves before any other attacks in the Combat phase, regardless of the attacker's Initiative (effectively at a higher-than-possible Initiative step). If the attacker's Initiative is also higher than the target model's, the attacker additionally re-rolls failed to-hit rolls against that target in melee.

Always Strikes First applies per-attack, not per-model: a model could have it on one weapon and not another.

Always Strikes First does not pre-empt Impact attacks, which resolve in the Movement phase before the Combat phase begins.

#### Always Strikes Last

An attack with this rule resolves after all other attacks in the Combat phase, regardless of the attacker's Initiative (effectively at a lower-than-possible Initiative step). If the attacker's Initiative is also lower than the target's, the target additionally re-rolls its successful to-hit rolls against this attacker in melee.

Always Strikes Last applies per-attack, not per-model — a model could have it on one weapon and not another.

**Interaction with Always Strikes First:** if exchanged attacks between attacker and target have opposing modifiers (one ASF, one ASL), the two cancel for that exchange and each attack resolves at its own Initiative step normally. Likewise, if a single attack has both ASF and ASL applied from separate sources, the two cancel and the attack resolves at the attacker's normal Initiative.

Always Strikes Last is a rare rule reserved for specifically thematic cases — a uniquely unwieldy artefact, a cursed weapon, a creature afflicted with real sluggishness. It is **not** the default cost of heavy or two-handed weapons.

#### Sniper

Attacks with this rule may be directed at any specific model in a target unit, bypassing the normal "models in weapon reach take wounds first" allocation. The attacking player chooses which enemy model the attack targets, provided:

- The chosen model is in line of sight of the shooter, and
- The shot suffers **-1 to hit**, reflecting the precision required

Sniper attacks also bypass the character-in-unit protection (§6.3): a character standing within a friendly unit, normally shielded from enemy shooting, may be targeted directly by Sniper attacks.

Sniper may appear as a **weapon keyword** (a rifle, a longbow with special sights, a crossbow on a tripod) or as a **unit or model rule** (a trained sharpshooter, a dedicated assassin). The mechanic is identical either way.

#### Mighty Blow (X)

May appear as a unit/model rule or as a weapon keyword:

- **As a unit/model rule:** all the bearer's melee attacks gain **+X Strength** in the first round of each melee combat engagement.
- **As a weapon keyword:** only the specific weapon's attacks gain **+X Strength** in the first round of combat. Other weapons the same model wields are unaffected.

Applies only in the first round of a given combat. If the unit disengages and re-engages in a later turn, Mighty Blow triggers again in the first round of the new engagement (same pattern as Hatred).

Stacks with charge bonuses, buffs, and other Strength modifiers. Works regardless of who charged — either side's Mighty Blow triggers in the first round of their engagement.

#### Devastating Charge

May appear as a unit/model rule or as a weapon keyword. On the turn the bearer successfully charges, its attacks gain **+1 Attack**:

- **As a unit/model rule:** all the bearer's melee attacks get +1 A on the charge.
- **As a weapon keyword:** only the specific weapon's attacks get +1 A on the charge.

Applies only on the turn of the charge; subsequent combat rounds use the normal Attacks value. Stacks with other Attacks modifiers (Frenzy, spell buffs, weapon-level charge bonuses). Intended for units or weapons with a specific charge niche — cavalry, shock troops, momentum-focused melee specialists.

#### Ward Piercing (X)

Attacks with this rule reduce the target's ward save by **X** steps. Applied to the target's **final** ward save (after stacking has been resolved), regardless of which sources contribute. If the reduction would make the save impossible (e.g., Ward Piercing (3) against a 6+ ward), no ward save is attempted against that attack.

Ward Piercing does not discriminate by ward source — it reduces Regeneration, Parry, Dodge, Ward vs Spells, Magic Resistance wards, and any other ward equally. This is distinct from **Flaming**, which specifically negates Regeneration entirely; Ward Piercing and Flaming are separate mechanisms that can coexist on a single attack.

May appear as a weapon keyword, a spell rider, or a unit/model rule. Typical values: 1 for a moderately magic-piercing effect, 2 for a strong one, 3 for a genuinely ward-shredding artefact or divine curse.

#### Dispersed Mass

Any attack targeting this unit has its Damage value **capped at 1**, regardless of the weapon's base Damage, any spell multiplier, or rule-granted bonus (Killing Blow's D3/D6, Multiple Wounds (X), multi-wound weapons, spell riders, etc.). Each hit kills or injures only one small creature — there is no single body to absorb a heavier blow.

Dispersed Mass caps only the final Damage value applied per unsaved wound; it does not modify hit rolls, wound rolls, armour or ward saves, or the number of attacks. Effects that bypass saves (Ignores Armour Saves, Ward Piercing) still bypass. The cap applies after all other wound-modifying rules have resolved.

#### Move or Fire

A weapon with this rule may not be fired in any turn during which any model in the unit moved. Represents heavy, slow-to-emplace, or finicky equipment — artillery, emplaced weapon teams, crew-served missile platforms.

"Moved" includes any physical relocation of models in the unit: Advance, March, Charge, wheel, pivot-reform, fall-back, Broken flee, voluntary Flee reaction, and Elusive's reactive move. It does **not** include Rally (no movement), Stand and Shoot (no movement), or Displacement (a unit being physically pushed by another unit's charge — this is imposed, not undertaken).

Move or Fire attaches to specific weapons; the trigger is unit-level. If any model in the unit moves, every Move-or-Fire weapon in the unit is locked out for that turn. The unit may still use weapons without the rule.

#### Quick to Fire

A weapon with this rule ignores the **-1 to-hit penalty for the unit having moved** this turn (see §7.4 Move-and-shoot). It may be fired after Advance, March, or reform at the weapon's normal to-hit rolls. Additionally, Quick to Fire ignores the **-1 to-hit penalty for Stand and Shoot** reactions. Represents light throwing weapons, breath weapons, short-range pistols, and spellcast-like missiles.

#### Ponderous

If any model in the unit moved voluntarily this turn, attacks from this weapon suffer **-2 to hit** (instead of the standard -1 for moving). Stacks with other modifiers. Represents heavy, cumbersome weapons — massive crossbows, heavy arquebus, siege bows.

#### Slow to Fire

A weapon with this rule **may not be used as part of a Stand and Shoot charge reaction**. Shots can still be fired normally in the Shooting phase. Represents weapons that require time to aim, brace, or reload — heavy crossbows, reloadable firearms, precision sniper weapons. Orthogonal to the move-and-shoot gradient; can stack with Ponderous, Move or Fire, etc.

#### Multiple Shots (X)

This weapon fires **X shots per model** per Shooting phase (X is a number, typically 2 or 3). Each shot is resolved separately — hit, wound, save. By default, **each shot suffers -1 to hit** — trying to get off several shots per action costs accuracy. The penalty stacks with other modifiers.

#### Rapid Fire

A weapon with Multiple Shots (X) and this rule **ignores the -1 to-hit penalty from Multiple Shots**. Each shot is resolved at the weapon's normal to-hit. Represents weapons engineered for fast, accurate repetition — repeating crossbows, machine-style spellcasters, multi-chamber handcannons.

#### Volley Fire

Models in a unit armed with weapons that have Volley Fire may shoot even if their line of sight is **blocked by other models in their own unit**, at an **additional -1 to hit** for the volley shot. Weapons must still be within range and the target must be in the model's arc. Enemy units, friendly *other* units, and terrain continue to block LOS normally — Volley Fire bypasses own-unit blockage only.

Per-model decision: each model in the unit independently chooses whether to Volley Fire (taking the -1 to hit) or shoot normally (only available if LiS is unblocked through standard means). Front-rank models with clear LiS typically shoot normally; rear-rank models obscured by their own front rank typically Volley Fire. Represents archers firing in a high arc over the heads of their own front rank — massed bow armies, deep-formation shooting. The -1 to hit captures the loss of precision when shooting indirectly without a clear line on the target.

#### Indirect Fire

A weapon with Indirect Fire does **not require line of sight** to the target. The target must still be within the weapon's range and in the model's shooting arc. Typically paired with a template and Scatter (X). Represents lobbed ordnance — stone throwers, mortars, trebuchet shot, high-arcing artillery.

#### Scatter (X)

A parameter applied to weapons and spells that use templates. X specifies the scatter distance dice expression — common values: **D3**, **D6**, **2D6**, **Artillery Die** (2/4/6/8/10/MISFIRE). When the template is placed, roll a scatter die (4 arrow faces + 2 HIT faces) together with the specified distance roll:
- **HIT:** template lands exactly on the nominated point.
- **Arrow:** template moves the rolled distance in the indicated direction. Ranged weapons subtract the wielder's BS from the scatter distance (minimum 0); spells do not.

Weapons should use **Scatter (D6)** or larger by default — Scatter (D3) is effectively nullified by BS 3+ and should be reserved for niche precision-template weapons.

#### Random Attacks (XDY)

A model with this rule has no fixed Attacks characteristic. Instead, the A field on its profile shows a dice expression (e.g., D6, D6+1, 2D3) which is rolled each Combat phase to determine how many attacks every model in the unit makes that phase. Represents unpredictable flailing or unstable creatures — trolls, tentacled horrors, swarms, wild beasts.

**Rolling:** one roll per unit per Combat phase. All models in the unit use the rolled result for that phase. Rerolled at the start of each new Combat phase. For Impact attacks with Random Attacks, each Impact-instance gets its own roll.

**Modifiers stack on top:** charge bonus (+1 A), Frenzy (+1 A), Predatory Fighter, and other Attacks modifiers apply to the rolled value as normal.

**Minimum and zero results:** the dice expression may produce 0 or negative results (e.g., D6-2 rolling a 1 gives -1). Treat any such result as **0 attacks** — the model simply does not strike that phase. Represents a flailing creature that occasionally flops around doing nothing.

> **Design note — variance:** rolling per unit rather than per model is a deliberate trade-off for table-speed and simplicity, but produces high swing (a 5-troll unit at D6 Attacks ranges from 5 total attacks to 30 total attacks on a single D6). If playtesting shows this is too unwieldy, the rule may be revised to per-model rolling.

### Defence

#### Armour Save Stacking

A model's Armour Save combines contributions from its worn armour, shields, barding, and any Natural Armour. Base armour tiers:

| Tier | Save |
|------|------|
| Light armour | 6+ |
| Medium armour | 5+ |
| Heavy armour | 4+ |
| Full plate | 3+ |

Additional modifier sources improve the save by one step:

- **Shield (Light):** +0 step (no save bonus, but +1 Parry — see Shield Class below)
- **Shield (Medium):** +1 step (and +1 Parry)
- **Shield (Heavy):** +1 step (no Parry contribution; +1 to incoming-ranged save)
- **Barding** (mounts): +1 step

The best base armour source (worn armour or Natural Armour, whichever is better) determines the starting value. Each additional armour source — base or modifier — improves the save by one step. The final Armour Save is capped at **2+** — there is always a chance of rolling a 1 as a failure.

Examples: Heavy armour + Medium Shield = 3+; Heavy armour + Medium Shield + Natural Armour 6+ = 2+ (cap); Light armour alone = 6+; Light armour + Medium Shield = 5+; Light armour + Light Shield = 6+ (no save bonus from Light Shield, but the wielder gains +1 Parry); Light armour + Heavy Shield = 5+ (also +1 vs incoming ranged attacks).

#### Shield Class

Shields come in three classes, each with a different defensive role across save / Parry / ranged-protection:

| Shield Class | Armour Save contribution | Parry contribution | Vs Ranged |
|--------------|--------------------------|---------------------|-----------|
| **Light Shield** | +0 step | +1 (to Parry computation, see Parry rule) | — |
| **Medium Shield** | +1 step | +1 (to Parry computation) | — |
| **Heavy Shield** | +1 step | +0 | +1 to save vs ranged attacks |

**Class assignment** is per-unit per-equipment-line — a unit's "Shield" reference in its profile or equipment options must specify Light / Medium / Heavy. Default unspecified is **Medium** (workhorse infantry shield). Light shields are typically bucklers / off-hand small shields; Medium shields are standard infantry round/square shields; Heavy shields are kite/tower/full-coverage shields used by heavy cavalry and dedicated shield-bearer infantry.

**Roster baseline reference** (for retrofit / drafting): Ogre bucklers = Light. Saurus / Skink / Empire State Troops / Bretonnian Men-at-Arms / most rank-and-file infantry = Medium. Imperial Knights / Demigryph Knights / Bretonnian Knights all vows / heavy cavalry generally = Heavy. Skeleton Warriors (rusted bucklers) = Light. Witch Elves (no shield baseline; if added, Cauldron-style buckler = Light).

#### Natural Armour (X+)

This model has an Armour Save of X+ from innate protection (scales, hide, carapace, thick fur). Natural Armour counts as a base armour source in the Armour Save stacking rule — combining with worn armour, shields, and barding to produce the final save. Natural Armour is **not considered worn armour** for rule-interaction purposes: restrictions on worn armour (such as "wizards may not wear heavy armour") do not apply to Natural Armour.

#### Ward Save Stacking

A unit may accumulate multiple sources of ward save. The **best single source** determines the base ward value — this may be as good as 2+ or 3+ from a sufficiently powerful source. Each **additional source** improves the effective ward by one step (e.g., 6+ → 5+), but stacking cannot improve a ward beyond **4+**. If the best single source is already 4+ or better, additional stacking sources contribute nothing.

Examples: 6+ alone = 6+; 6+ + 6+ = 5+; 6+ + 6+ + 6+ = 4+ (cap); 5+ + 6+ = 4+ (cap); 3+ + 5+ = 3+ (single source beats cap); 2+ alone = 2+.

#### Regeneration (X+)

This unit has an X+ ward save representing natural healing, supernatural resilience, or magical protection of the flesh. Regeneration is **negated by Flaming attacks** — a wound from a Flaming attack skips the Regeneration save entirely (other ward sources still apply). Regeneration wards stack with other ward sources under the normal ward stacking rules.

#### Magic Resistance (X)

Enemy spells that **target or affect** this unit suffer **-X to the casting roll**. The reduced result is used for both the casting-value check (determining whether the spell is cast at all) and any subsequent dispel attempts (the lower result is easier to beat). The penalty applies to any spell the unit is a target or affected unit of, whether the spell names the unit directly or catches it in an area effect. If multiple units with Magic Resistance are targets or affected units of the same cast, apply the **highest single X** — Magic Resistance does not stack across units.

#### Ward vs Spells (X+)

This unit has an X+ ward save against wounds caused by spells. Stacks with other wards under the normal ward stacking rules.

#### Elven Grace

A model with this rule has a **Ward (6+) in melee** against attacks made at the model's own Initiative **or lower**. Attacks made by models with strictly higher Initiative than the elf are not affected — they land faster than the elf can react, and Elven Grace does not apply. Iconic elven reflex: elves *are* harder to hit, but only so long as nothing strikes faster.

Faction-wide for **Asur** (High Elves) and **Druchii** (Dark Elves); also for **Asrai** (Wood Elves) once that faction is drafted, per §13 *Elves*. Melee only — Elven Grace does not protect against ranged attacks, magic, or template effects.

**Stacking note:** Elven Grace is a Ward Save and follows the Ward Save Stacking rules above. A model that already carries another Ward source improves by one step from Elven Grace's 6+ contribution, up to the standard 4+ cap.

**Mount and rider interaction:** Elven Grace applies to all melee hits resolved against a model containing an elf — whether the model itself is an elf, or carries an elf rider. Mirrors the Parry / Dodge convention (per §1 *Combined Wounds*): rider-level identity rules apply to the combined wound pool of the rider-and-mount model. The rule does **not** extend to non-elf characters that subsequently attach to an elf unit — rules attach per-model, not by unit-association.

#### Parry (X)

A model-level rule, **equipment-conditional**. Parry grants **+X to the model's MD** in melee combat (no effect on ranged attacks — you can't parry an arrow in flight).

**Parry value computation:** the final Parry(X) is the sum of the model's **weapon-type baseline** plus its **shield contribution**:

| Weapon-type keyword | Baseline Parry |
|---------------------|----------------|
| **1H Blade** | 1 |
| **1H Reach** | 0 |
| **1H Lance** | 0 |
| **2H** | 0 |
| **Paired** | 1 (each blade defends with the other) |
| **Natural** | 0 |

Plus the wielded shield's contribution (per Shield Class table above):
- **Light Shield:** +1 Parry
- **Medium Shield:** +1 Parry
- **Heavy Shield:** +0 Parry

**Examples:** Empire Halberdier (1H Reach + Medium Shield) → Parry baseline 0 + 1 = **Parry(1)**, gaining +1 MD in melee. Saurus Warrior (1H Blade + Medium Shield) → Parry 1 + 1 = **Parry(2)**, +2 MD. Imperial Knight (1H Lance + Heavy Shield) → Parry 0 + 0 = **Parry(0)**, no melee defensive bonus from kit (relies on heavy armour and W). Witch Elf (Paired hand weapons) → Parry 1, no shield contribution = **Parry(1)**, +1 MD from the second blade.

**Multi-weapon resolution:** the model's currently-wielded melee weapon determines the weapon-type baseline. Natural attacks (Saurus Jaws, Vampire Bite, Demigryph Claws-and-Beak) **do not override or modify** the weapon-derived value — they're additional attack profiles, not replacement weapons. Riders with mount attacks: the rider's loadout determines Parry; the mount has no Parry of its own. The single combined wound pool (per §1 *Combined Wounds*) means the +X MD bonus applies to all incoming melee hits regardless of which "side" of the model would logically take them.

**Front-arc only.** Parry does not apply against melee attacks from the model's flank or rear (you can't parry what you can't see). The attacker resolves at +0 MD modifier from this rule when attacking from a flank or rear arc.

#### Dodge (X)

A model-level rule that grants **+X to the model's MD** in melee combat. Dodge represents agile evasion at close quarters: slipping aside from a sword swing rather than parrying it. **Melee only** — arrows and bolts travel too fast to physically evade once fired; ranged protection lives in Skirmisher / cover / camouflage rules, not Dodge.

**Front-arc only.** Dodge does not apply against melee attacks from the model's flank or rear (no warning, no time to move).

**Stacks with Parry.** A model with both Parry(X) and Dodge(Y) applies **+X+Y total to MD** in melee. Independent contributions — one is weapon-and-shield work, the other is reflex.

**Typical values:** Dodge(1) for naturally agile units (Skink Skirmishers, Witch Elves' bare-flesh acrobatics if granted by identity rule); Dodge(2) for elite-tier evasion specialists. Most units have no Dodge.

A model may have both if thematic (a duelist with both blade-work and agility).

### Movement and Positioning

#### Skirmishers

Represents dispersed, loose-order troops trained to fight independently rather than in close ranks. Skirmishers are *the* specialist mobile unit-class — light infantry, hunting parties, scout-pickets — and the speed bump that used to be granted by the generic Loose state lives here instead, as their unit-class signature.

- **Coherency 2"** instead of the default 1"
- **+1 Movement** — base Movement is increased by 1 inch for all movement actions (Advance, March, Charge baseline). The skirmishing identity expresses through sustained pace, distinct from generic Loose-state rules; this bonus is what marks the Skirmisher specialist tier
- **Fire on the move** — may shoot in the same turn it has marched, ignoring the normal prohibition on shooting after marching. No to-hit bonus or penalty; simply the action is permitted
- **Free pivots** — models may pivot freely at any point during their move, not only at the end. Not subject to the base-contact-prevents-pivot rule
- **Cannot Form** — Skirmisher units never enter the Formed state. Even if the arrangement satisfies Formed requirements geometrically, the unit is treated as Loose (or Disordered if neither state's requirements are met). Skirmishers fundamentally don't fight in close-order discipline; the rule lock matches the lore

#### Aquatic

This unit ignores movement penalties from water terrain (shallows, streams, marsh) — for all movement including charges. Does not protect against effects layered onto water from external sources (haunted waters, magical currents). Thematically: this unit is amphibious, webbed, or otherwise at home in aquatic environments.

#### Elusive

When this unit is charged, before the charger rolls charge distance, the Elusive unit may make a **2" reactive move directly away from the charger**. Models may not pivot or change facing during this move — they are scrambling backward, not reorienting. If the charge can no longer reach after the reactive move, the charge fails. The reactive move is limited to whatever distance is legal (blocked by friendly units, impassable terrain, or board edges). Usable **once per turn**.

#### Strider (X)

Where X is a terrain type (e.g., Forest, Rocky, Difficult). Models with Strider ignore the terrain's **inherent effects** — movement penalties, and Dangerous Terrain tests arising from the terrain's natural features. Applies to all movement including charges. Does not negate effects layered onto terrain from external sources (haunted woods, magical quagmires) — those are supernatural threats that familiarity with the landscape does not address.

#### Wall-crawler

The model or unit ignores all Movement penalties from **Difficult Terrain** and **Dangerous Terrain** (no Dangerous Terrain test required), and may move over **impassable-but-vertical features** (cliffs, walls, sheer rock faces) as if they were open ground — the unit literally crawls across the surface. The model or unit **cannot end its movement** inside another model, inside **impassable-horizontal terrain** (water, lava, void), or in any space where it could not legally be deployed.

Equivalent to **Strider (any terrain)** with the additional clause for vertical impassable features. Distinct from **Fly** (which ignores intervening models and all terrain types including horizontal-impassable, and may freely end movement at any legal flying-eligible position).

**Applies to:** Forest Goblin Arachnarok Spider, Forest Goblin Spider Riders (and any future spider-mounted unit). Cross-faction precedent: Forest Goblin spider-cult biology.

#### Chameleon

Enemy ranged attacks targeting this unit suffer **-1 to hit**. While this unit has at least one model in base contact with a Forest, Jungle, Swamp, or dense-cover terrain feature, the penalty is **-2 to hit** instead. The unit's colouration and posture shift to match its surroundings — Skinks of the chameleon-caste are nearly impossible to spot against the canopy or in broken cover, and hard even in the open.

#### Fly (X")

Where X is the flight movement characteristic in inches. A unit with Fly may, during its Movement phase, move using X" instead of its normal M value. A Flying move:

- Ignores all terrain (may pass over forests, water, walls, impassable terrain)
- Ignores intervening models, friendly or enemy, provided the unit ends in a legal position (coherency, separation, not overlapping an enemy base)
- Still requires line of sight for charge declarations — you cannot Fly through a mountain to a target you cannot see over it
- Still obeys board edges
- May be used for Advance, March, or Charge actions. A Flying charge uses X + D6 (Formed) or X + 2D6 (Loose), consistent with the standard charge formula but substituting X for M

A unit with Fly may choose each activation whether to Fly or to move normally at M. Impact weapons still trigger on successful Flying charges — velocity and mass are undiminished by lift.

Fly itself governs only movement. Multi-model flying units (squadrons, flocks) are not automatically treated as Skirmishers or Loose — that treatment is a separate unit-level design choice, not inherent to the keyword.

#### Swiftstride

When this unit rolls its charge distance, it rolls **one additional D6 and discards the lowest** before adding the result to M.

- **Formed charger:** rolls 2D6, keeps the higher. Charge distance = M + (higher die).
- **Loose charger:** rolls 3D6, keeps the higher two. Charge distance = M + (sum of the higher two).

Swiftstride adds roughly +1" average to charge distance and sharply reduces the chance of a catastrophically low roll — fast units reach charge range reliably. Failed charges (where the total still falls short of the target) resolve normally, with the unit making a standard advance instead.

Swiftstride applies only to charge rolls. Flee in this system is a deterministic move, not a dice roll, so the rule has no effect on it. Pursuit (per §4 *Pursuit*) is a D3/D6 reaction roll, but Swiftstride does not apply to it either — Swiftstride is a charge-mobility upgrade, not a generic dice-roll modifier.

#### Chariot

A unit-type identifier for wheeled vehicles pulled by mounts, with a Crew on the platform. Chariots are Mixed Units (per §1 Crew-pattern, with a chariot-specific stat-routing variant — see individual unit profiles). A unit with the Chariot keyword carries the following rules:

- **Cannot March** in Difficult Terrain or Dangerous Terrain. The chariot's wheels are not designed for off-road tracks. When entering or traversing Difficult Terrain, the unit moves at half its normal M; when entering Dangerous Terrain, the unit takes a Dangerous Terrain test (per §6.5) and may take wounds on a failed roll.
- **Flank / Rear Charge Vulnerability** — when this unit is charged in the **flank or rear arc**, the charging unit gains **+1 to its melee combat resolution score** for that combat round, on top of standard flank/rear bonuses. The chariot is designed to face forward; its sides and back are exposed.

**Stat-routing convention (chariot-specific Crew-pattern variant):** Chariot units route their stats across the Primary (chariot frame), Crew, and Mount profiles distinctly from the standard §1 Crew-pattern. The Chariot Primary carries only **T / W / Res / LiS / US** (frame durability). The Mount carries the unit's **M** (the mount pulls the chariot) plus its own MA / MD / S / I for natural-weapon attacks. The Crew carries **MA / MD / BS / S / I** for the Crew's weapon profiles AND for incoming melee defence (attackers roll to-hit against the Crew's MD). M / T / W are dashed on the supporting profiles (the chariot's durability is the unit's). Wounds go to the Chariot Primary's W pool; Crew and Mount never die individually. Composition is fixed at deployment per unit profile.

**Applies to:** Orc Boar Chariot, Goblin Wolf Chariot (and any future chariot drafts).

#### Fast Cavalry

A package rule representing light horse, swift scouts, and mobile harassers. A unit with Fast Cavalry gains all of the following:

- **Vanguard** by default (see §8) — deploys up to its M outside the deployment zone
- **Free pivots** — models may pivot freely at any point during their move, not only at the end. Not subject to the base-contact-prevents-pivot rule
- **Flee reaction** — when charged, the unit may declare **Flee** as its charge reaction instead of Stand and Shoot. It immediately makes a free move of **M + D6 directly away** from the charger. If the charger can no longer reach, the charge fails. The fleeing unit suffers **+4 stress** (or **+2 stress** if it has the **Skirmisher** keyword per §8 *Skirmisher* — evasion-coded units bear the moral cost less heavily) for the act of fleeing. The act of Fleeing does not by itself put the unit into the Broken state, but the accumulated stress contributes toward state thresholds at the **next regular threshold check** (Start of Turn, per §5) — a Flee that pushes the unit's stress past Wavering or Broken triggers that state at the check, not immediately. The unit operates normally for the remainder of the current turn and on subsequent turns subject to whatever state effects the stress eventually triggers. Coherency must be maintained — if the Flee move cannot end in a legal formation, it is limited to whatever distance is legal

Fast Cavalry and Skirmishers (Loose formation) share free-pivots by design — both are evasion-oriented archetypes. A single unit may have both if thematic (mounted skirmishers). The Flee reaction is distinct from Elusive's 2" reactive scramble; a unit could have both, using Elusive for quick sidesteps and Flee as a genuine retreat from an overwhelming charge. Fast Cavalry still pays the standard **-1 to hit for moving-and-shooting** (see §7.4) — the package confers positioning advantages, not shooting advantages.

#### Barding (mounts)

Barding is heavy fabric or metal armour fitted to a mount. A barded mount gains both an armour benefit and a movement penalty:

- **Armour Save:** +1 step (per Armour Save Stacking, §8 Defence)
- **Movement:** the mount's M is reduced by **2** for the additional weight (e.g., a Warhorse at M 10 baseline becomes M 8 when barded)

The M penalty applies to all movement — Advance, March, Charge, Flee — and is calculated from the mount's profile M before any other modifier. Negated by **Purebred Warhorse** (below) and any other rule that explicitly waives barding's M penalty.

For Rider-and-Mount profiles, the unit's effective M is the mount's M; the barding penalty therefore reduces the unit's movement directly. A character or rider profile is unaffected on foot (foot-profile M does not interact with mount barding).

#### Purebred Warhorse

A model with this special rule does **not** suffer the M penalty for being barded. Bretonnian destriers are bred and conditioned over generations to bear the weight of full barding without losing pace; common warhorses are not. The Armour Save bonus from barding still applies normally — only the M penalty is waived.

Granted to specific Bretonnian mount profiles (see §17). The rule has no effect on a mount without barding (there is no penalty to negate).

#### Random Movement (XDY)

Where XDY is a dice expression (e.g., 2D6, 3D6, D6+6) specifying how far this unit moves. A unit with Random Movement has no fixed M value. Instead, during its Movement phase:

1. The controlling player may pivot the unit once before the move — Formed units wheel; Loose or single-model units pivot freely.
2. Roll the specified dice expression. The result is the distance in inches the unit moves this turn.
3. The unit moves that distance directly forward from its new facing.

A Random Movement unit **cannot Advance, March, or Rally** in the normal sense — the roll replaces all movement actions for the turn. It **may charge**: if the rolled distance would reach an enemy unit directly in front, the movement resolves as a charge, with the rolled distance replacing the standard M + D6 charge range. A successful random charge grants the normal +1 I charge bonus and triggers Impact attacks if the unit has any.

The unit stops **1" short** of any friendly unit or impassable terrain it would otherwise contact — it lacks the discipline or awareness to handle close quarters. If it contacts an enemy unit, it stops in base contact.

A Random Movement unit never counts as Formed — it lacks the discipline to hold formation. It may be treated as Loose or Disordered based on arrangement. Most Random Movement creatures are single models in any case.

A Random Movement unit activates in the **Normal Movement sub-phase (§7.2b)**. If its rolled move brings it into contact with an enemy, it resolves as a charge at that moment (+1 I, Impact attacks trigger) — but the defender may **not** Stand and Shoot; the lurch gives no warning.

#### Scouts

This unit deploys after both armies have completed standard deployment. The scouting player chooses between two options:

- **Rear deployment:** anywhere within the unit's own deployment zone. The extra information (seeing where the enemy has committed) allows optimal positioning, but normal movement options including Turn 1 charges are retained.
- **Forward deployment:** anywhere on the battlefield more than 12" from any enemy model, outside the unit's own deployment zone. The unit may not declare a charge on Turn 1 — the forward position is already a significant advantage.

Deployment is open — both players see the final positions. *(Standard deployment framework: §9.5 Battles — Deployment, which sequences Scouts after all standard placement is complete.)*

#### Vanguard

During deployment, a unit with Vanguard may be placed **outside its own deployment zone**, up to a distance equal to its **Movement (M)** from the nearest edge of the deployment zone. Normal coherency, separation, and frontage rules apply during placement. The unit must be placed **at least 12" from any enemy model already deployed**. A Vanguard unit may not declare a charge on Turn 1 — the forward placement is already the advantage.

Vanguard units deploy during normal alternating deployment alongside the rest of the army (not after, like Scouts). The unit's M scales the forward-deploy distance — fast units (cavalry, flyers) reach genuinely advanced positions; M 4 infantry deploys only modestly forward.

A unit with **both Scouts and Vanguard** uses one or the other in any given game; their effects do not stack. The player chooses which rule applies at deployment time.

#### Ambushers

Models with Ambushers are not deployed with the rest of the army. They are held in reserve. At the start of each turn beginning with Turn 2, roll D6 for each ambushing unit:

| Turn | Arrival |
|------|---------|
| Turn 2 | 3+ |
| Turn 3 | 2+ |
| Turn 4+ | Automatic |

When arriving, the unit is placed in base contact with any board edge (including the opponent's rear) in a legal formation facing inward. It may not be placed with any enemy model within melee weapon reach, in either direction — engagement still requires a charge (per §6 *Engaging the Enemy*). The unit may move, shoot, cast, or perform any other normal action on the turn it arrives, but may not declare a charge.

If the roll succeeds but no legal space exists at the chosen edge (blocked by enemies, terrain, or other units), the attempt is wasted — the unit does not arrive this turn. It rolls again next turn under the same schedule (Turn 4+ still auto-succeeds, subject to space availability).

### Resolve and Command

#### Inspiring Presence (X")

Where X is the range in inches. Friendly units with any model within X" of this character gain all of the following:

- **+1 Res** for threshold purposes — Shaken, Wavering, and Broken thresholds each shift up by 1
- **Enables rally** — units that lack a living Leader may still rally if within range (this character acts as the Leader for rally purposes)
- **Rally in combat** — units within range may rally even while engaged in melee
- **Reroll recovery and rally rolls** — units within range may reroll their D3 recovery or rally roll and take the second result

The army general has Inspiring Presence (12") by default. Other characters, artefacts, or abilities may grant smaller-range versions. If the character is slain, the aura ends immediately — units that depended on it lose the effect.

#### Battle Standard Bearer (X")

Where X is the range in inches. Friendly units with any model within X" of this character gain:

- **+1 combat resolution**
- **+1 to recovery and rally rolls**

The army's Battle Standard Bearer has Battle Standard Bearer (12") by default. Other characters or artefacts may grant smaller-range versions. If the Battle Standard Bearer is slain, the aura ends immediately.

#### Loner

A model with Loner cannot be designated as the army general. Loner characters also cannot join units (for the character-in-unit attachment exception in §6.3) unless the unit itself also has Loner. Likewise, a non-Loner character cannot join a unit that has Loner.

Loner represents a model whose nature (aloof, feared, antisocial, magically volatile, or personally reclusive) makes them unsuitable for command and unwilling or unable to operate within a regiment. Intended as an anti-deathstar lever — preventing elite singleton models from being sheltered inside tarpit blocks, or dominating the army command structure.

#### Expendable

This unit represents tribute-troops, expendable thralls, slaves, mindless minions, or similar disposable units whose destruction is accepted as part of their role. Effects:

- **No stress spread from loss.** When an Expendable unit is destroyed or flees (by any means), the "friendly unit destroyed within 6"" and "friendly unit flees within 6"" stress triggers **do not fire** from that unit. Nearby non-Expendable friendly units suffer no stress from the Expendable unit's loss — they expected it.
- **Character composition:** Expendable characters can only join Expendable units, and non-Expendable characters cannot join Expendable units. Expendable and non-Expendable models do not mix within a single unit.

Expendable units themselves still accumulate and react to stress normally — the rule governs what others feel about *them*, not what they feel about others. A non-Expendable friendly unit destroyed within 6" of an Expendable unit still triggers stress on the Expendable unit as normal.

Expendable combines naturally with Unbreakable (slaves driven forward under the lash, goblin fodder pushed by bigger greenskins) — the two rules operate on different axes and can coexist.

### Magic

#### Loremaster (Lore)

This wizard knows all spells in the named lore, up to the tier their Lore Access permits. Loremaster replaces the normal Spells Known count for the named lore — no selection needed at list building. If the wizard has Loremaster in multiple lores, each is counted separately.

Example: A Skink Priest with **Loremaster (Heavens)** and LA 2 in Heavens knows the signature spell plus all Basic and Intermediate spells in the Heavens lore automatically. If the wizard's Heavens LA increased to 3, they would gain all Advanced spells as well.

#### Divination (X/Y)

Once per Y (typically "turn" or "game"), after any die is rolled by a unit within 12" of this model, the bearer may declare Divination. A die belongs to the unit whose models roll it — the attacker for to-hit and to-wound rolls, the defender for saves, the unit itself for tests, casting rolls, and recovery. The die is rerolled and the second result must be accepted. Applies to any die — friendly, enemy, own, or another's.

A die may only be affected by a single Divination per roll; rerolls cannot be chained across multiple Divination users.

---
