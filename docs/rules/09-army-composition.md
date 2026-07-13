# §9 Army Composition


> **Design principle:** every army is a themed host, not a vanilla roster. The category chassis (Lords / Heroes / Core / Special / Rare) is uniform across factions — identity lives in *which units sit in which category*, and that assignment is the job of the **Army of Infamy** (AoI). Characters tune the assignment further, so mount and equipment choices become list-shaping decisions rather than pure stat selections. Pillar 7 of the design — no army archetype is inherently weaker — rests on AoIs being able to reshape composition freely, so a mono-monster or pure-shooting host is a valid way to play a faction, not a malformed version of the default.

### 9.1 Categories

An army is divided into five categories. Each AoI defines its own Composition Table; default constraints across most AoIs are:

| Category | Default constraint | Notes |
|---|---|---|
| **Lords** | Maximum **25%** of army points | No per-character count limit — multiple of the same Lord type are permitted within the points cap |
| **Heroes** | Maximum **25%** of army points | Same — no per-character count limit |
| **Core** | Minimum **25%** of army points | The faction's rank-and-file backbone |
| **Special** | Maximum **50%** of army points | Elite and specialist units |
| **Rare** | Maximum **25%** of army points | Apex units; signature monsters and unique assets |

- **Lords** — the most powerful commanders of the faction.
- **Heroes** — lesser characters, lieutenants, and exceptional individuals above line-officer level.
- **Core** — rank-and-file infantry, standard cavalry, the faction's most numerous units.
- **Special** — elite and specialist units: shock cavalry, veterans, heavy infantry, war beasts, unusual troop types.
- **Rare** — apex units: signature monsters, unique constructs, the faction's most unusual or powerful assets.

Categories are the **chassis**. Which of a faction's units sit in which category under any given list is decided by the AoI. AoIs may tighten or loosen the default constraints.

### 9.2 Armies of Infamy

Every list must be built under an **Army of Infamy**. Each faction has a **Default AoI** — its classic, unthemed army list, with canonical category assignments and standard ratios. Beyond the default, each faction carries a handful of themed AoIs representing famous hosts, regional variants, narrative alliances, or subfactional traditions.

An AoI defines:

- **Composition Table** — minimums and maximums per category (default: Lords 25% max, Heroes 25% max, Core 25% min, Special 50% max, Rare 25% max — see §9.1). AoIs may diverge from the defaults to enforce their theme.
- **Category assignments** — which of the faction's units sit in each category under this AoI.
- **Army-wide rules** — 0–2 special rules applied to the entire list.
- **Mandatory picks** — 0–2 units that must appear.
- **Banned picks** — 0–3 units that cannot appear under this AoI.
- **Optional — magic lore restriction.** Some AoIs lock, unlock, or substitute spell lores.
- **Optional — named hero unlock.** A unique character available only under this AoI.

Two AoIs of the same faction may differ dramatically. One may require a Core-heavy horde and ban apex monsters; another may open Rare to 50% and make a signature monster Core. Cross-faction unit sharing is the exception: where an AoI draws units from another faction, it is at most **one** partner faction, and the partnership must be justified in the AoI's narrative description.

### 9.3 Character Shifts

Most characters in an army represent a real choice — different mounts, roles, equipment, name-level individuals. To reflect this, characters may carry a **shift rule** that tunes the AoI's category assignments. Whether a character carries a shift, and of what form, is decided on a per-faction basis; not every character has one. As a guideline, mount variants, named characters, and Lord-tier commanders are the natural candidates.

Shifts come in two forms.

**Per-unit shift** — the common form. Attached to a specific character variant. Makes *one* unit of a listed type count as a lower category while that character is in the army.

> *Scar-Veteran on Aggradon — Lead from the Saddle:* one Aggradon Lancers unit in your army counts as Core instead of Special while this model is in your list.

Per-unit shifts **stack across characters**. Two Scar-Veterans on Aggradons produce two Aggradon Lancers units that count as Core.

**Blanket shift** — reserved for Lord-tier characters whose presence re-homes a unit type wholesale.

> *Slann Mage-Priest — Ancient Authority:* while this model is in your army, Temple Guard count as Core.

All units of the shifted type change category at once. Blanket shifts are binary: they apply or they do not.

**Direction of shift.** Character shifts only move units *down* the category ladder — Rare → Special, Special → Core. Characters never promote, restrict, or ban units upward. Upward restrictions, bans, and mandatory picks are the job of the AoI, not the character.

**Order of resolution.** Start with the AoI's category assignments. Apply all blanket shifts first, then per-unit shifts. A per-unit shift takes effect only if, after blanket shifts, the unit would still sit in the higher category.

### 9.4 List-Building Procedure

1. **Choose a faction.**
2. **Choose an Army of Infamy** from that faction. The Default AoI is always available.
3. **Note the AoI's parameters** — Composition Table, category assignments, army-wide rules, mandatory and banned picks, lore or character restrictions.
4. **Build the list to the agreed points total**, obeying the AoI's ratios and assignments.
5. **Apply character shifts.** For each character with a shift rule in the list, adjust the category of the indicated unit(s) — blanket shifts first, then per-unit shifts.
6. **Verify the final list** against the Composition Table after all shifts are applied. Shifted units count in their new category for min/max purposes.

---

## 9.5. Battles

> **Design principle:** A baseline framework for setting up and resolving a game — board, terrain, deployment, scenario, victory. The aim is "playable enough to start" rather than a finished tournament packet. Specific scenario packs, narrative campaign rules, and competitive matched-play conventions are deferred. What's here is what two players need to put models on the table and have something to play for.

### Battlefield Setup

**Standard board.** 6' × 4' (72" × 48") for full-scale battles (1500-2500 pts). Smaller engagements (≤1000 pts) play comfortably on 4' × 4' (48" × 48"). Larger games (>2500 pts) extend to 6' × 6'.

**Terrain density.** A standard battlefield carries **6-10 terrain features**, occupying roughly 20-30% of the board area. Heavier terrain is permitted (jungle, urban) but should be agreed by both players in advance. Open battlefields with fewer than 4 features risk one-dimensional play; over-cluttered boards risk terrain-locking entire armies. Terrain features and their effects (movement, line of sight, combat) are defined in **§6.5 Terrain**.

**Terrain placement.** Three options, in order of preference:

1. **Pre-set table** — players agree the terrain is what's on the table (clubs, demo tables, fixed narrative maps).
2. **Alternating placement** — each player places one terrain feature in turn, starting with the player who lost the roll-off below. Features must sit at least 6" from any board edge and 6" from any other feature unless mutually waived.
3. **D6 per quadrant** — divide the board into quadrants. Each quadrant rolls D6 to determine number of features (1-2: 1; 3-4: 2; 5-6: 3), drawn from an agreed pool.

**Roll-off.** Both players roll D6. Higher result chooses one of: **active player on Turn 1** (declares first in alternating phases) *or* **second-deploy** (places second under alternating deployment). The other choice falls to the opponent. Re-roll ties.

### Deployment

**Standard zones.** Each player's deployment zone extends **12" inward from their long edge**, leaving a 24" no-man's-land. Specific scenarios may modify zones (Meeting Engagement reduces to 6", etc.).

**Alternating placement.** The player who lost the roll-off (or chose second-deploy) places their first unit. Players then alternate placing one unit at a time — units, not models — until both armies are deployed. A player who finishes first may declare *passes* on remaining alternations and watch the opponent finish.

**Character placement.** A character that joins a unit (per §6 *Character Attachment Exception*) deploys with that unit, in the same alternation slot. A lone character deploys as its own unit-slot.

**Scouts and Vanguard.** Per §8. Scouts deploy *after* all standard deployment is complete. Vanguard deploys *during* standard deployment, in the deploying player's slot, up to **M** outside the deployment zone (and ≥12" from any enemy already deployed).

**Ambushers.** Per §8. Held in reserve; not placed during deployment. Arrival is rolled per Turn (see §8 *Ambushers*).

**Re-deploys.** None permitted under standard rules — once a unit is placed, it stays. Specific scenarios or AoIs may grant a re-deploy as a faction-specific rule.

### Game Length

Standard games run **5 turns**. Scenario rules may extend (6 turns for objective-heavy missions) or shorten (4 turns for fast Meeting Engagements).

A turn is **one cycle** through the six phases (§7), with both players acting alternately within each phase. After the final turn's End of Turn step, the game ends and victory is determined per the scenario.

### Scenarios

Three baseline scenarios. Players agree before deployment, or roll D3.

#### Scenario 1: Pitched Battle

> The classic head-on engagement. Two armies arrive on a contested field with the simple intent of breaking the enemy. No objective beyond destruction.

- **Deployment:** standard 12" zones along long edges
- **Game length:** 5 turns
- **Victory:** highest total **Victory Points (VP)** at end of game
  - Each enemy unit **destroyed** (all models removed): full unit cost in VP
  - Each enemy unit at **half strength or less** at game end (current model count or current W ≤ half starting): half unit cost in VP
  - Enemy **General slain**: +200 VP bonus
  - Enemy **Battle Standard Bearer slain**: +100 VP bonus
- **Draw:** within 100 VP of each other

#### Scenario 2: Take and Hold

> Three positions of significance — a shrine, a watchtower, a crossroads. Hold them and the field is yours.

- **Setup:** before deployment, place **3 Objective Markers** along the board's centre line — one at the centre, one 18" to each side. Each marker is a 1" disk (a coin works)
- **Deployment:** standard 12" zones
- **Game length:** 5 turns
- **Holding an objective:** a marker is **held** by the player with greater **total US within 3"** of the marker. A unit must be neither Broken nor fleeing to count. Equal US (or zero on both sides) means **contested** — neither player holds it
- **Scoring:**
  - At the **end of each turn from Turn 2 onward**, each held marker scores **+100 VP** to its holder. Cumulative across turns
  - At **end of Turn 5** (game end), each held marker scores **+200 VP** instead of +100 — the final position is what matters most
  - **Annihilation also scores:** add destroyed-unit VP (full / half / general / BSB) per Pitched Battle
- **Draw:** within 100 VP

#### Scenario 3: Meeting Engagement

> Two armies collide unexpectedly along a march. Forces are scattered, the centre is open, and reinforcements trickle in as the fight develops.

- **Deployment:** **6" zones** along long edges (smaller than standard). Each player **deploys only half their army** by points value (rounded up to the nearest unit) at the start; the remainder is held in reserve
- **Reserves:** at the start of **the Movement phase from Turn 2 onward**, each player rolls D6 for each of their reserve units. The unit arrives on **3+ on Turn 2**, **2+ on Turn 3**, **automatic on Turn 4+**. Place arriving units in base contact with the player's own long edge, at least **12" from any enemy model**, in a legal formation facing inward. The unit may not declare a charge on the turn it arrives
- **Game length:** 5 turns
- **Victory:** Pitched Battle scoring (destroyed-unit VP + general/BSB)
- **Draw:** within 100 VP

> **Future expansion.** This baseline is deliberately small. Future scenario packs may add: narrative-driven asymmetric scenarios (one army defends, the other attacks), king-of-the-hill (single objective, escalating points), random battlefield events, magical / supernatural board hazards, and matched-play tournament packets with objective-track scoring. Drafted as needed; not blocking playtest.

---
