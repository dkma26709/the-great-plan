# §1 The Stat Line

| Stat | Abbr | Description |
|------|------|-------------|
| Movement | M | Base movement in inches |
| Weapon Skill | WS | Melee combat ability |
| Ballistic Skill | BS | Ranged combat ability |
| Strength | S | Raw hitting power |
| Toughness | T | Physical resilience |
| Wounds | W | Damage each model can absorb — used freely for flavour, not locked to 1 for infantry |
| Initiative | I | Determines strike order in combat |
| Leadership | Ld | Resistance to stress and morale effects |
| Line of Sight | LiS | Size/visibility for LoS calculations (see §7.4) |
| Unit Strength | US | Physical presence and mass of one model. See below |

**Attacks are a weapon property, not a stat.** The number of attacks a model makes is defined per-weapon on the weapon profile, not on the stat line. A model with three weapon profiles (e.g., a Monster's natural weapons plus a howdah-mounted ranged weapon) has three independent Attack values. This keeps multi-weapon units cleanly expressible and prevents double-counting across attack modes. When a weapon is used, the model makes the Attacks listed on that weapon's profile, resolved at the weapon's own S, AP, D, and any special rules.

## Armour and Protection (separate from stat line)

| Stat | Description |
|------|-------------|
| Armour Save (AS) | Base save from armour and natural scales |
| Ward Save (WS) | Unmodifiable save (magical protection, blessed, etc.) |

## Magical Profile (wizards only, separate from stat line)

| Stat | Abbr | Description |
|------|------|-------------|
| Cast Base | CaB | Fixed Cast Dice contributed to the wizard's personal Cast pool each Magic phase |
| Dispel Base | DiB | Fixed Dispel Dice contributed to the wizard's personal Dispel pool each Magic phase |
| Channeling | Ch | Number of D6s the wizard rolls at phase start; each result of **5+** generates one extra die, placed (player's choice) into this wizard's Cast *or* Dispel pool |
| Cast Bonus | CB | Modifier to cast rolls. Total effective CB from all sources is capped at **+5** |
| Dispel Bonus | DB | Modifier to dispel rolls. Total effective DB (lead wizard + supporter contributions + item/spell bonuses) is capped at **+5** |
| Dispel Range | DR | Maximum range at which a wizard may act as lead dispeller or contribute dice to a dispel |
| Lore Access | LA | Highest spell tier accessible, per lore |

See §7.3 (Magic Phase) for full rules.

## Unit Strength (US)

Unit Strength represents a model's **physical presence and mass**. It is a stat-line characteristic, independent of Wounds (which is durability) and LiS (which is visibility). Each model contributes its US to its unit — a unit's **total US** is the sum of all surviving models' US values, updated dynamically as casualties are removed.

**What US does:**

1. **Combat resolution wound totals.** Each model killed contributes its US, not 1, to the CR wound tally. A Kroxigor (US 3) killed in combat adds 3 CR wounds. A Stegadon (US 5) killed adds 5. A Saurus (US 1) adds 1.

2. **Objective and presence calculations.** Scenarios scored by "controlling an objective" or "holding a zone" count **total US** on the point, not model count. A Dragon (US 5) controls a courtyard more decisively than three Skinks (US 3) huddled on it. Physical presence scales with mass.

3. **Rule gating by scale.** Some rules gate their effects on a US threshold rather than enumerating type keywords (e.g., Flaming's beast-panic triggers on US 2+; Killing Blow can target models with US ≤ 2 for anti-infantry or US ≥ 3 for anti-large). More scalable than listing types.

**US is not tied to Wounds.** A multi-wound hero (W4 Scar-Veteran) still has US 1 — he's one bloke, however tough. A Monster with many wounds has high US because of its mass, not because of its durability.

**US and Degrading.** Monsters with the Degrading rule may have US on their damage table, decreasing as wounds are lost. A wounded Stegadon is a smaller presence than a healthy one — less imposing on the battlefield, contributes less to objectives, and its death counts for fewer CR wounds.

**Monster US = current W.** As a convention, Monster-keyword units have **US equal to their current remaining Wounds** rather than a fixed value. A full-strength Monster contributes its maximum W as US; a heavily-wounded Monster contributes proportionally less. This is a smoother version of the tier-based US-degrading pattern — the wound pool directly reads as battlefield presence.

**Characters and command US.** A character model adds **+1 US** to the typical value for its type (a foot character on an Infantry chassis starts at US 2 rather than 1; a Cavalry character at US 3; a Monster-mounted character at US 6). The army **general** adds a further **+1 US** on top, reflecting command gravity — a foot general is US 3, a mounted general US 4, a monster-mounted general US 7. These are baseline values; individual character profiles may override them for specifically thematic reasons.

## Unit Types

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
| **Swarm** | A mass of small creatures fighting as a single unit — rats, bats, spiders, insects. | 0 | 5 |

**One type per unit.** If mounted, the mount determines the unit type — Skinks on Cold Ones are Cavalry even though the riders are Skink-sized.

**Type vs LiS are independent.** The "typical" LiS column is guidance, not binding. A small but monstrous creature may be tagged Monster with LiS 2 if thematic; an unusually large humanoid may be tagged Infantry with LiS 2. LiS is an independent stat that rules reference alongside type keywords.

**Swarms are a special case.** A Swarm base's **US is dynamic** — equal to its **current remaining Wounds**, not a fixed value. As the swarm takes damage its mass on objectives diminishes in real time.

## Rider and Mount Profiles

Units whose models consist of a rider and a mount (Cavalry, Monstrous Cavalry, Chariot, Monster-mounted characters) display **two profiles** on their unit card — one for the rider and one for the mount. Rider and mount are a single model for casualty purposes; their profiles combine contextually per the table below.

| When resolving... | Use... |
|-------------------|--------|
| **Movement** | The **mount's M** |
| **An attack the model makes** | The profile of the part performing the attack — rider's WS/S/I/A for rider's weapons; mount's for mount attacks. Each strikes at its own Initiative step |
| **An attack against the model** | Attacker's to-hit uses the **highest WS** of rider or mount. To-wound uses the **highest T** |
| **Armour save** | The model's combined save (natural armour from the mount + any worn armour + shield), per §8 Armour Save Stacking |
| **Wounds** | **Pooled** — the model's wound pool equals rider's W + mount's W. When the combined pool reaches zero, the model is removed |
| **Leadership and stress** | The **rider's Ld** (the rider commands the mount); stress is tracked at the unit level |
| **LiS, US** | Listed on the unit-level entry (not per-profile) — representing the combined model's size and mass |

## Unit Keywords

Every unit profile carries a **keyword line** — a list of tags that identify the unit for the purpose of rules that target categories of units rather than specific profiles. Keywords let effects say "any Saurus unit" or "any Core unit" or "any Monster" without listing every profile that qualifies.

**Keyword categories:**

| Category | Examples |
|----------|----------|
| **Faction** | Lizardmen (Seraphon is an AoS-specific alias; "Lizardmen" is the canonical faction keyword) |
| **Sub-faction / race** | Saurus, Skink, Kroxigor, Slann |
| **Unit type** | Infantry, Cavalry, Monstrous Infantry, Monstrous Cavalry, Warbeast, Monster, Chariot, Swarm |
| **Role** | Core, Special, Rare, Hero, Lord (army-composition categories for list building) |
| **Descriptive** | Situational tags for narrow rule hooks — e.g., Aquatic, Mounted, etc. |

A typical keyword line for a Saurus Warriors unit: `Lizardmen, Saurus, Infantry, Core`.

**Effects reference keywords directly.** A spell text reading "all friendly Lizardmen units within 12" gain +1 to hit" applies to any friendly unit with the Lizardmen keyword — including characters, core, rare, monsters, etc.

Keywords are **static** — printed on the profile, not gained or lost in play — unless a rule explicitly adds or removes one.

## Mixed Unit

A unit whose composition includes models of two or more distinct profiles — e.g., a Warbeast accompanied by a fixed pool of Handler support models, a crew-served weapon with its Crew, a Chariot with a Rider and a Driver. Both profiles appear on the unit card; each model uses its own profile when attacking or being attacked.

**Wound allocation.** Wounds inflicted on a Mixed Unit are applied to the **supporting profile** (Handlers, Crew, etc.) first. Only once all supporting models are removed may wounds be allocated to the **primary profile**.

**Movement and coherency.** All models move together as a single unit. The **primary profile sets the unit's M**. Supporting models must remain within **2"** of a primary model at the end of any move; a supporting model isolated from all primary models is removed as a casualty.

**If all primary models are destroyed**, any remaining supporting models are also removed and the unit is destroyed. Supporting models cannot outlive their primaries.
