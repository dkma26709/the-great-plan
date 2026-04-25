# §5 Stress and Morale


**Stress** represents accumulated psychological pressure on a unit — casualties, being targeted, losing ground. It is tracked as a counter that rises through the turn as triggers fire and falls via recovery and removal. When stress crosses a threshold, the unit enters a degraded state — **Shaken**, **Wavering**, or **Broken**.

There are no Leadership tests anywhere in the system — no pass/fail rolls against Ld. Stress accumulation is deterministic (triggers add fixed amounts); recovery introduces variability (D3 rolls). Whether a unit crosses a threshold depends on its stress count at the Start of Turn (after recovery), its Ld, recovery luck, and any modifiers from nearby characters. The same rules apply uniformly to multi-model units and single models (monsters, characters).

### Triggers

- **Losing a combat round:** +1 per point of combat difference (capped at +3). A Formed unit subtracts 2 from the combat difference before calculating stress (minimum 0).
- **Every 2 wounds lost in a single phase:** +1. Uniform across multi-model units (wounds = casualties) and single models (wounds = W lost).
- **Being a shooting target:** +1, once per Shooting phase. Applies whether or not casualties result; capped at once per phase regardless of how many enemies shot at the unit.
- **Targeted by an enemy spell:** +1, once per Magic phase. Applies only if the spell is successfully cast and not dispelled, whether or not it causes damage. Individual spells may inflict additional stress as part of their rules.
- **Being charged:** +1, once per charge declared against this unit. Additional stress from Psychology rules on the charging unit (Fear, Terror) applies separately via those rules' own triggers.
- **Friendly unit destroyed within 6":** +1, once per turn per affected unit (regardless of how many friendlies are destroyed nearby).
- **Friendly unit flees within 6":** +1, once per turn per affected unit. Applies to Broken units making mandatory flee moves and to voluntary flee reactions (e.g., Fast Cavalry's Flee reaction). Does **not** apply to disciplined withdrawals: fall-back from losing combat, Elusive's 2" reactive scramble, or normal movement away from an enemy.
- **General slain:** +2 to all friendly units on the table immediately, then +1 to all friendly units at the start of the following turn (the shock sets in). The General's Inspiring Presence aura is also lost — units that depended on it for rally access or threshold bonuses feel the absence immediately.

### Removal

- **Recovery** (natural): at Start of Turn, each unit rolls **D3** and removes that much stress. This is the base recovery roll; modifiers (musician, BSB, special rules) add to it.
- **Winning a combat round:** −1 stress to the winning unit(s).
- **Rally action:** the unit forgoes its Normal Movement activation and rolls **D3**, removing that much stress. Rally may only be used if the unit has a **Leader** (champion) alive or is within range of a General's Inspiring Presence, is not in combat (unless within range of Inspiring Presence), and is not Broken. See *Command Group and Stress* and *Characters as Morale Aids* below.

### Thresholds

A unit's state is determined by its current stress count relative to its Leadership:

| State | Stress at |
|-------|-----------|
| — | 0 up to (Ld − 5) |
| **Shaken** | Ld − 4 |
| **Wavering** | Ld − 2 |
| **Broken** | Ld |

For reference at base Ld values (no modifiers):

| Ld | Shaken | Wavering | Broken |
|----|--------|----------|--------|
| 7 | 3 | 5 | 7 |
| 8 | 4 | 6 | 8 |
| 9 | 5 | 7 | 9 |
| 10 | 6 | 8 | 10 |

### State Effects

| State | Effects |
|-------|---------|
| Shaken | −1 to hit (melee and ranged) |
| Wavering | −1 to hit, cannot charge |
| Broken | flees every Movement phase (full-M move directly away from the nearest enemy); attacks against the unit hit automatically (no to-hit roll required); enemies may engage a Broken unit by simply moving into weapon reach — no charge declaration needed |

States apply while the unit's stress is at or above the threshold. A unit whose stress drops below a threshold (via recovery, winning combat, or rally) loses the corresponding state at the next Start of Turn threshold check.

### Size Leadership Bonus

Larger units are inherently more resilient — more bodies, more cohesion, less vulnerability to individual panic. Based on **current** model count:

- **1–9 models:** base Ld
- **10–19 models:** Ld +1
- **20+ models:** Ld +2
- **Single models:** base Ld (no size modifier)

This raises the Shaken / Wavering / Broken thresholds by the same amount, so large blocks absorb considerably more stress before breaking than small units with the same base Ld. As a unit takes casualties, its size bonus may shrink — a 20-model unit reduced to 9 drops from +2 to base Ld, compounding its fragility.

### Characters as Morale Aids

Two character-level special rules anchor a unit's morale. Full definitions are in §8 *Special Rules Glossary* — *Leadership and Command*.

- **Inspiring Presence (X")** — the character raises Ld thresholds, enables rally (even in combat), and grants rerolls on recovery and rally rolls. The army general has Inspiring Presence (12") by default.
- **Battle Standard Bearer (X")** — the character gives +1 combat resolution and +1 to recovery/rally rolls. The army's Battle Standard Bearer has Battle Standard Bearer (12") by default.

The General and BSB serve different roles: the General is the morale backbone (enabling rally, rerolls, threshold bonuses), the BSB is a combat anchor (CR and recovery). Their effects stack. A unit within range of both benefits from Ld +1 thresholds, +1 CR, +1 to recovery/rally rolls, reroll on those rolls, and the ability to rally in combat.

### Stress-related Special Rules

Several rules in the special rules glossary (§8) modify a unit's stress behaviour — notably **Stubborn**, **Skittish**, **Unbreakable**, **Frenzy**, **Fear**, **Terror**, and **Immune to Psychology**. See §8 for definitions. Unit profiles list which rules apply.

### Command Group and Stress

The three command group roles — Leader, Standard Bearer, Musician — each contribute to a unit's stress resilience. These are upgrade options purchased during list building.

| Role | Stress effect |
|------|--------------|
| **Leader** (champion) | Enables the Rally action. A unit without a living Leader cannot rally — they are leaderless and must rely on natural recovery, winning combat, or external morale aids. |
| **Standard Bearer** | +1 combat resolution for the unit. A unit may include multiple standard bearers for redundancy, but the bonus is only +1 regardless of how many survive. If all standard bearers are slain, the bonus is lost. |
| **Musician** | +1 to all recovery and rally rolls (D3+1 instead of D3). |

The Leader's role is deliberately tactical, not combat-oriented. They are not necessarily a better fighter — their value is in holding the unit together under pressure. Losing a champion to a sniper, a challenge, or simple bad luck degrades the unit's ability to recover, compounding the effect of sustained pressure. This makes champion targeting a legitimate tactical play.

### Timing

Stress counters are recorded **throughout the turn** as their triggers occur — combat losses, shooting casualties, spell effects, charges, all add stress as they happen.

**Start of Turn** (next turn): two steps, in order:

1. **Recovery rolls.** Every unit rolls for recovery (D3 + modifiers). Stress counters are reduced accordingly.
2. **Threshold check.** Each unit's stress is compared against its Ld-based thresholds. States (Shaken, Wavering, Broken) are applied or removed based on the unit's current stress after recovery.

**Movement Phase** (immediately after): Broken units flee first, before any charges or normal movement are declared (see *Broken* in State Effects above).

This sequence means stress from the previous turn is not evaluated until the start of the next — giving recovery a chance to intervene before consequences take effect. A unit driven past its Broken threshold by a brutal combat may still steady itself if the recovery roll is good enough. Conversely, a unit that barely held together may slip into a worse state if recovery is poor. The uncertainty is deliberate.

---
