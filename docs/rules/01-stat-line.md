# §1 The Stat Line


| Stat | Abbr | Description |
|------|------|-------------|
| Movement | M | Base movement in inches |
| Weapon Skill (Attack) | WS-A | Skill at striking enemies in melee |
| Weapon Skill (Defence) | WS-D | Skill at avoiding being struck in melee |
| Ballistic Skill | BS | Ranged combat ability |
| Strength | S | Raw hitting power |
| Toughness | T | Physical resilience |
| Wounds | W | Damage each model can absorb — used freely for flavour, not locked to 1 for infantry |
| Initiative | I | Determines strike order in combat |
| Resolve | Res | Resistance to stress and morale effects |
| Line of Sight | LiS | Size/visibility for LoS calculations (see §7.4) |
| Unit Strength | US | Physical presence and mass of one model. See below |

**Note on the WS-A / WS-D split:** Weapon Skill is split into two stats — **WS-A** (the attacker's skill at landing blows) and **WS-D** (the defender's skill at avoiding them). The §3 To Hit (Melee) table compares **attacker's WS-A vs defender's WS-D**. Always display both values on a profile (e.g., `WS-A 4 / WS-D 4`) even when symmetric, so the architecture is visible. Asymmetric profiles capture lore-distinct combat archetypes — frenzied glass-cannons (high WS-A / low WS-D), evasive skirmishers (low WS-A / high WS-D), bred-warrior moderate-attacker / lower-defender (Saurus), apex predators with heavy committed motion (Carnosaur high WS-A / moderate WS-D), and so on.

**Attacks are a weapon property, not a stat.** The number of attacks a model makes is defined per-weapon on the weapon profile, not on the stat line. A model with three weapon profiles (e.g., a Monster's natural weapons plus a howdah-mounted ranged weapon) has three independent Attack values. This keeps multi-weapon units cleanly expressible and prevents double-counting across attack modes. When a weapon is used, the model makes the Attacks listed on that weapon's profile, resolved at the weapon's own S, AP, D, and any special rules.

### Armour and Protection (separate from stat line)

| Stat | Description |
|------|-------------|
| Armour Save (AS) | Base save from armour and natural scales |
| Ward Save | Unmodifiable save (magical protection, blessed, etc.) — referred to as "Ward (X+)" in body text; no abbreviation reused |

### Magical Profile (wizards only, separate from stat line)

| Stat | Abbr | Description |
|------|------|-------------|
| Cast Base | CaB | Fixed Cast Dice contributed to the wizard's personal Cast pool each Magic phase |
| Dispel Base | DiB | Fixed Dispel Dice contributed to the wizard's personal Dispel pool each Magic phase |
| Channeling | Ch | Number of D6s the wizard rolls at phase start; each result of **5+** generates one extra die, placed (player's choice) into this wizard's Cast *or* Dispel pool |
| Cast Bonus | CB | Modifier to cast rolls. Total effective CB from all sources is capped at **+5** |
| Dispel Bonus | DB | Modifier to dispel rolls. Total effective DB (lead wizard + supporter contributions + item/spell bonuses) is capped at **+5** |
| Dispel Range | DR | Maximum range at which a wizard may act as lead dispeller or contribute dice to a dispel |
| Lore Access | LA | Highest spell tier accessible, per lore |
| Spells Known | SK | **Total** number of spells the wizard knows, including all Signature spells from accessible lores plus picks made at list-building. Loremaster replaces this with "All" (the wizard knows every spell in the named lore up to their LA tier) |

See §7.3 (Magic Phase) for full rules.

### Unit Strength (US)

Unit Strength represents a model's **physical presence and mass**. It is a stat-line characteristic, independent of Wounds (which is durability) and LiS (which is visibility). Each model contributes its US to its unit — a unit's **total US** is the sum of all surviving models' US values, updated dynamically as casualties are removed.

**What US does:**

1. **Combat resolution wound totals.** Each model killed contributes its US, not 1, to the CR wound tally. A Kroxigor (US 3) killed in combat adds 3 CR wounds. A Stegadon (US 5) killed adds 5. A Saurus (US 1) adds 1.

2. **Objective and presence calculations.** Scenarios scored by "controlling an objective" or "holding a zone" count **total US** on the point, not model count. A Dragon (US 5) controls a courtyard more decisively than three Skinks (US 3) huddled on it. Physical presence scales with mass.

3. **Rule gating by scale.** Some rules gate their effects on a US threshold rather than enumerating type keywords (e.g., Flaming's beast-panic triggers on US 2+; Killing Blow can target models with US ≤ 2 for anti-infantry or US ≥ 3 for anti-large). More scalable than listing types.

**US is not tied to Wounds.** A multi-wound hero (W4 Scar-Veteran) still has US 1 — he's one bloke, however tough. A Monster with many wounds has high US because of its mass, not because of its durability.

**US and Degrading.** Monsters with the Degrading rule may have US on their damage table, decreasing as wounds are lost. A wounded Stegadon is a smaller presence than a healthy one — less imposing on the battlefield, contributes less to objectives, and its death counts for fewer CR wounds.

**Monster US = current W.** As a convention, Monster-keyword units have **US equal to their current remaining Wounds** rather than a fixed value. A full-strength Monster contributes its maximum W as US; a heavily-wounded Monster contributes proportionally less. This is a smoother version of the tier-based US-degrading pattern — the wound pool directly reads as battlefield presence. The Monster's *typical* W value governs the top-end presence; individual profiles should set LiS independently to reflect the Monster's scale irrespective of W (a Carnosaur and a Stegadon may both be W10+ but carry different LiS per their sheer physical volume).

**Characters and command US.** A character model adds **+1 US** to the typical value for its type (a foot character on an Infantry chassis starts at US 2 rather than 1; a Cavalry character at US 3; a Monster-mounted character at US 6). The army **general** adds a further **+1 US** on top, reflecting command gravity — a foot general is US 3, a mounted general US 4, a monster-mounted general US 7. These are baseline values; individual character profiles may override them for specifically thematic reasons.

### Unit Types

Each unit has exactly one **type keyword**, assigned in its profile. Unit types are categorical tags that rules reference (Flaming's beast panic, Killing Blow's target clauses, Apex Predator, Sniper allocation, etc.). They describe what kind of thing the unit is, not how it fights — type keywords do not confer mechanical benefits themselves.

| Type | Description | Typical LiS | Typical US |
|------|-------------|-------------|------------|
| **Infantry** | Standard humanoid foot troops. The default for most rank-and-file units. | 1 | 1 |
| **Cavalry** | Humanoid rider on a standard-size mount (horse, boar, wolf, Cold One). | 2 | 2 |
| **Monstrous Infantry** | Large bipedal or squat creatures fighting on foot — larger than Infantry but not Monster-scale. | 2 | 3 |
| **Monstrous Cavalry** | A larger rider or a larger mount — between Cavalry and Monster in scale. | 3 | 3 |
| **Warbeast** | Non-ridden pack animals, lone beasts below Monster scale, or domesticated combat animals. | 2 | 2 |
| **Monster** | Enormous single-model creatures. Dragons, Carnosaurs, Giants, Stegadons. | 4+ | 5 |
| **Chariot** | Riders on a wheeled vehicle drawn by beasts. | 3 | 3 |
| **Swarm** | A mass of small creatures fighting as a single unit — rats, bats, spiders, insects. Individually small but numerous; low to the ground. | 0 | 5 |

**One type per unit.** If mounted, the mount determines the unit type — Skinks on Cold Ones are Cavalry even though the riders are Skink-sized. Mixed combinations (e.g., a character and their mount counting separately) are not permitted at the unit level.

**Type vs LiS are independent.** The "typical" LiS column is guidance, not binding. A small but monstrous creature may be tagged Monster with LiS 2 if thematic; an unusually large humanoid may be tagged Infantry with LiS 2. LiS is an independent stat that rules reference alongside type keywords.

**Swarms are a special case.** A Swarm base's **US is dynamic** — equal to its **current remaining Wounds**, not a fixed value. As the swarm takes damage its mass on objectives diminishes in real time; a full-strength base contributes full US, a heavily-wounded base contributes little. The "Typical US 5" entry in the table above is indicative only for a rough mid-strength swarm base. Individual swarm profiles may also tie other stats to remaining Wounds (e.g., Attacks), but US is the type-wide default.

### Rider and Mount Profiles

Units whose models consist of a rider and a mount (Cavalry, Monstrous Cavalry, Chariot, Monster-mounted characters) display **two profiles** on their unit card — one for the rider and one for the mount. Rider and mount are a **single model for all game purposes** — there is no demounting, no rider-killed-mount-survives outcome, no mount-killed-rider-on-foot outcome. The whole model lives or dies as one entity.

| When resolving... | Cavalry / Monstrous Cavalry | Monster-mount |
|-------------------|------------------------------|---------------|
| **Movement** | Mount's M | Mount's M |
| **An attack the model makes** | Profile of the part attacking — rider's WS-A / S / I / A for rider's weapons, mount's for mount attacks. Each strikes at its own Initiative step | Same |
| **To-hit roll against the model** | Highest WS-D of rider or mount | **Mount's WS-D only** — the rider cannot interpose against attacks aimed at a body that dwarfs him |
| **To-wound roll against the model** | Highest T of rider or mount | Same |
| **Wounds** | See *Combined Wounds* below | Same |
| **Armour Save** | See *Combined Save — Cavalry / Monstrous Cavalry* below | See *Combined Save — Monster-mount* below |
| **Resolve and stress** | Rider's Res; stress tracked at unit level | Same |
| **LiS, US** | Listed at unit-level entry | Same |

**Combined Save — Cavalry / Monstrous Cavalry.** Take the **highest** base armour save of rider or mount (whichever profile's Natural Armour or worn armour is best). Stack additional sources — shield, barding, save-modifying magic items — per §8 *Armour Save Stacking*. Final save capped at 2+ per §8.

**Combined Save — Monster-mount.** The mount's Natural Armour is the model's base save. The rider's defensive layer contributes via a conversion rule: compute the rider's effective save **as if the rider were on foot** (NA + worn armour + shield + magic items, stacked per §8), then count steps from "no save":

| Rider effective save | Steps |
|---|---|
| No save | 0 |
| 6+ | 1 |
| 5+ | 2 |
| 4+ | 3 |
| 3+ | 4 |
| 2+ | 5 |

Every **two rider steps** add **one step** to the mount's NA. Round down. Final save capped at 2+ per §8.

The lore principle: the mount's bulk dominates the model's silhouette, so the rider's defensive layer operates at half effectiveness — half of what protects them on foot translates to the mounted profile.

**Defensive equipment beyond armour save.** Even where rider gear doesn't translate fully into save value (Monster-mount tier especially), it still contributes:
- **Shield Parry** (per §8) applies to the model's melee defence
- **Heavy Shield's +1 vs ranged** still applies
- **Dodge** and other WS-D buffs on the rider apply to the model's WS-D when attacks are resolved against it

**Combined Wounds (uniform across all mounted tiers).** Take the **higher** W of rider or mount as the base. The **other** profile contributes via a 2:1 conversion (round down):

| Other profile's W | Steps added to base |
|---|---|
| 1 | +0 |
| 2-3 | +1 |
| 4-5 | +2 |
| 6-7 | +3 |
| 8-9 | +4 |

(Equivalently: other W ÷ 2, round down.)

Examples:
- Imperial Knight (rider W1, Warhorse W1) → max(1,1) = 1, plus 1÷2 = 0 → **W1**
- Aggradon Lancer (rider W3, Aggradon W4) → max(3,4) = 4, plus 3÷2 = 1 → **W5**
- Saurus Oldblood (W7) on Carnosaur (W10) → max(7,10) = 10, plus 7÷2 = 3 → **W13**
- Bretonnian Lord (W5) on Royal Pegasus (W3) → max(5,3) = 5, plus 3÷2 = 1 → **W6**

**Floor:** the model's W can never be lower than the rider's foot W. Mounting up never *reduces* durability — the rider's biology comes with him. This floor is automatic when "higher of either" is the base; the explicit clause is documentation.

The lore principle parallels the armour rule: the mount occupies most of the model's silhouette, but the rider's body still absorbs some hits. Half-effectiveness is the geometric expression of "rider is part of, but not all of, the model."

**Wound pool and casualty resolution.** Wounds inflicted on the model deplete the combined wound pool computed above. When it reaches zero, the entire model — rider and mount together — is removed as a single casualty. Rules that nominally target "the rider" or "the mount" alone resolve against the model's combined wound pool; there are no separate-tracking exceptions.

### Unit Keywords

Every unit profile carries a **keyword line** — a list of tags that identify the unit for the purpose of rules that target categories of units rather than specific profiles. Keywords let effects say "any Saurus unit" or "any Core unit" or "any Monster" without listing every profile that qualifies.

**Keyword categories:**

| Category | Examples |
|----------|----------|
| **Faction** | Lizardmen (Seraphon is an AoS-specific alias; "Lizardmen" is the canonical faction keyword) |
| **Sub-faction / race** | Saurus, Skink, Kroxigor, Slann |
| **Unit type** | Infantry, Cavalry, Monstrous Infantry, Monstrous Cavalry, Warbeast, Monster, Chariot, Swarm (matches the Unit Types table above — every unit carries its type keyword here as well) |
| **Role** | Core, Special, Rare, Hero, Lord (army-composition categories for list building) |
| **Descriptive** | Situational tags for narrow rule hooks — e.g., Aquatic, Mounted, etc. — added to profiles that need them |

A typical keyword line for a Saurus Warriors unit: `Lizardmen, Saurus, Infantry, Core`.

**Effects reference keywords directly.** A spell text reading "all friendly Lizardmen units within 12" gain +1 to hit" applies to any friendly unit with the Lizardmen keyword — including characters, core, rare, monsters, etc., as long as they share the faction tag. Weapon text reading "damage 2 against Cavalry" applies to any target with the Cavalry keyword, regardless of faction.

Keywords are **static** — printed on the profile, not gained or lost in play — unless a rule explicitly adds or removes one (e.g., a transformation spell that temporarily grants Monster).

### Mixed Unit

A unit whose composition includes models of two or more distinct profiles — e.g., a Warbeast accompanied by a fixed pool of Handler support models, a crew-served weapon with its Crew, a Chariot with a Rider and a Driver. Both profiles appear on the unit card; each model uses its own profile when attacking or being attacked.

**Wound allocation.** Wounds inflicted on a Mixed Unit are applied to the **supporting profile** (Handlers, Crew, etc.) first. Only once all supporting models are removed may wounds be allocated to the **primary profile**. Rules that specifically target a named model or profile (Sniper, Precision Strike, "pick a model" effects) bypass this priority and apply per the targeting rule's own text.

**Movement and coherency.** All models move together as a single unit. The **primary profile sets the unit's M** (slowest-moves-all is the convention). Supporting models must remain within **2"** of a primary model at the end of any move; a supporting model isolated from all primary models is removed as a casualty.

**If all primary models are destroyed**, any remaining supporting models are also removed and the unit is destroyed. Supporting models cannot outlive their primaries.

Individual unit profiles specify the composition — typically a fixed ratio of support-to-primary (e.g. "3 Handlers per Beast"). Fixed ratios are locked at deployment and cannot be adjusted in play, unlike regular unit sizes.

---

## 1.5. Species Identities

> **Design reference, not strict inheritance.** This section catalogues the species that populate the rules system — what each one *is* biologically, how a "typical" rank-and-file unit of that species looks, and what the species *cannot easily express*. It is a guideline for adjusting existing units and a contract for drafting new ones, not a strict rule package — individual unit profiles may deviate when lore demands, but deviations should be lore-justified rather than arbitrary.
>
> Phase 1 covers the Lizardmen sub-castes (Saurus, Skink, Kroxigor, Slann, Saurian Beasts). Phase 2 covers Humans (Empire / Bretonnia mortal-baseline) and Ogres. Phase 3 covers the §18 cross-faction species — Orcs, Goblins, Snotlings, Elves (Asur + Druchii), Wood Elves (Asrai + Forest Spirits), Dwarfs, Chaos Warriors, Beastmen, Daemons, Vampire Counts, Tomb Kings, Skaven. Minor / deeply-deferred species (Halflings, Norsca / Northmen tribes, Kislev, Cathay / Nippon / Araby, Fimir) are not currently catalogued; they may receive entries when those rosters are drafted.

### Saurus

> Spawn-bred apex predators of the Lizardmen — engineered by the Old Ones for war, hatched as adult fighters. Six-to-eight feet tall, broad-muscled, scales hardening with age. Lifespan effectively unbounded; older Saurus unlock latent strategic knowledge implanted at hatching. Cold, methodical predator-warriors who register no emotion save savagery. Crocodilian features — jaws "that crush steel", muscular tails, scaly hide.

**Typical baseline** — rank-and-file Saurus Warrior:

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 4 | 4 | 3 | 0 | 4 | 4 | 3 | 2 | 2 | 10 | 5+ |

**Common traits** (typical, not universal):
- **Cold-Blooded** (faction-wide)
- **Stubborn** (Saurus species)
- **Predatory Fighter** (apex-predator biology)
- **Fear** (the cohort's silent advance unsettles living foes)
- **Locked Jaws** (death-bite when removed in Combat phase)
- **Tail Sweep** (foot Saurus, rear-arc only — disabled when mounted on Cavalry / Monstrous Cav / Monster mounts per cavalry geometry)
- **Saurus Jaws** as natural attack baseline

**Biologically constrained:**
- No magical biology (that's Slann territory)
- No flight (no anatomy for it)
- Rank-and-file Saurus stay around W3; Hero-tier reaches W6-7, Lord-tier W7-10. Going beyond requires specific lore (Gor-Rok's oversized frame, Sunblood's celestial form)
- Cannot bear heavy armour without lore reason — Saurus naturally rely on scaly NA + light armour at most
- Cannot wield ranged weapons effectively (no missile-tier biology — Skink-caste owns that)

**Variants of note:**
- Saurus Warriors (W3, NA 5+) — baseline rank-and-file
- Temple Guard (W3, NA 4+, WS 5/5, Sworn Protectors) — sacred bodyguards, thicker scales
- Crested Saurus (Aggradon Lancer rider — W3, baseline)
- Saurus Scar-Veteran (Hero, W6, NA 4+, WS 6/6)
- Sunblood (Hero, W7, NA 4+, Ward 6+) — celestial-form variant
- Saurus Astrolith Bearer (Hero, W4, NA 5+, BSB carrier)
- Saurus Oldblood (Lord, W8, NA 3+, WS 7/7, Primeval Command)
- Gor-Rok (named Hero, W10, NA 3+, oversized albino)
- Chakax (named Hero, W6, NA 4+, Temple Guard apex)
- Kroq-Gar (named Lord, W8 + Tlanxla spawning WS-A 8)

### Skink

> Small, quick, cunning Lizardmen. Three to four feet tall, slender, scaly, jungle-trained. Multiple sub-castes: rank-and-file Skink, Skirmisher hunters, Chameleon (apex-camouflage caste), Skink Brave (elite riders), Great Crested (disciplined drilled variant), Priest / Oracle / Starseer (psychic and divinatory castes). Communication via clicks, chirps, and crest-color shifts. Telescopic eyes (most pronounced in chameleon-caste). Pit-venom production for Poisoned Attacks weapons. Webbed feet — at home in waterways.

**Typical baseline** — rank-and-file Skink Cohort:

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 6 | 3 | 3 | 3 | 3 | 2 | 1 | 4 | 1 | 6 | 6+ |

**Common traits** (typical, not universal):
- **Cold-Blooded** (faction-wide)
- **Aquatic** (most Skink units; exceptions are flyer-mounted variants)
- **Skittish** (faster to break — biological nervousness)
- **WS-A < WS-D asymmetry** on the **Skirmisher / stalker / Chameleon caste** — slippery profile, poor melee skill, hard to pin down. **Cohort-caste Skinks** (drilled rank-and-file in Formed regiments) instead carry **symmetric WS-A = WS-D** baseline — the discipline of standing in line is its own combat rhythm, distinct from the evader-asymmetry of skirmishing kin
- **Pit-venom biology** (Poisoned Attacks on Skink-default ranged weapons; Jungle Poisons upgrade extends this to melee for some variants)

**Biologically constrained:**
- No biting / jaws-as-weapon (small, designed for chirps and venom-delivery, not crushing prey)
- No tail-as-weapon (small tails for balance, not striking)
- No high T or W — biology is small-and-quick, not tough-and-heavy
- Skink rank-and-file should not exceed W1; Hero-tier Skink characters cap at W3-4
- Cannot bear heavy armour effectively (small frame, encumbrance)
- No melee force-multiplier rules without specific lore (no Predatory Fighter, no Locked Jaws, no Stubborn) — Skinks are *evasion*, not *combat*

**Variants of note:**
- Skink Cohort (W1, baseline rank-and-file, formed-capable)
- Skink Skirmishers (W1, Skirmisher, WS 2/4, Elusive)
- Chameleon Skinks (W1, Chameleon, Sniper, Scouts, Dartpipe)
- Skink Brave (mounted variants, often Res 7 elevation)
- Great Crested Skink (Horned One Riders, Res 6, more disciplined)
- Skink Chief (Hero, W3, command + scout)
- Skink High Chief (Lord, W4, Strategist of the Skink-caste)
- Skink Priest / High Priest / Starseer (Hero/Lord, W3, Wizard tiers)
- Chameleon Stalker (Hero, W3, sniper-caste apex)
- Tehenhauin (named Hero, W3, Prophet of Sotek)
- Oxyotl (named Hero, W4, Realm-of-Chaos veteran)
- Tetto'eko (named Lord, W3, palanquin-borne astromancer)
- Tiktaq'to (named Hero, W3, Master of Skies)

### Kroxigor

> Massive, dim-witted, muscle-bound Saurus-kin. Twelve-plus feet tall — "two stories tall" — with scales thicker than emperor's-bodyguard armour and jaws built for tearing flesh from bone. Lore-canonical "twenty-three crossbow bolts to fell a single specimen." Amphibious; emerges silent from swamp, waterhole, river-bend. Dim-witted — without Skink handlers within reach, Kroxigor lumber Stupidly toward the nearest threat. Wield weapons taller than a Saurus Warrior in wide arcs that "splatter a man-sized creature beyond all recognition."

**Typical baseline** — rank-and-file Kroxigor:

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 6 | 3 | 2 | 0 | 5 | 5 | 8 | 2 | (on weapon) | 7 | 4+ |

**Common traits** (typical, not universal):
- **Cold-Blooded** (faction-wide)
- **Aquatic** (amphibious biology)
- **Predatory Fighter** (Saurus-kin)
- **Locked Jaws** (death-bite — Kroxigor variant deals D D3 damage per the larger crocodilian frame)
- **Saurus Jaws (Kroxigor scale)** natural attack — multi-wound bite
- **Tail Club** (rear-arc, foot only) — heavy weaponized tail
- **Stupidity-when-isolated** (without Skink handlers within 6")

**Biologically constrained:**
- Cannot wield small / human-scale weapons effectively (massive hands; Kroxigor weapons are great-club / great-weapon scale exclusively)
- Cannot be Skink-quick — too massive for high I (cap at I 2-3)
- Cannot bear ranged weapons (no missile-tier biology; ancient Kroxigor with magical weapons might in named-character cases)
- Lacks the tactical-cognition of Saurus-tier Lord characters — even the Kroxigor Ancient is a brute apex, not a strategist
- WS-D capped low (2-3) — *easy to hit but hard to actually hurt* is the species fingerprint

**Variants of note:**
- Kroxigor (W8, NA 4+) — baseline Monstrous Infantry
- Kroxigor Warspawn (W8, lone-wolf variant)
- Kroxigor Ancient (Hero, W10, NA 3+, "iron-hard scales")
- Nakai (named Lord, W12, NA 2+, Mark of the Old Ones intrinsic, jungle-spirit avatar)

### Slann

> Toad-form Mage-Priests of the Lizardmen — ancients of the First Spawning, palanquin-borne, telepathically projecting their will across the battlefield. Physically inert; combat is something done *at* the Slann, not by the Slann. The mind is the apex; the body is a vessel. Lifespan in millennia; the eldest Slann remember the Old Ones personally.

**Typical baseline** — Slann Mage-Priest:

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| — | 0 | 1 | 0 | 3 | 4 | 8 | 1 | (Palanquin Lightning) | 12 | — (Ward 4+ baseline) |

(M dash — palanquin-borne; movement equivalent to flight or static positioning per specific entry. NA dash — the palanquin is the model's frame; baseline Ward 4+ replaces an armour save.)

**Common traits** (typical, not universal):
- **Cold-Blooded** (faction-wide)
- **Stubborn** (the Slann does not break)
- **Mastery of All Winds** — the species-defining magical capability; access to multiple lores including Lizardmen faction lores (Geomancy, Cosmic Architecture)
- **Telepathic Projection** — Inspiring Presence at extended range (typically 24"+); Arcane Vassal (cast through any friendly Skink Priest/Oracle's position)
- **Shield of the Old Ones** — baseline Ward 4+ (or better via specific Slann)
- **Long-Lived** — Res 12 baseline, above the standard Lord cap

**Biologically constrained:**
- Cannot fight in melee personally (WS-A 0 baseline — the Slann is a passenger; the palanquin's celestite array fires independent lightning at fixed-2+ to-hit)
- Cannot equip magical weapons or armour (the "Contemplation" lore-rule)
- Cannot be transported except by palanquin — no direct mount options. **Mazdamundi is the lore-canonical exception**: his palanquin is borne *atop* Zlaaq the Ancient Stegadon, but the Slann himself never directly mounts the creature. This palanquin-on-creature configuration is rare and named-character-only; commonplace Slann are palanquin-borne via floating-stone-throne mechanics
- Slann should not appear at Hero-tier — Lord-only species; Slann are too rare and powerful for sub-Lord drafting

**Variants of note:**
- Slann Mage-Priest (W8, baseline) — generic Slann with Mastery of All Winds (3 lores)
- Lord Kroak (named Lord, W10, Relic Priest, Unbreakable, SK 10 across all lores) — apex caster, deathless husk
- Mazdamundi (named Lord, W8 rider on Zlaaq Stegadon, Loremaster Geomancy + 4 baked Disciplines) — apex *living* Slann

### Saurian Beasts (Megafauna)

> The great reptilian creatures of Lustria — predator-monsters (Carnosaur), howdah-bearers (Stegadon), apex tank-types (Bastiladon), flyer cavalry (Terradon, Ripperdactyl), ancient herd-types (Coatl, Arcanadon, Dread Saurian). Not Saurus, not Skink, not Kroxigor — but sharing the core Lizardmen reptilian biology (Cold-Blooded faction-wide). These creatures predate the Old Ones' war-spawning programs; they are the planet's pre-existing megafauna, woven into Lizardmen warfare via taming, mount-bonds, and ritual command.

**Typical baseline** — varies widely by tier; this section provides anchors:

| Tier | Typical W | Typical T | Typical NA | Examples |
|------|-----------|-----------|------------|----------|
| **Mount-class** | 1-4 | 3-5 | 5+ to 6+ | Cold One, Aggradon, Raptadon, Horned One |
| **Cavalry-class flyer** | 2-3 | 3 | 6+ | Terradon, Ripperdactyl, Coatl-mount |
| **Monstrous Cavalry mount** | 4-5 | 4-5 | 4+ to 5+ | Aggradon (heavier riders), Demigryph parallel |
| **Monster** | 10-12 | 5-7 | 2+ to 5+ | Carnosaur, Stegadon, Bastiladon, Troglodon |
| **Apex / Unique** | 12-25 | 6-7 | 2+ to 3+ | Arcanadon, Dread Saurian, Engine of the Gods |

**Common traits** (typical, not universal):
- **Cold-Blooded** (faction-wide for all Lustrian saurians)
- **Predatory Fighter** common on apex predators (Carnosaur, smaller theropods, Aggradon)
- Various unit-specific identity rules (Apex Predator, Bloodlust, Bloodroar, Pinned Prey, etc.) — see individual entries

**Biologically constrained:**
- Most Saurian beasts are not magical — no rank-and-file Wizard variants among the beast tiers. **Coatl is the lore-canonical exception** — an arcane saurian with full Wizard access (Lore of Heavens, casts spells via the Magic phase), divinatory by nature but mechanically a caster. The exception confirms the rule rather than breaking it: ordinary saurians are animal-tier; Coatl is the rare arcane-creature outlier
- Most are Aquatic-capable but not all (Terradons, Ripperdactyls are flyers — non-aquatic)
- Cannot equip worn armour beyond barding for mount profiles
- Damage-table degrade pattern is common (Stegadon, Carnosaur, Bastiladon, Arcanadon) — apex monsters lose stats as W drops; rank-and-file mounts don't
- Cognition is animal-tier (no command auras for the rank-and-file beasts); the rare intelligent saurians (Coatl) are exceptions with Wizard-tier consciousness

**Variants of note:**
- Mount profiles in Lizardmen Cavalry / Monstrous Cavalry units (§10): Aggradon, Raptadon, Horned One, Terradon, Ripperdactyl
- Standalone Monsters (§10 Rare): Stegadon, Engine of the Gods, Bastiladon, Troglodon, Ancient Salamander, Arcanadon, Coatl, Dread Saurian, Wild Carnosaur
- Character-mount Carnosaur (Saurus Oldblood / Scar-Veteran / Kroq-Gar's Grimloq)
- Special-tier ranged saurians: Salamander (template flame), Razordon (volley quills) — Mixed Unit with Skink Handlers
- Swarm-class Saurian: Jungle Swarms (Swarm-type, A=W, US=W dynamic stats)

### Humans (Mortal Baseline)

> The reference species the rules system was designed around — Empire, Bretonnia, the human contingents of mercenary Ogre forces, and most §18 cross-faction roster humans (Chaos Warriors are *corrupted* humans, treated as their own species below; Witch Elves and similar are *not* humans despite humanoid appearance). Mortal physiology, finite lifespan, no biological armour. Differentiation across human factions comes from **training, equipment, and faith** — not biology. Empire's combined-arms drilled professionalism, Bretonnia's chivalric-vow caste system, and any future mercenary humans share the underlying baseline.

**Typical baseline** — rank-and-file human soldier (Empire State Trooper):

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 4 | 3 | 3 | 3 | 3 | 3 | 1 | 3 | 1 | 9 | — |

(Res 9 reflects the cross-faction +1 calibration applied to disciplined factions per stress-system convention; baseline WAP human Res is 7, our system reads humans as Res 8-9 to absorb the stress-system's tighter thresholds. Undisciplined humans — peasants, rabble — sit at Res 6-7 instead.)

**Common traits** (typical, not universal):
- **Disciplined** (Empire State Troops, Bretonnian knights, professional soldiery)
- **Undisciplined** (Bretonnian peasants — Men-at-Arms, Longbowmen, Bidowers; Empire militia tier when drafted)
- **Faction-specific traits** — Empire's State Troops reroll-near-General; Bretonnia's Knight's Vow / Crusader's Vow / Questing Vow / Grail Vow + Blessing of the Lady; future faction additions
- **Equipment-driven differentiation** — wide weapon and armour menus; same biology, different gear

**Biologically constrained:**
- No Natural Armour — protection comes entirely from worn armour and shields
- W1 at rank-and-file; Hero-tier W3-4, Lord-tier W4-5. Going beyond requires lore (chaos-mutation, vampiric transformation, magical augmentation)
- Standard reaction speed (I 3) — no I 4+ baseline without specific training (Knight tier, Captain) or magical effect
- No species-wide combat-cascade rules (no Predatory Fighter, no Locked Jaws, no death-bite biology)
- No flight without external means (winged mount, Pegasus, magic)
- Lifespan 50-80 years — no Saurus-style centuries-of-unlocked-knowledge framing

**Variants of note:**
- Empire State Troops (Halberdiers, Handgunners, Spearmen, Swordsmen, Crossbowmen) — W1, Disciplined, drilled-daily professional
- Empire Greatswords (W1, Stubborn + Professional Soldiers — elite pro tier)
- Empire Knights (W1, heavy armour + barding chassis)
- Empire characters (Imperial General, Captain, Wizard Lord, Battle Wizard) — W3-4
- Bretonnian Men-at-Arms / Longbowmen / Bidowers (W1, Undisciplined peasant tier)
- Bretonnian Knights of the Realm / Errant / Questing / Pegasus (W1, vow-bearing chivalric tier)
- Bretonnian Lord / Paladin / Damsel / Prophetess (W4-5, Lady's Chosen casters at the apex)

### Ogres

> Massive, brutal, hungry humanoids of the Mountains of Mourn. Ten-plus feet tall, 700-800 lbs of fat-and-muscle, gut-plated, hand-to-hand brawlers. Multiple stomachs digest anything; canonically eat their kills bones-and-all. Tribal might-makes-right culture — the strongest Ogre rules. Three Lord-tier expressions: the *combat* apex (Tyrant), the *spiritual* apex (Slaughtermaster, channelling the Lore of the Great Maw), and the *enforcer* Hero (Bruiser). Limited magical depth — Ogre cosmology favours hunger and bestial savagery (Maw + Beasts) over the cosmic-scale Winds. No drilled-regiment morale tradition; Ogres are brutal, not stoic.

**Typical baseline** — rank-and-file Ogre Bull (Pass 4):

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 6 | 4 | 2 | 2 | 4 | 4 | 7 | 2 | 3 | 7 | — / 6+ gut-plate |

(NA dash — Ogres have no biological armour; the gut-plate is a strapped-on bronze chest-plate functioning as a hands-free shield-equivalent per §15.)

**Common traits** (typical, not universal):
- **Gut-plate** (faction-wide convention) — intrinsic shield-equivalent that preserves save with two-handed weapons
- **Undisciplined** at rank-and-file (Bulls); **Disciplined** at character tier (Tyrant, Bruiser, Slaughtermaster — drilled by violence rather than training)
- **Bull Charge** — most Ogres trigger Impact Hits on charge (D3 per model at S 5 AP -1; profile per unit)
- **Hand-to-hand orientation** — Ogres are melee specialists by default; ranged options are limited (Maneaters, Leadbelchers when drafted)
- **Mighty Blow at apex** — Lord-tier combat dominance expresses via Mighty Blow (+1 S in first round) rather than Predatory Fighter (which is reserved to Lizardmen). Saurus apex = swarm-of-strikes; Ogre apex = single-crushing-blow

**Biologically constrained:**
- No Natural Armour — protection comes from gut-plate (intrinsic shield) and optional light armour. **No heavy armour anywhere in the Ogre roster** (5+ save ceiling) — "fat guys with little armour" is the design call
- WS-D capped low (rank-and-file WS-D 2; even Tyrant only WS-D 6) — *easy to hit but hard to actually hurt* via wounds + Toughness rather than dodge-tier defence
- I 2-4 across the species — Ogres are not quick; Mighty Blow + Headbutt land late in the strike order vs apex-Initiative opponents
- No Predatory Fighter (Lizardmen-reserved) — Ogre combat-spike rules use Mighty Blow / Bone Crackers / Bull Charge / Bloodgreed instead
- Limited magic depth — only Slaughtermaster (Lord-caster) channels; Ogre lore-access is dual (Great Maw + Beasts) but no ladder of caster tiers below Slaughtermaster
- No flight, no aquatic specialisation, no Cold-Blooded biology
- Inspiring Presence and similar morale auras are **not Ogre identity** — authority is established through dominance and threat, not charisma. Tyrant's "no Fall Back within 12"" is positional enforcement, not Res buff

**Variants of note (Pass 4 W ladder):**
- Ogre Bulls (W7, baseline rank-and-file Monstrous Infantry)
- Ironguts (W7, elite Special — light armour, Bone Crackers, mandatory great weapons)
- Bruiser (Hero, W9, Bully — unit-attached charge buff, traditional BSB carrier)
- Slaughtermaster (Lord caster, W10, dual-lore Maw+Beasts intrinsic, Bloodgreed)
- Tyrant (Lord combat apex, W12, Mighty Blow + Headbutt + No-Fall-Back-within-12")
- *Pending drafts:* Maneaters, Leadbelchers, Yhetees, Mournfangs, Stonehorn / Thundertusk mounts, Gnoblar contingents

### Orcs

> The warrior caste of the Greenskin race — large, brutal, aggressive humanoids spawned from fungal spores and grown to ~6 ft tall, broad-muscled, perpetually itching for a fight. Common Orcs are physically similar to Saurus and Chaos Warriors in size; the larger Big'Uns and Black Orcs scale up further. Fungal physiology (lore-flavour, no species-wide rule) gives them T 4 resilience and a famous pain-tolerance. Their natural state is conflict — without immediate enemies to fight, an Orc unit's aggression turns inward via Animosity. The flip side: Orcs *in* melee thrive on it. Brawling is what they're for.

**Typical baseline** — rank-and-file Common Orc (Boyz):

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 4 | 4 | 3 | 3 | 4 | 4 | 2 | 2 | 1 | 7 | — |

(W 2 reflects fungal-pain-tolerance — Orcs at the rank-and-file tier already exceed mortal humans on durability per the Pass 4 species-identity scaling. WS-A 4 / WS-D 3 captures the hit-hard-but-telegraphed combat profile — Orcs swing hard, register hits poorly. Res 7 unchanged from WAP — Greenskins don't get the +1 disciplined-faction Res bump.)

**Common traits** (typical, not universal):
- **Animosity** (Greenskin faction-wide) — D6 each Movement phase; on a 1, the unit must charge nearest enemy or take +1 stress squabbling
- **Loves a Scrap** (Greenskin faction-wide for Orcs specifically) — bleeds 1 stress per Combat phase the unit was engaged; melee is morale-positive
- **Undisciplined** (Common Orcs and most rank-and-file Greenskins; -1 to Recovery rolls). Black Orcs are the exception — Disciplined.
- **Boyz Will Be Boyz** on hand-weapon-only Boyz (charge-bonus +1 attack)
- **WS-A > WS-D** asymmetry — Orcs swing harder than they parry, by typically one step

**Biologically constrained:**
- No Natural Armour — protection from worn armour and shields only
- WS-D tends to lag WS-A — Orcs are not parry-fighters; the design call is "swing hard, get hit hard"
- I 2 baseline — Orcs are not quick. Apex Black Orcs may reach I 3, never higher
- Heavy armour reserved for elite tier (Black Orcs); rank-and-file Boyz cap at light armour + shield
- No species-wide morale-aura abilities — Greenskins are individualistic; no Inspiring Presence baseline
- Magic surfaces only at the Shaman tier (Orc Shaman / Goblin Shaman) — no rank-and-file caster biology

**Equipment patterns:** **choppas** (the iconic Orc one-handed cleaver), **big choppas** (two-handed great-cleaver tier), light or medium armour at rank-and-file, heavy armour reserved for Black Orcs. Boar Boyz ride War Boars (Cavalry-tier mounts); Warbosses ride Wyverns (Monster-tier flying mounts).

**Magic:** **Waaagh! Magic** (the lore of conflict and brute psychic-momentum) — channelled through Orc Shamans and Goblin Shamans. The shamans don't *master* Waaagh-energy so much as *survive their attempts to channel it* — Orc Shamans risk their heads exploding if a cast goes wrong. Magic is a niche role, never a faction-anchor; rank-and-file Orcs are not casters in any way.

**Variants of note:**
- Common Orcs / Boyz (W2, baseline rank-and-file)
- Big'Uns (W3, S5 — Boyz who survived enough fights to grow; elite rank-and-file)
- Black Orcs (W3, Disciplined, heavy-armour-capable, Stubborn-leaning) — the disciplined Greenskin elite, the only Orc sub-tribe that *isn't* Undisciplined
- Savage Orcs (W2 baseline, no armour, Frenzy-leaning, war-paint-instead-of-plate)
- **Boar Boyz** (Orc cavalry on War Boars — Cavalry-tier)
- **Wyvern-mounted Warboss** (Lord-tier on Monster mount)
- **Orc Shaman / Great Shaman** (caster tier — Hero / Lord, Waaagh! Magic)
- *Pending:* Black Orc Big Boss, Warboss (foot Orc Lord)
- **Monstrous counterparts (Greenskin-allied):** **Trolls** (Monstrous Infantry-tier — large, dimwitted, regenerating, vomit corrosive acid as ranged attack), **Giants** (Monster-tier — apex Greenskin behemoth, drunken / unstable combat), **Squigs** (chaos-fungus creatures, see Goblins entry — Greenskin-shared menagerie)

### Goblins

> Small, cowardly Greenskins — three to four feet tall, scrawny, ~25-50 lbs. Where Orcs charge in and brawl, Goblins prefer to stab from behind, swarm in numbers, or simply run. Multiple sub-tribes: **Common Goblins** (open-plain skulkers), **Night Goblins** (subterranean cave-dwellers, fungus-eaters, Fanatics, Squig Hoppers), **Forest Goblins** (jungle-canopy spider-cult, Wall-crawler riders, Spider God magical lore). Faction-wide Animosity, but the Goblin manifestation is panic and squabbling rather than aggressive bloodlust. Goblins win battles through *quantity* and *positional opportunism* — outnumber, outflank, ambush, then retreat before the enemy regroups. A Goblin alone against an enemy generally runs.

**Typical baseline** — rank-and-file Common Goblin:

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 4 | 2 | 3 | 3 | 3 | 3 | 1 | 3 | 1 | 5 | — |

(WS-A 2 / WS-D 3 reflects the stab-from-behind instinct — Goblins are bad at fair fights but slippery to pin down. Res 5 — Goblins panic readily; cowardice is the species fingerprint, distinguishing them sharply from their Orcish kin.)

**Common traits** (typical, not universal):
- **Animosity** (Greenskin faction-wide) — same trigger as Orcs, but the manifestation is more often panic/squabble than bloodlust
- **Cowardly Numbers** *(species identity guideline — mechanics to be specified per unit)* — Goblins gain meaningful identity benefits in large units; when a Goblin unit drops below half starting strength, additional stress / morale penalties apply
- **Stab in the Back** *(typical for Goblin combat units — mechanics per unit)* — bonus against rear-arc targets or models already carrying stress; the cowardice manifests as opportunistic backstabbing rather than fair confrontation
- **Undisciplined** (faction-wide; -1 Recovery)
- **No Loves a Scrap** — Goblins do *not* enjoy combat; brawling drains them, doesn't refresh them. The faction-wide Greenskin trait does not apply at the Goblin sub-species level. This is the cleanest mechanical expression of "Orcs love a fight, Goblins do not"

**Biologically constrained:**
- No Natural Armour, fragile baseline (W1, T3)
- Low S (3) — Goblins struggle to wound T 4+ targets without poison, magic, or numbers
- Low Res (5-6) — easy to break; Goblins generally do not hold a line under sustained pressure
- Cannot bear heavy armour (small frame, encumbrance, cultural disinclination)
- No species-wide melee-cascade rules; Goblin combat output is volume + opportunism, not raw quality
- **Forest Goblin sub-tribe** layers Poisoned Attacks (spider-pit-venom) + Wall-crawler mount-mechanic + Spider God magical access on top of the Goblin baseline; same biology, distinct sub-tribe culture and toolkit. Forest Goblins retain the Common Goblin slippery profile (WS-A 2 / WS-D 3) — sub-tribe culture changes the *toolkit*, not the *combat-axis identity*

**Equipment patterns:** light armour at most, shield, hand weapon (short blade or club), bow (Common Goblins favour the short-bow; Forest Goblins use poisoned bows), **slings** (cheaper alternative ranged weapon). Night Goblins layer in **bound Fanatics** (chained-and-mushroom-dosed Goblins released as whirling-ball-of-death suicide weapons before contact). Spear + shield is also common at the rank-and-file tier.

**Magic:** **Waaagh! Magic** (Greenskin-shared with Orcs, channelled through Goblin Shamans). Night Goblin Shamans channel via mushroom-induced visions ("Little Waaagh!" — characteristically chaotic and mushroom-fuelled). Forest Goblin Shamans channel a **Spider God** lore (pending separate §11 drafting) — venom, web-attacks, swarm-summoning.

**Monstrous counterparts (Goblin-allied menagerie):**
- **Squigs** — chaos-fungus creatures, "part fungus, part animal," ball of tough flesh with razor teeth. Variants: **Cave Squigs** (Squig Hoppers — Goblins riding bouncing Squigs as fast cavalry), **Mangler Squigs** (giant rolling Squig of death — Monster-tier suicide weapon), **Squig Herds** (Goblin handlers driving Squig swarms)
- **Wolves** — Common Goblin Wolf Riders (light cavalry, fast harassers)
- **Giant Spiders** — Forest Goblin Spider Riders (cavalry — Wall-crawler mount-mechanic) and **Arachnarok Spiders** (apex Forest Goblin Monster — see §18 stress-test entry)
- **Trolls** (Greenskin-shared with Orcs) — also fielded by Goblin tribes, especially Night Goblins (River Trolls, Stone Trolls)

**Variants of note:**
- Common Goblins (W1, baseline rank-and-file open-plain Goblins)
- Night Goblins — sub-tribe; W1, cave-adapted, mushroom-induced Frenzy variants (Fanatics, Squig Hoppers), darkness-affinity
- Forest Goblins — sub-tribe; W1, spider-cult, Spider Rider / Arachnarok-mounted, Poisoned Attacks pervasive (jungle-pit-venom from spider biology), Spider God magical lore (faction-flavoured)
- *Pending:* Goblin Big Boss, Goblin Shaman, Forest Goblin Shaman, Night Goblin Shaman, Squig Hoppers, Spider Riders, Wolf Riders, Doom Diver Catapult crews, Mangler Squigs, Trolls (Greenskin-shared)

### Snotlings

> Tiny mushroom-creatures — barely a foot tall, half-Goblin intelligence, swarm-tier biology. Snotlings exist as servant-fodder for Goblins and Orcs; they tend fungus-gardens, carry equipment, and occasionally are organised into Pump Wagons or swarm-bases for combat use. Negligible individually; collectively a Snotling base is a slow-moving distraction. Stub entry pending faction-draft expansion.

**Typical baseline** — Snotling base (Swarm-tier):

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 4 | 2 | 2 | 0 | 2 | 2 | =W (5-7) | 3 | =W | 4 | — |

**Common traits:**
- **Animosity** (Greenskin faction-wide)
- **Swarm-type** (Dispersed Mass, A=W / US=W per §1)
- **No combat output worth mentioning** — Snotlings are board-presence, not damage-dealers

**Biologically constrained:**
- Cannot bear armour (too small)
- No magic, no specialty combat rules
- Should not appear at Hero or Lord tier

**Variants of note:** *Pending* — Snotling Pump Wagons, Snotling Swarm bases.

### Elves

> Long-lived, slim, magic-attuned humanoids. Two and a half millennia of life is typical for an elf; the eldest reach 6+ centuries. Cultural sub-factions: **High Elves** (Asur — disciplined citizen-soldiers of Ulthuan, ten-thousand-year war-tradition), **Dark Elves** (Druchii — frenzied raiders of Naggaroth, Khaine-cult bloodlust). **Wood Elves** (Asrai) are biologically identical but currently omitted from the species reference until forest-bound mechanics are drafted — the Wood Elves are a future revisit if material warrants it. Across all sub-factions, elves share the same biological baseline. Long-lifespan is *flavour* mechanically — but it surfaces indirectly through the higher-than-average WS / I baselines (centuries of compressed training), and through the M 5-6 species speed.

**Typical baseline** — disciplined-tier elf (High Elf Spearman as the baseline reference):

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 5 | 4 | 4 | 4 | 3 | 3 | 1 | 5 | 1 | 9 | — |

(M 5-6 baseline. WS / BS / I 4-5 reflects centuries of training compressed into a slim biological frame. Cultural sub-factions warp the WS-A / WS-D *axis*, not the underlying stat.)

**Common traits** (typical, not universal):
- **Elven Grace** (faction-wide for both Asur and Druchii) — Ward 6+ in melee against attacks made at the elf's Initiative or lower
- **Martial Prowess** (faction-wide for both Asur and Druchii) — reroll to-Hit 1s in melee
- **Disciplined** for High Elves (Asur), often **Frenzy** or sub-faction-specific bloodlust for Druchii Khainite units
- High WS / BS / I baselines reflecting long-lifespan training compression — elves are the *skill-and-discipline* species archetype across the ruleset
- **Cultural WS-A / WS-D asymmetry** as the across-sub-faction axis: High Elf disciplined-balanced (WS-A ≈ WS-D), Dark Elf frenzied-attacker (WS-A > WS-D), Wood Elf (pending) likely skirmisher-evader (WS-A < WS-D)

**Biologically constrained:**
- Low T / W (3 / 1) — elves are slender; biological resilience is low. Lord-tier characters cap at W4-5
- No Natural Armour — protection comes from worn armour
- Magic affinity is *cultural-level* (lots of caster characters across all sub-factions) but does not appear as a rank-and-file trait — common elves are not mages, only elf characters are
- Cannot grow large — no Monstrous Infantry-tier elves; the species-frame is fundamentally slim. Mounted variants and monster-mounted variants exceed the slim baseline only via the *mount*, not the rider
- Long-lifespan does not surface as a stat-line bump; instead it's expressed via the elevated WS / I baseline

**Equipment patterns:** elves are master craftsmen — every elf-forged weapon and armour piece is exquisite by mortal standards. **High Elves** favour spears (Lothern Sea Guard, Spearmen), longbows (every Sea Guard carries one), elite swordsmanship (Sword Masters of Hoeth wield two-handed greatswords), and ceremonial weapons (Phoenix Guard halberds). **Dark Elves** favour repeater crossbows (Dark Shards, Corsairs), paired weapons (Witch Elf knives, Corsair sea-blades), and heavy armour-and-shield (Black Guard, Cold One Knights). **Wood Elves** (pending) lean heavily on the **Glade Bow** (apex longbow tradition) and forest-camouflage.

**Magic:** elves are the most magic-attuned mortal species — both factions field Lord-tier casters as a matter of course. **High Elves** practise **High Magic** — the disciplined ordering of all eight Winds (the only mortal tradition that channels the unified Aethyr rather than individual Winds). **Dark Elves** practise **Dark Magic** — the corrupted, dangerous version of the same tradition; faster and more powerful per cast but unstable and self-damaging. **Wood Elves** (pending) channel the **Wild** of the forest (Asrai-specific lore). Magic is faction-anchor at the Lord tier across all three sub-factions.

**Monstrous counterparts:**
- **Dragons** — both High Elves and Dark Elves field Dragon-mounted Princes / Dreadlords at apex. Apex Monster mounts; lore-canonical Princes-on-Dragons are the ultimate elf battlefield commanders
- **Hydras** — Dark Elf Monster (multi-headed, regenerative, breath-weapon)
- **Cold Ones** — Dark Elf cavalry mount (cold-blooded saurian; Cold One Knights ride them, parallel to Lizardmen Aggradon mounts)
- **Cauldron of Blood** — Dark Elf Khainite altar; not strictly a monster, but a faction-anchor mobile shrine that boosts nearby Witch Elves
- **Manticores** — apex Hero / Lord mounts for both High and Dark Elf characters
- **Great Eagles** — High Elf flying mounts and skirmish-units; sentient noble birds of the Annulii Mountains
- **Treemen** (pending Wood Elf draft) — animated forest-monsters, apex Wood Elf Monster

**Variants of note:**
- High Elf Spearmen (W1, M 5, WS-A 4 / WS-D 4, Disciplined, Defensive Formation)
- Witch Elves / Druchii (W1, WS-A 5 / WS-D 3, Frenzy, Khainite-cult bloodlust — frenzied-attacker cultural axis)
- *Pending:* Sword Masters of Hoeth, Phoenix Guard, White Lions, Lothern Sea Guard, High Elf Archers, Reavers, Silver Helms / Dragon Princes (High Elf elite tiers); Black Guard, Corsairs, Cold One Knights, Dark Riders, Dark Shards, Executioners (Dark Elf tiers); Wood Elf entire roster (Wardancers, Glade Guard, Eternal Guard, Treekin, Treemen, etc.); High Elf and Dark Elf Lord/Hero characters (Princes, Anointed, Dreadlords, Sorceresses, Loremasters of Hoeth, etc.); Dragon-mounted apex characters across both factions

### Dwarfs

> Short, stocky, tough, slow. Three centuries' lifespan, master-craftsmen of the Karaz Ankor (the Dwarf realm of underground holds and mountain fastnesses). Stubborn, grudge-bearing, **naturally magic-resistant**. Where elves channel the Winds, dwarfs *deny* magic — their resistance is biological, not cultural; runic engineering and gunpowder stand in for traditional spellcraft. Every adult dwarf is drilled in axe and shield from boyhood; the cultural baseline is "warrior-craftsman", with units distinguishing themselves through equipment-tier, oath, and inheritance rather than tactical doctrine.

**Typical baseline** — rank-and-file Dwarf Warrior:

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 3 | 4 | 4 | 3 | 3 | 4 | 1 | 2 | 1 | 10 | — |

(M 3 baseline — dwarfs are slow, hard-coded into the species. T 4 / Res 10 captures the iron-stoic identity. WS 4 across the species — every adult dwarf is a trained warrior.)

**Common traits** (typical, not universal):
- **Stubborn** (faction-wide) — dwarf morale ignores Shaken / Wavering state effects
- **Ancestral Grudge** (faction-wide) — Hatred against Greenskins, Skaven, Trolls, Beastmen
- **Resolute** (faction-wide) — combat-resolution-loss-to-stress conversion reduced by 1 (minimum 0)
- **Magic Resistance (1)** *(faction-wide species trait)* — natural biological resistance to incoming hostile magic; -1 to enemy cast rolls targeting any dwarf unit. The dwarven body and soul reject the Winds; spells skip off them more readily than they would mortal humans
- **Disciplined** (most rank-and-file and elite dwarfs are drilled veterans)
- **Heavy armour standard** at rank-and-file tier — dwarfs are the only species in the ruleset where Heavy armour is the *default*, not an upgrade

**Biologically constrained:**
- M 3 — dwarfs are slow; this is hard-coded into the species. No species-wide M-bump option
- I 2 baseline — dwarfs hit hard but slow; never apex-Initiative
- W 1 at rank-and-file; Hero-tier W 2-3, Lord-tier W 3-4. Modest scaling — dwarfs are not Saurus / Ogre bulk
- **No traditional Wind magic** — dwarfs do not channel the Winds. Dwarf magic comes exclusively from **engineered runes, Anvil-of-Doom rituals, and gunpowder**, not spell lores. A dwarf "Wizard" character does not exist; Runelords / Runesmiths use bound-rune magic items, not lore-cast spells. Runic magic itself is a deferred design space, pending a dedicated treatment
- No flight, no aquatic specialisation
- Cultural disinclination toward magic items beyond runic-engineered equivalents

**Equipment patterns:** every dwarf carries master-crafted gear — there is no "peasant-tier" dwarf. Iconic equipment: dwarf axes (one-handed standard), great weapons (hammers, axes, mauls — Hammerers / great-weapon Slayers), heavy armour standard at rank-and-file (Dwarf Warriors), full plate at elite (Ironbreakers, Longbeards). Gunpowder and engineered weapons: **handguns** (Thunderers — drilled handgunners), **crossbows** (Quarrellers), **cannons / Grudge Throwers / Organ Guns / Flame Cannons** (war machines, every one with engineering runes inscribed), **Gyrocopters / Gyrobombers** (steam-powered flying machines — the *only* "flight" available to a faction with no biological flying biology). Slayer caste eschews armour entirely — death-seeking culture refuses the protection that would prolong the shame of survival.

**Magic — runic engineering:** dwarven magic is **not channelled from the Winds**. Instead, **Runesmiths** and **Runelords** inscribe runes onto weapons, armour, standards, and equipment, capturing arcane effects in *engineered* form. Five rune categories: **Weapon Runes** (offensive), **Armour Runes** (defensive), **Runic Standards** (banner-borne battlefield effects), **Runic Talismans** (character-borne wards / utility), **Engineering Runes** (war-machine-specific). The **Anvil of Doom** is the highest-tier Runelord platform — battlefield rune-magic device powered by direct dwarven ancestor-link. Rune-magic is *bound at forging*, not cast per turn — a dwarven army's magical depth is entirely list-build dependent. Pending dedicated §11 Runic Magic treatment.

**Monstrous counterparts:** **none traditionally.** Dwarfs reject biological monsters as allies; their cultural disinclination is total. The closest dwarven equivalents are **engineered**: Gyrocopters / Gyrobombers (flying machines), Steam Tanks (when drafted — note: lore-canonically the Empire fields the Steam Tank, but it was engineered with significant Imperial-Dwarven cooperation), and the **Anvil of Doom** (Runelord-borne shrine). The faction expression of "monster-tier asset" is *engineered*, not *biological*.

**Variants of note:**
- Dwarf Warriors (W1, baseline; Disciplined, Ancestral Grudge, Resolute, Grudgebearer)
- *Pending:* Hammerers (elite Killing Blow), Ironbreakers (heavy plate apex), Longbeards (veteran Hatred-bonus), **Slayers** (renounced caste — same biology, same Stubborn / Grudge / Resolute baseline, but no armour by oath; "dwarves without armour" — death-seeking Frenzy-leaning unit identity, multiple sub-tiers including Trollslayers / Giantslayers / Dragonslayers / Doomseekers / Slayer Kings escalating by quarry), Thunderers / Quarrellers (gunpowder / crossbow), **Cannons / Grudge Throwers / Organ Guns / Flame Cannons** (war machines), **Gyrocopters / Gyrobombers** (engineered "flight"), Thanes / Lords (combat characters), Runelords / Runesmiths (rune-engineering "casters"), Anvil of Doom

### Chaos Warriors (Mortal Chaos)

(Note: this entry covers the *biologically corrupted-human* arm of Chaos. **Beastmen** are chaos-mutated animal-humanoid hybrids and have their own entry below; **Daemons** are aetheric beings with a fundamentally different paradigm and have their own entry below.)

> Mortal humans corrupted by the Ruinous Powers — twisted by chaos-exposure into something *more* than human. Each has fought hundreds of battles where lesser men would have died in the first; each has been hardened by chaos-exposure into a tougher frame than mortal humans wear. They wear master-crafted plate armour from the forges of the Chaos Wastes, wield weapons enchanted by daemonic patrons, and march under the banner of their Chaos Champion. **Marks of Chaos** are a layer in addition to the species-baseline — Khorne, Nurgle, Slaanesh, Tzeentch each grant mark-specific traits applied per unit / character; pending full Chaos faction draft.

**Typical baseline** — Chaos Warrior (the unmarked-mortal-corrupted reference):

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 4 | 5 | 5 | 3 | 4 | 4 | 2 | 4 | 2 | 9 | — |

(W 2 reflects chaos-mutation hardening — every chaos warrior has survived dozens of fights that would kill a man. Heavy armour standard; combined save 4+ baseline, 3+ with Heavy Shield. WS / I 4-5 reflects veteran skill compounded with chaos-blessed reaction speed.)

**Common traits** (typical, not universal):
- **Will of Chaos** (faction-wide for mortal Chaos) — Immune to Psychology + reroll failed recovery rolls; centuries of chaos-devotion purges fear
- **Marks of Chaos** (faction-design, per-unit / per-character at list-build) — Khorne (Frenzy), Nurgle (+1 T), Slaanesh (Stubborn + extra Imm Psych redundancy), Tzeentch (MR + Ward) — pending full faction draft
- **Heavy armour standard** at the Chaos Warrior tier
- **Disciplined** at rank-and-file tier (Chaos Warriors are veterans, not rabble); Marauders may sit at Undisciplined
- **A 2 baseline** at rank-and-file — only Chaos Warriors and Saurus Warriors carry A 2 at non-character infantry tier in the ruleset

**Biologically constrained:**
- Chaos-mutation W bump *varies* — Chaos Warriors W2 baseline, Marked-elite tiers may reach W3, Marauders sit at W1-2 depending on devotion-level. Not a fixed +1 across the board
- No Natural Armour at the human tier — protection from mortal armour and weapons is the chaos warrior's defensive expression; biological corruption shows in W and T, not in NA
- No flight, no aquatic specialisation at rank-and-file (Daemon Princes and unique characters can; rank-and-file cannot)
- Will of Chaos is a *psychological-immunity* trait, not a *biological-resilience* trait — chaos warriors take damage like other living things; their advantage is *spiritual*, manifest in the bond with their patron god

**Equipment patterns:** master-crafted plate from the **Forges of the Chaos Wastes** (heavy armour standard at Chaos Warrior tier, full plate at Chosen / Lord), **chaos-edged weapons** (one-handed hand weapons, paired hand weapons, polearms, great weapons — every weapon often daemon-bound or rune-etched), **Heavy Shield** common at Warrior tier. Marauders (lighter chaos infantry) wear less, fight with raw aggression. Chaos Knights ride **Chaos Steeds** (warped barded mounts, often chaos-mutated themselves — Cavalry-tier).

**Magic:** **Lores of Chaos** — each god has its own arcane lore (Lore of Tzeentch / Lore of Nurgle / Lore of Slaanesh / Lore of Khorne — though Khorne refuses sorcery; his "magic" is the Bloodbath itself). **Chaos Sorcerers** channel one chosen god's lore. **Daemon Princes** transcend mortal magic, gaining daemonic-tier casting. Chaos magic is faction-anchor at apex — Tzeentch lists especially.

**Monstrous counterparts:**
- **Dragons** — Chaos Dragons (corrupted apex), often mounts for Chaos Lords / Daemon Princes
- **Manticores** — chaos-warped beasts, Hero / Lord-tier mounts
- **Chaos Warhounds** — Warbeast-tier (corrupted hounds, fast-cavalry-equivalent)
- **Chaos Spawn** — failed chaos-corruption survivors, mutated past sapience; Monstrous-Beast tier, unstable rage
- **Chaos Trolls** — Trolls aligned to Chaos (Greenskin-shared species, Chaos overlay)
- **Daemon Princes** — apex characters who have transcended mortality into daemonhood; Lord-tier characters, fly, magical attacks, the bridge between Mortal Chaos and Daemons
- **Mutalith Vortex Beasts / Slaughterbrute / Cygors** (chaos-monstrous tier, see Beastmen entry for some)

**Variants of note:**
- Chaos Warriors (W2, unmarked, baseline; Will of Chaos, full plate)
- *Pending:* Marked Chaos Warriors (Khorne / Nurgle / Slaanesh / Tzeentch — each Mark a unit-buff layer), **Chosen** (elite Chaos Warriors), **Chaos Knights** (Chaos cavalry on Chaos Steeds), **Marauders** (lighter chaos infantry, often Undisciplined), Chaos Lord / Sorcerer / **Daemon Prince**, **Chaos Warhounds**, **Chaos Spawn**, Chaos Dragon / Manticore mounts

### Beastmen

> Chaos-mutated bestial humanoids — animal-headed, hoof-footed, savage. Where Chaos Warriors are *humans corrupted to apex-elite*, Beastmen are *bestial creatures born already-corrupted*: weaker baseline than the mortal Chaos human, more twisted, more feral. Conceptually closer to a Lizardmen-style species (multiple sub-castes, fixed biological tiers) than to the disciplined-elite Chaos Warriors. The Beastmen hierarchy by caste:
>
> - **Gors** — the rank-and-file majority. Human torsos and arms with distinctly animal heads and legs; the latter can be **Bovigors** (bovine-headed, cattle-like) or **Caprigors** (caprine-headed, goat-like). Form the spine of all warherds.
> - **Ungors** — the most common, smallest, and physically *most humanoid* breed of Gor Beastmen. Smaller horns or none, less muscle, lower tier. Carry out menial physical labour for the more powerful Gors and Bestigors; in war, Ungors fight as light skirmish-tier infantry.
> - **Bestigors** — the elite Beastmen tribe; Baqsen-Gor in the Dark Tongue. Larger, stronger, better-equipped, better-disciplined than ordinary Gors, blessed by the Dark Gods with the most spectacular horns, mighty constitution, and raw physical power. Monstrous-Infantry-tier scaling.
> - **Centigors** — *not Beastmen in the strictest sense, being more beast than man.* Centaur-bodied, drinking-and-brawling tribe, occasionally march with Beastherds when motivated. Cavalry-class.
> - **Minotaurs** — Monster-tier behemoths, larger than Bestigors, primal rage incarnate.
>
> Mutation variation is wide: horns or antlers, serrated blades sprouting from heads, sheep / horse / insect heads, extra limbs, eye stalks, lashing tails, and any other Chaos-touched alteration. Pack-and-herd culture; raid-tribes rather than disciplined regiments. Faction-wide Will of Chaos by Mark inheritance, but the disciplined-veteran flavour of Chaos Warriors does *not* extend — Beastmen are *savage*, not *drilled*.

**Typical baseline** — pending; rank-and-file Gor (the Beastman parallel to Common Orcs) is the expected anchor. Provisional values:

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 5 | 4 | 3 | 3 | 4 | 4 | 1 | 3 | 1 | 7 | — |

(W 1 — weaker than Chaos Warriors at the rank-and-file tier per the "weaker baseline + more twisted" framing. M 5 — Beastmen are quicker than Chaos Warriors, evolved for the chase. WS-A 4 / WS-D 3 captures the savage-attacker valence. T 4 — bestial-frame resilience.)

**Common traits** (typical, not universal):
- **Will of Chaos** (Mortal Chaos faction-wide inherit, partial — most Beastmen are Imm Psych but the reroll-recovery is unit-specific)
- **Marks of Chaos** (faction-design — same as Chaos Warriors; Khorne / Nurgle / Slaanesh / Tzeentch / Undivided)
- **Undisciplined** at rank-and-file (Gors, Ungors); some Bestigor units may carry Disciplined
- **Frenzy-leaning** — Beastmen cultural valence is *savage*, distinguishing them from Chaos Warriors' *disciplined-elite* posture
- **Pack tactics** — Beastmen identity rules tend toward herd-mass and ambush rather than drilled-line combat

**Biologically constrained:**
- Weaker biological baseline than Chaos Warriors — W1 rank-and-file, T 4 for the larger Gors, T 3 for Ungors. Bestigors at Monstrous-Infantry-class W3-4
- No Natural Armour at the rank-and-file tier (some Bestigor / Minotaur variants may carry hide NA at higher tiers)
- Cultural disinclination toward heavy armour — Beastmen wear light armour at most; the Chaos-Warriors-style full plate identity is *not* a Beastman trait
- No magical biology at rank-and-file — Bray-Shamans channel chaos magic via Marks, but rank-and-file Gors are not casters
- Lifespan considerably shorter than Chaos Warriors — Beastmen are bestial, raid-living; few survive to apex tier

**Equipment patterns:** ramshackle scrap-armour, hand weapons (cleavers, axes, hammers — taken from slain enemies as much as forged), spears, bows. Bestigors carry great weapons (the elite tier's heavier kit). No standardised armoury — Beastmen scavenge. Light armour at most for Gors; some Bestigors reach medium / heavy via stolen plate.

**Magic:** **Bray-Shamans** channel chaos magic, often Mark-aligned — Lores of Chaos as per Mortal Chaos entry. Less disciplined than Chaos Sorcerers; Bray-Shamans are bestial-frenzy casters. Beastmen lack the magical depth of Chaos Warriors — magic is a niche role, not a faction-anchor.

**Monstrous counterparts:**
- **Minotaurs** — Monster-tier behemoths, raw rage, Monstrous-Infantry-class
- **Centigors** — centaur-bodied semi-allies (Cavalry tier in our system)
- **Cygors** — one-eyed chaos-blinded giants, magic-attuned (sense magic, anti-caster role)
- **Ghorgons** — chaos-mutated multi-armed giants, Monster-tier
- **Razorgors** — boar-mutants (Warbeast-tier, often used as chariots / Chariot-pull beasts)
- **Chaos Warhounds** — Beastmen-shared with Mortal Chaos
- **Chaos Giants** (when aligned with Beastherds) — Monster-tier apex

**Variants of note:** *All pending* — Gors (W1, rank-and-file), Ungors (W1, light skirmish-tier — smaller, more humanoid, slave-labour caste), **Bestigors (W2, Monstrous-Infantry elite — Baqsen-Gor; the chaos-blessed apex Beastmen, larger and stronger frame)**, Centigors (W2-3, Centaur-bodied — Cavalry tier), Minotaurs (W3-4, Monster-tier), Beast Lords / Doombulls / Bray-Shamans, Razorgors / Razorgor Chariots, Cygors, Ghorgons, Chaos Warhounds, Chaos Giants

### Daemons

> Immortal beings of raw Chaos who dwell in the Realm of Chaos — not biological in the mortal sense, but constructs of chaos-energy given form by the will of their patron god and the *expectations of those who behold them*. A Bloodletter looks the way it does because the people facing it believe it should look that way; the daemon's perceived form is amplified by the abject terror in the witness's mind. Daemons can only manifest in the mortal world while sustained by intense concentrations of ambient magic or while possessing a mortal body — without that anchor, they cannot remain. **A Daemon cannot truly be slain** in the mortal sense: its physical body can be destroyed, but the essence is merely *banished* back to the Forge of Souls in the Realm of Chaos, where the Daemon embarks on the slow process of forming a new body and dreams of vengeance. Each of the four Chaos Gods commands his own daemonic legions: **Khorne** (Bloodletters, Bloodthirsters, Flesh Hounds — the war-fragments), **Nurgle** (Plaguebearers, Beasts of Nurgle, Great Unclean Ones — the corruption-fragments), **Slaanesh** (Daemonettes, Fiends, Keepers of Secrets — the desire-fragments), **Tzeentch** (Pink/Blue Horrors, Flamers, Lords of Change — the change-fragments). Hierarchy: **Lesser Daemons** (rank-and-file legion-troops), **Greater Daemons** (Lord-tier patron-fragments — Bloodthirster, Great Unclean One, Keeper of Secrets, Lord of Change), with intermediary Daemonic Heralds and unique entities between.

**Typical baseline** — provisional Lesser Daemon (rank-and-file legion-troop, e.g., Bloodletter):

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 4-5 | 5 | 4 | 0 | 4-5 | 4 | 1-2 | 4-5 | 1-2 | 9-10 | — / Ward 5+ |

(Stats vary by patron god — Khorne Bloodletters lean toward higher S and A; Nurgle Plaguebearers toward higher T and resilience; Slaanesh Daemonettes toward higher I and A; Tzeentch Horrors toward magical attack-output. Daemonic essence resists mortal weapons via Ward 5+ baseline; the chaos-energy form has no Natural Armour but turns mundane strikes through sheer unreality. Per-god baselines pending full faction draft.)

**Common traits** (typical, not universal):
- **Daemonic** *(faction-wide)* — Immune to Psychology; the chaos-energy form does not feel fear or panic in the mortal sense
- **Banished, not Killed** — when a Daemon is reduced to 0 W, its physical form is destroyed and the essence returns to the Forge of Souls. Mechanically removed as a casualty; the lore framing is *banishment*, not *death*
- **Mark-aligned intrinsic** — each Daemon carries the Mark of its patron god inseparably; the four daemonic legions are mechanically distinct via per-god Marks (Khorne / Nurgle / Slaanesh / Tzeentch — full Mark mechanics pending Chaos faction draft)
- **Ward Save baseline** — daemonic essence resists mortal weapons; species-wide Ward (5+ tentative) against mundane attacks; Magical Attacks bypass
- **Sustained by Magic** — Daemons require ambient warp-energy or possession of a mortal vessel to maintain manifestation; **dispelling effects, anti-magic auras, and the death of a summoning caster** may force daemons to fade. Tentative mechanic: an "Instability" Crumble-equivalent triggered when the army's daemonic anchor (a Greater Daemon, a binding spell) is broken — pending design pass

**Biologically constrained:**
- No biological reproduction, no aging, no mortal lifespan — Daemons exist as long as warp-energy sustains them; banishment is a setback, not annihilation
- Cannot wield non-chaos magic items — the chaos-aligned essence rejects mortal-magical bindings
- No Natural Armour — defence is via Ward (chaos-energy protection), not material armour
- Form is *patron-determined and observer-amplified* — Daemons cannot transcend their patron god's domain. A Khornate daemon cannot do Slaaneshi things; a Tzeentchian daemon cannot do Nurglite things. The Marks are not interchangeable
- Cannot Rally (Daemonic-keyword inherit, parallel to Undead) — the manifestation is psychological-stable but cannot be *reinforced*; a faltering daemon must be re-summoned rather than re-rallied

**Variants of note:**
- **Khorne legions** — Bloodletters (rank-and-file), Flesh Hounds (warbeast tier), Bloodcrushers (juggernaut cavalry), Bloodthirster (Greater Daemon)
- **Nurgle legions** — Plaguebearers (rank-and-file), Beasts of Nurgle (warbeast), Plague Drones (cavalry-tier), Great Unclean One (Greater Daemon)
- **Slaanesh legions** — Daemonettes (rank-and-file), Seekers / Fiends (cavalry / monstrous), Keeper of Secrets (Greater Daemon)
- **Tzeentch legions** — Pink Horrors (rank-and-file casters), Blue Horrors (split-form on death), Flamers (warbeast magical), Lord of Change (Greater Daemon)
- **Daemonic Heralds** — Hero-tier intermediary between rank-and-file and Greater Daemons, per god
- *Pending full faction draft* — per-god baselines, Mark mechanical packages, summoning rules, Instability-Crumble specifics

### Vampire Counts

> The animated dead of Sylvania, raised and commanded by Vampires using necromantic magic. Two distinct biological tiers within the faction:
>
> **Animated Dead (rank-and-file)** — Skeleton Warriors, Zombies, Grave Guard. Mindless or near-mindless corpses re-animated by spell-binding; mortal flesh and bone given an unholy semblance of life. The Necromancer or Vampire's continued spellwork keeps them upright; remove the binding (kill the master, dispel the magic) and they crumble. Crumble accelerates as the unit takes stress beyond its Res — bones collapse and rotting flesh dissolves where the necromantic binding gives out.
>
> **Vampires (apex)** — supernatural undead nobility. Vampires are biologically distinct from rank-and-file Skeletons and Zombies — they retain consciousness, intelligence, and apex combat capability; they regenerate via blood-drinking; they channel necromantic magic personally. Vampires drive the entire Vampire Counts army both martially and magically — they are the necromantic anchor that keeps the rank-and-file standing.

**Typical baselines** — separate per sub-tier:

**Animated Dead (Skeleton Warrior baseline):**

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 4 | 2 | 2 | 2 | 3 | 3 | 1 | 2 | 1 | 4 | — |

(Low Res 4 — Crumble triggers easily; the unit dissolves under sustained pressure. Maintained on the table by Necromancy resurrection, not by intrinsic durability.)

**Vampires (Vampire Hero / Lord baseline):**

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 6 | 6-7 | 6-7 | 4 | 5 | 4-5 | 4-5 | 6 | 4 | 9-10 | — |

(Apex-tier supernatural stats — high WS, high I, supernatural T. Vampires regenerate via Vampiric Hunger on Bite wounds.)

**Common traits — Animated Dead:**
- **Undead** (faction-wide; see §8 — Imm to Psychology, no morale-source stress, can't Fall Back, Crumble mechanic when stress > Res)
- **Cannot Rally** (intrinsic to Undead keyword)
- Low W / T / Res — frail per-model; Necromancy keeps the unit alive
- No species-wide combat-cascade rules — animated-dead biology lacks the regenerative or apex-skill traits that Vampires carry

**Common traits — Vampires:**
- **Undead** (faction-wide)
- **Vampiric Hunger** — Bite-weapon attacks regenerate 1W on unsaved wound (cap 1W/turn)
- **Bloodline Powers** (list-build customisation menu — Vampire Lord & Vampire Hero)
- **Wizard** at apex (Vampire Lord caster-tier; Necromancy-only-but-expanded magical depth)

**Biologically constrained:**
- Animated Dead cannot be Hero or Lord tier — they're rank-and-file binding-magic constructs; characters are Vampires (apex) or Necromancers (mortal humans, see Humans entry)
- Animated Dead cannot grow beyond their drafted W (W1 baseline at infantry; W2 for Wights / Grave Guard tier, max ~W3 for skeletal cavalry)
- No biological reproduction — the population is *raised*, not bred. Necromancer / Vampire magic generates the warriors as needed
- Vampires are biologically supernatural — Marked (Bloodlines) and lifespan-unbounded; their bumps to W / T / WS reflect supernatural stat ladder, not mortal biological scaling
- No armour beyond what was worn in mortal life — Skeleton Warriors with rusted bucklers, Grave Guard with light armour; Vampires with Heavy armour as apex caster-warriors

**Equipment patterns:** Animated Dead retain *what they died wearing* — Skeleton Warriors with rusted bucklers and rotted leathers, Zombies with whatever rags survive, Grave Guard with their mortal-life heavy armour and Wight Blades (magical-by-binding). Vampires wear what their station and personal taste dictate — typically Heavy armour at apex, intricate gothic plate; Vampire blades are often magical heirlooms (the Sword of Vlad, Drakenhof Runefang etc.).

**Magic:** **Necromancy** is the faction-anchor lore (signature: Invocation of Nehek for resurrection — see §11). Vampires often access **Vampire-specific lores** in addition (Lahmian for charm-magic, Strigoi for bestial-rage, etc. — pending faction-draft expansion). Necromancers are mortal humans who learned the dark arts; Vampires are *born to* the magic supernaturally. The Vampire Lord is one of the most-feared Lord-casters in the Old World, second only to Slann / Lord Kroak in raw magical depth.

**Monstrous counterparts:**
- **Skeletal cavalry** — **Black Knights** (skeletal Wights mounted on skeletal steeds; ethereal-leaning), **Hexwraiths** (incorporeal cavalry, bypass terrain)
- **Wraiths / Banshees** — Ethereal-tier (incorporeal, magical-attacks-only-to-wound)
- **Vargheists** — bat-form Vampires (degenerate sub-cousin), Monstrous Infantry tier
- **Crypt Horrors** — bloated cannibal-undead, Monstrous Infantry tier
- **Black Coach** — Undead chariot (skeletal horses + hearse)
- **Mortis Engine** — necromantic siege-platform, soul-energy weapon
- **Coven Throne** — apex Vampire-Lord platform (multi-handmaiden palanquin)
- **Terrorgheist** — apex flying Undead monster (giant bat-corpse, sonic-screech weapon)
- **Zombie Dragon** — Vampire-Lord-mount apex; flying Monster, breath weapon
- **Strigoi-Vampires** — degenerate Vampire bloodline (apex bestial-vampire Lord)

**Variants of note:**
- Animated Dead: Skeleton Warriors (W1, rusted-buckler tier), Zombies (W1 mindless mass), Grave Guard (W2 Wight-tier elite skeletons)
- Vampires: Vampire Hero (W4, mid-tier supernatural), Vampire Lord (W5, apex caster-warrior)
- Necromancer (mortal human, separate species — see Humans entry): the *cause* of the animation, not himself Undead
- *Pending:* Black Knights, Hexwraiths, Wraiths / Banshees, Black Coach, Vargheists, Crypt Horrors, Strigoi-Vampires, Mortis Engine, Coven Throne, Terrorgheist / Zombie Dragon (apex Undead monsters)

### Tomb Kings

> The mummified dead of Nehekhara — the ancient kingdom whose pyramid-tombs predate even the Empire — raised by **Liche Priests** of the **Mortuary Cult** through ritual rather than per-turn spellwork. Where Vampire Counts bind newly-dead flesh through *active* necromantic casting (an unbroken spell-stream sustains the army), Tomb Kings rouse the *long-buried* — embalmed corpses ritual-prepared centuries before death, woken from millennial slumber by the Mortuary Cult's invocations. Each warrior of Khemri retains **individual ritual-bound purpose**: he remembers the king he served and the duty he was buried with. The Liche Priests *direct* and *sustain* rather than *animate per cast*; without a Liche Priest's presence, however, the army gradually falls to dust — skeleton warriors collapsing to piles of bones across the battlefield. So the autonomy distinction vs Vampire Counts is **degree, not kind**: Tomb Kings dead don't need per-turn resurrection spells to stay upright, but they do require the Liche Priest's *ongoing ritual presence* in the army; remove him and the slow dissolution begins. The faction also fields **stone constructs** (Sphinxes, Hierotitans, Casket of Souls, Bone Giants) — animated stone-and-bronze figures, T-anchored with no separate Natural Armour layer (the stone *is* the toughness).

**Typical baselines** — separate per sub-tier:

**Skeletal Tomb-Bound (Tomb-King-bound skeleton):**

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 4 | 2 | 2 | 2 | 3 | 3 | 1 | 2 | 1 | 5-6 | — |

(Slightly higher Res than Vampire Counts skeletons — Res 5-6 vs 4. Tomb-bound dead retain ritual-purpose; they don't crumble as readily as fresh-bound Vampire Counts skeletons. Liche Priests sustain via Mortuary Cult ritual, not constant per-turn spellwork.)

**Stone Constructs (Khemrian Warsphinx as anchor):**

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 6 | 4 | 4 | 0 | 5 | 8 | 10 | 1 | (varies) | 10 | — |

(T 8 captures the stone-construct durability — the stone *is* the toughness; no separate Natural Armour layer to avoid double-counting.)

**Common traits — Tomb Kings (faction-wide):**
- **Undead** (per §8 — Imm Psychology, Crumble-paradigm, Cannot Rally, Cannot Fall Back)
- **More autonomous than Vampire Counts skeletons** — Liche Priest anchor permits ritual-distance command without per-turn spell-cast resurrection (specific Crumble trigger pending design)
- Most Tomb Kings units carry the **Magical Attacks** keyword (the magic that animates them is in their weapons)
- **Killing Blow** appears on many high-end units (Tomb Guard, Tomb King, Necrosphinx) — would generalise as a faction-leaning trait

**Common traits — Stone Constructs (sub-tier):**
- **Stone Construct** (per Warsphinx entry §18) — Imm to Killing Blow (no joints to sever), Imm to Poisoned Attacks (no flesh to poison), Liche-Priest-anchored animation bypasses Crumble while a priest lives
- **Not Flammable** — distinct from Forest Spirits (which are wood-bodied and Flammable); Tomb Kings stone constructs are made of *stone*, fire-resistant by composition. Flaming attacks resolve at their normal effect against stone constructs (no Regen-negation issue applies — they have no Regen — but no Flammable-rerolls either)

**Biologically constrained:**
- No biological reproduction — Tomb Kings dead are pre-buried, ritual-prepared centuries before death; the population is *finite*
- Stone constructs lack any Natural Armour layer; T 6-8 expresses durability without doubling on save
- Cannot Rally / Cannot Fall Back (Undead-keyword inherit)
- Skeletal warriors in Tomb Kings have similar limits to Vampire Counts skeletons — W1 baseline, low Res, melee-focused; the higher Res 5-6 vs Vampire Counts' 4 is the autonomy distinction

**Equipment patterns:** ancient bronze weapons — **khopeshes** (Khemrian sickle-bladed swords), spears, ceremonial bows (mortuary-prepared composite bows), bronze-and-jade armour. The aesthetic is **bronze and gold and sand-bleached white** — Khemrian style, not Sylvanian gothic. Tomb Guard wear bronze plate and wield khopeshes (Magical Attacks, Killing Blow). All Tomb Kings weaponry carries *Magical Attacks* by default — the magic that animates the dead is in the weapon's swing.

**Magic:** **Mortuary Cult magic** — ritual-based, distinct from Vampire Counts' per-turn-cast Necromancy. Liche Priests and Tomb Kings channel **Nehekharan Incantations** — a faction-exclusive lore drawing on the Mortuary Cult's millennia of accumulated death-rites. Distinct from Necromancy in that the bindings are *inscribed at burial*, not cast at the moment of need; the Liche Priest *invokes* rather than *creates*. Pending dedicated §11 Mortuary Cult lore drafting.

**Monstrous counterparts (Stone-and-Bronze tradition):**
- **Khemrian Warsphinx** — see §18 stress-test entry; T 8 stone construct with Thundercrush Attack
- **Necrosphinx** — sister-construct, more aggressive, Decapitating Strike
- **Hierotitan** — bronze-bound mummified colossus, magic-amplifier (boosts nearby Liche Priests)
- **Bone Giant** — colossal animated skeleton; Monster-tier apex
- **Necrolith Bone Dragon** — apex Tomb-King mount; flying skeletal Monster
- **Casket of Souls** — magical artillery / Wail-of-the-Damned ranged weapon
- **Screaming Skull Catapult** — ritual-animated stone-thrower (bound skull-projectiles screech as they fly)
- **Ushabti** — bronze-statue warrior-spirits (Monstrous Infantry tier)
- **Tomb Scorpions** — buried Mortuary-Cult guardians, ambush-spawned

**Variants of note:**
- Skeletal Tomb-Bound (Skeleton Warriors equivalents — W1, ritual-bound)
- Tomb Guard (W2, elite skeletal honour-guard, Khopesh + Magical Attacks + Killing Blow)
- **Skeletal Chariots** — iconic Khemri cavalry (skeletal horses pulling bronze-bound chariots, archer-crew)
- **Skeleton Horsemen / Light Horsemen** — skeletal cavalry (bow-armed, fast harassers)
- **Tomb Swarms** — buried scarab-swarm ambush units (Swarm-type)
- Stone Constructs: Khemrian Warsphinx, Necrosphinx, Hierotitan, Bone Giant, Casket of Souls, Necrolith Bone Dragon — varied apex-tier
- Characters: Liche Priests / Liche High Priests (caster Hero / Lord), Tomb Princes (combat Hero), Tomb Kings (combat Lord, mummified-but-conscious — Settra is the apex named Tomb King)
- *Pending:* Screaming Skull Catapults, Ushabti, Tomb Scorpions, Settra (named Lord), full character treatment

### Wood Elves (Asrai)

> Descendants of High Elves who chose to remain in the Old World, bonded across generations to the forest-kingdom of **Athel Loren**. Biologically the Asrai are *elves* — same long-lifespan slim physiology, same Elven Grace + Martial Prowess that High Elves and Dark Elves share — but the cultural and magical bond with the forest has shaped their warfare, equipment, and magic into a distinct identity. Wood Elves "have been likened to a force of nature, neither truly good nor evil"; they pay homage to **Orion (King of the Wood, avatar of Kurnous the Hunter)** and **Ariel (Queen of the Wood, avatar of Isha the Mother)**, and the forest itself fights alongside them as a faction-anchor. Athel Loren is suffused with primeval magic; *time flows unevenly* within its borders, and the forest is alive in ways incomprehensible to mortals.
>
> Two distinct biological tiers within the faction:
>
> **Asrai (the Wood Elves themselves)** — same elf biology as Asur and Druchii, with M 5-6, low T/W, Elven Grace + Martial Prowess faction-wide. The cultural axis: **WS-A < WS-D leaning** (skirmisher-evader — Wood Elves are forest-rangers, ambush-hunters, kite-and-fade specialists; closer in valence to Skink Skirmishers than to disciplined Asur or frenzied Druchii).
>
> **Forest Spirits** — biologically distinct entities; *not elves at all*. **Dryads** (forest-spirits bound to living trees, Monstrous-Infantry tier), **Tree Kin** (lesser tree-spirits bound into dead-wood bodies — animated tree-monsters), **Treemen** (apex Forest Spirit Monster — ancient sentient trees taking the field). Forest Spirits do not bleed in the mortal sense; they are *bound spirits in plant-matter*, with their own durability paradigm closer to Daemons-on-mortal-plane than to mortal elves.

**Typical baselines** — separate per sub-tier:

**Asrai (rank-and-file Wood Elf, e.g., Glade Guard):**

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 5 | 4 | 4 | 5 | 3 | 3 | 1 | 5 | 1 | 8-9 | — |

(BS 5 reflects the Glade Bow apex tradition — Wood Elves are the best longbow archers in the Old World. Standard elf low T/W. Res 8-9 — slightly below Asur's 9 but above peasant-tier humans; Asrai have less of the millennia-of-discipline framework, more of the wild-bond intuition.)

**Forest Spirits (Dryad baseline):**

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 5 | 4 | 4 | 0 | 4 | 4 | 2 | 4 | 2 | 8 | 5+ (bark-and-thorn) |

(Forest Spirits are tougher than Asrai — bark-bodied resilience, claw-and-thorn natural attacks, Fear-causing. Treemen scale up to Monster-tier W 6-8.)

**Common traits — Asrai (typical, not universal):**
- **Elven Grace** (faction-wide, shared with Asur and Druchii) — Ward 6+ in melee against attacks at the elf's I or lower
- **Martial Prowess** (faction-wide) — reroll to-Hit 1s in melee
- **Forest Stride** *(Asrai-distinct)* — Wood Elves treat forest terrain as Open ground (no movement penalties, no Dangerous Terrain tests for thorn-fields / dense undergrowth); the forest does not impede the forest-folk
- **Wardancer / Skirmisher cultural valence** — most Asrai melee units are Skirmisher-keyword; the species expression of melee is fluid evasion, not formed-wedge discipline

**Common traits — Forest Spirits (typical, not universal):**
- **Forest Spirit** *(faction-shared trait — working title)* — bound to Athel Loren's magic; potential restrictions or bonuses related to proximity to forest terrain (mechanic per unit)
- **Fear** (most Forest Spirits radiate primeval-forest dread)
- **Natural Armour 5+** (bark-and-thorn body — biological armour distinct from worn armour)
- **Magical** — many Forest Spirit attacks count as Magical Attacks intrinsically
- **Flammable** *(faction-wide for the wood-bodied tier — see §8)* — Dryads, Tree Kin, and Treemen are literal treefolk; Flaming attacks reroll failed wounds against them. The bark-and-thorn NA 5+ does not protect against fire taking hold. Lore-true: an Athel Loren Spirit walks through arrows but burns like dry kindling

**Equipment patterns:** **Glade Bow** is the apex longbow tradition — a 30"+ range, AP-leaning ranged identity that defines Wood Elf shooting (Glade Guard, Waywatchers, Glade Riders all wield variants). Light armour at most for elf rank-and-file; **paired asrai blades** for Wardancers (no armour by oath); **spears** for Eternal Guard (the apex elf melee tier — King Orion's personal guard, halberd-equivalent reach). Wardancers eschew armour entirely — they fight in dance-step rhythm, dodging through gaps with Imm to Fear / Terror per their cultural identity.

**Magic:** **Lore of Athel Loren** — faction-exclusive Wood Elf lore drawing on the Weave of life and death that flows through the forest. Pending dedicated §11 drafting; expected to draw heavily from Lore of Life themes (regeneration, healing, plant-summoning) plus forest-specific spells (animating trees, calling Wild Hunt). **Spellweavers** (Lord-tier casters) and **Spellsingers** (Hero-tier) are the standard Wood Elf magical character. Magic is faction-anchor — Athel Loren itself contributes magical presence to any Wood Elf army on the field.

**Monstrous counterparts:**
- **Forest Spirits** *(faction-shared sub-tier — see above)* — Dryads (Monstrous Infantry), Tree Kin (Monstrous Cavalry / Monster-adjacent), **Treemen** (Monster-tier ancient sentient trees, can be Hero / Lord characters)
- **Wild Riders / Stag Riders** — Asrai cavalry on Great Stags (sacred Athel Loren beasts; often Wild-Hunt-themed Frenzy-leaning units)
- **Sisters of the Thorn** — fast cavalry on Steeds of Isha (apex Asrai magical cavalry)
- **Great Eagles** — shared with High Elves; sacred birds of Athel Loren's high peaks
- **Forest Dragons** — Athel-Loren-specific Dragon variant; mounts for Asrai Lords
- **Orion** (named King-Lord, avatar of Kurnous) — apex Wood Elf Lord-character, Wild Hunt summoner
- **Ariel** (named Queen-Lord, avatar of Isha) — apex Wood Elf caster-Lord, mistress of Athel Loren's magic

**Biologically constrained — Asrai:**
- Same constraints as other Elves (low T / W, no Natural Armour beyond worn equipment, M 5 baseline, slim biological frame)
- **No heavy armour culturally** — Wood Elves disdain plate; their warfare is mobility-and-bow, not armour-and-charge
- **No gunpowder, no engineered war machines** — Asrai reject mortal-industrial technology; the closest equivalent is a Treeman (a *living* siege-engine)
- **No formed-line combat tradition** — Asrai are Skirmisher-keyword across most rank-and-file units; the cultural expression is fluid evasion

**Biologically constrained — Forest Spirits:**
- Cannot exist far from forest terrain without lore-justification — Dryads especially are bound to specific living trees
- No biological reproduction in the mortal sense; Forest Spirits are *born of the forest's will*, not bred
- No equipment slot — claws, thorns, bark-bodies are their entire kit
- Cannot wield ranged weapons (the species combat profile is melee-natural-attack)

**Variants of note:**
- **Asrai units:** Glade Guard (W1, baseline rank-and-file Glade Bow archers), Eternal Guard (W1 elite spear-and-shield, defensive formed-line — *the* Asrai disciplined-tier exception), Wardancers (W1, no armour, paired blades, Imm Fear/Terror, Frenzy-leaning), **Waywatchers** (W1 Skirmisher-Sniper-Scouts apex), Glade Riders (W1 fast cavalry), Wild Riders (W1 frenzied stag-mounted cavalry), Sisters of the Thorn (apex magic-cavalry)
- **Forest Spirits:** Dryads (Monstrous Infantry, W2, bark-NA, Fear), Tree Kin (Monstrous Cavalry / Monster-adjacent, W3-4), **Treemen** (Monster, W6-8, ancient sentient trees, can be Hero / Lord characters)
- **Apex Lord characters:** **Orion** (King of the Wood, named Lord, Kurnous-avatar; Wild Hunt summon), **Ariel** (Queen of the Wood, named Lord-caster, Isha-avatar; Athel Loren's magical anchor), Spellweaver (Lord-caster), Highborn (combat Lord)
- *Pending:* Glade Lord / Highborn / Wayfinder character drafts, Forest Dragon mounts, Eagle / Great Stag mounts, Lore of Athel Loren spell list, full Wood Elf faction draft

### Skaven

> Anthropomorphic rat-men of the **Under-Empire** — the vast subterranean tunnel network that permeates beneath every continent of the Old World. Four to five feet tall, lithe-furred, sharp-toothed, tail-balanced; cunning and treacherous individually, vicious and overwhelming in numbers. The Skaven race is **highly fecund** — breeding-stock multiplies with rat-like speed; a Skaven army's first identity is **mass**. Cowardly per-individual but courageous in swarms, the species fingerprint is "more-more, kill-kill" — backstabbing kin whenever a chance presents itself, then surging forward as a tide when the numbers favour them. Driven by **warpstone hunger** — the species substance, fuel, drug, and arcane power-source — the Skaven civilisation is built on the warpstone they mine from beneath the world. Constant inter-clan civil war is the natural Skaven state; the **Council of Thirteen** (twelve lord-Skaven plus the symbolically-empty seat for the Horned Rat himself) nominally arbitrates but practically just makes the schemes more elaborate.

**Typical baseline** — rank-and-file Clanrat:

| M | WS-A | WS-D | BS | S | T | W | I | A | Res | NA |
|---|------|------|----|---|---|---|---|---|-----|-----|
| 5 | 3 | 3 | 3 | 3 | 3 | 1 | 4 | 1 | 5 | — |

(M 5 — Skaven are quick. Res 5 — cowardly baseline; the species identity is mass-bravery, not stoic resilience. Skavenslaves drop another step on most stats; Stormvermin / Plague Monks / Eshin assassins are elite tiers above this baseline.)

**Common traits** (typical, not universal):
- **Verminous Valour** *(Skaven-wide — working title)* — Skaven units derive courage from numbers; large units gain meaningful Res / morale benefits, while units below half strength suffer escalating cowardice penalties (specific mechanic per unit)
- **Strength in Numbers** — many Skaven units field 30+ models in lore-canonical regiments; the species expresses identity at *unit size* rather than per-model quality
- **Backstabbing** — Skaven rules often interact with stress / morale of surrounding friendly units; a Skaven unit that breaks may *spread panic* faster than the +1 stress baseline normally implies (mechanic per unit)
- **Undisciplined** at rank-and-file (Clanrats, Skavenslaves); **Disciplined** at elite tier (Stormvermin — black-furred drilled veterans of the Mors clans)

**Equipment patterns:** rusted hand weapons + shields at the rank-and-file, with **halberds** at Stormvermin tier. **Warpstone-powered firearms** are Clan Skryre's signature: **Warplock Jezzails** (long-range warpstone sniper-rifles), **Warplock Pistols** (Warlock-Engineer sidearms), **Ratling Guns** (hand-cranked Gatling-style multi-barrel), **Warpfire Throwers** (warpstone-fuelled flamethrowers). **Plague weapons** from Clan Pestilens: **Plague Censers** (swung incense-burners trailing miasma), poison-coated daggers. **Eshin gear** includes throwing stars (warp-stars), poisoned blades, smoke bombs, climbing claws.

**Magic:** **Warpstone-fuelled** across the species. Three distinct casting traditions per Greater Clan:
- **Lore of Ruin (Skryre Warlock-Engineers)** — warp-lightning, technological-arcane fusion; cast from warpstone batteries strapped to the Engineer's back
- **Lore of Plague (Pestilens Plague-Priests)** — disease, miasma, plague-vomit, contagion-summoning; cast through ritual chant and warpstone-charged plague catalysts
- **Lore of Stealth / Night (Eshin)** — shadow-step, smoke, distortion; fewer dedicated casters, more bound-warpstone-item users
- **Grey Seers** — the most powerful Skaven casters, twin-tailed albino-marked Skaven who serve the Council of Thirteen directly. Grey Seers channel a fusion-lore drawing from Ruin + Plague + raw warpstone (faction-flavoured). The apex Skaven Lord-caster

**Monstrous counterparts (Clan Moulder's bio-engineered menagerie):**
- **Rat Ogres** — Monstrous-Infantry-tier; massive brutes stitched together from rats and other creatures by Moulder's flesh-shapers, Packmaster-handled (parallel to Skink Handlers driving Salamanders)
- **Hell Pit Abomination** — Monster-tier apex; towering mass of mutated flesh, unstable regenerative biology, frequently destroys itself mid-battle
- **Giant Rats / Wolf Rats** — Warbeast / cavalry tier (Packmaster-handled, swarm-style)
- **Plague Toads** — Pestilens-bred monstrous-beast tier
- **Plague Furnace** — Pestilens battle-altar (bell + plague-cauldron mounted on burnt-bone wagon)
- **Engineered "monsters" from Skryre:** **Doomwheel** (motorised warpstone hamster-wheel of death — Monster-tier engineered chariot), **Warp Lightning Cannon** (artillery), **Plagueclaw Catapult** (Pestilens artillery)

**Biologically constrained:**
- W 1 at rank-and-file; Hero-tier Skaven characters W 2-3, Lord-tier Warlords / Grey Seers / Plague Lords / Warlock Masters / Master Assassins / Master Moulders W 3-5. Skaven biology is fundamentally fragile per-model; the species expresses durability through *numbers*, not *bulk*
- No Natural Armour beyond the rusted gear they wear — fur is not protective at the WS-vs-S level
- Cowardice baseline — Res 4-6 across most units. Skaven Lord-tier characters (Grey Seers, Warlords) reach Res 7-8 via station / warpstone-corruption / sheer ambition, never higher
- T 3 baseline rank-and-file (T 4 only at elite tier — Stormvermin, certain monstrous Moulder-creations)
- Cannot hold a line under sustained pressure without numerical advantage — this is the species fingerprint, and faction design reinforces it via Verminous Valour and similar identity rules
- No flight (no biological flying Skaven; Doomwheel is engineered ground-mobility, not flight)
- Low magical durability per-cast — Skaven magic is *cheap and powerful but unreliable*, frequently miscasting (warpstone overload). Grey Seers excepted at the Lord tier
- Cannot be Disciplined faction-wide — Skaven culture is fundamentally treacherous; the few Disciplined units (Stormvermin) are exception, not norm

**Variants of note:**
- **Clanrat** (W1, baseline rank-and-file, Mors-clan generic warrior)
- **Skavenslave** (W1, lowest-tier, even more cowardly — used as expendable forward-screen)
- **Stormvermin** (W1, Mors elite, halberd, black-furred, Disciplined and Stubborn-leaning) — the apex Mors warrior tier
- **Clan Eshin units:** **Night Runners** (skirmishers), **Gutter Runners** (Scout-tier infiltrators), **Eshin Triads / Assassins** (Hero-tier sniper-killers)
- **Clan Pestilens units:** **Plague Monks** (Frenzy-leaning fanatics, often massed; W1 but A 2 with paired weapons), **Plague Censer Bearers** (Plague Monk variant with censer), **Plague Priest** (Hero / Lord caster)
- **Clan Skryre units:** **Warplock Jezzails** (sniper-tier ranged Hero-supports), **Ratling Gun teams**, **Warpfire Thrower teams**, **Warp Lightning Cannons** (artillery), **Doomwheel** (Monster-tier engineered chariot), **Warlock-Engineer** (Hero / Lord caster)
- **Clan Moulder units:** **Giant Rats** (Warbeast swarm), **Rat Ogres** (Monstrous-Infantry brutes), **Hell Pit Abomination** (Monster), **Packmaster** (Hero handler), **Master Moulder** (Lord)
- **Apex Lord-tier:** **Grey Seer** (twin-tailed magic apex), **Warlord** (clan combat-Lord), **Verminlord** (greater-daemon-of-the-Horned-Rat — daemon-tier ascended Skaven, faction-edge crossover with Daemons entry)
- *Pending:* full faction draft — per-clan lore detail, full unit roster, Council of Thirteen named Lords, Verminlord as Skaven-Daemon hybrid character

---
