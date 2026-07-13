# Slaughterbrute

> Hulking Chaos beast of muscle and aggression, bound by ritual chains, branded with sigils of enslavement, and tied through marrow-deep magic to the will of a single Chaos Champion. "The Slaughterbrute is the epitome of violence and bloodshed kept tamed through means of ritual daggers and powerful magic. It possesses four front arms of differing sizes, a muscular body, a triplex tongue, and a massive head that contains a cluster of eyes and multiple rows of teeth. It possesses skin that is chitinous, creased and spiked, and the creature stands on hoofed feet." The binding ritual is long and arduous: "First, the beast is bound with magical chains, its flesh carved with runes of domination and branded with sigils of enslavement. Finally, daggers are soaked in the blood of the Chaos Champion who would be the beast's master." Through this bond, "a monster that would otherwise lash out with blind fury instead strikes with the skill of a warrior born" — the Master's combat training transmitted through the binding-runes into the bound beast's nervous system. **Bound**, the Slaughterbrute fights with the Master's skill. **Unbound** — when the Master is dead, far away, or otherwise unable to maintain the binding — the brute reverts to clumsy, frenzied rampage, lashing out at whatever moves. The lore signature is the **Bound** mechanic itself — the Slaughterbrute's combat profile *literally inherits* the Master's MA and MD when bound, capturing the marionette-puppet lore directly. Drafted here as a **Rare-slot Monster** with the Bound/Unbound state-switch as the identity rule; the **Master of the Slaughterbrute** Hero character (canon WAP) is deferred to a future Chaos character draft, with any friendly Chaos-keyword Character eligible to serve as the deployment-nominated Master in the interim.

## Profile

| M | MA | MD | BS | S | T | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|----|-----|----|
| 6 | 3 | 2 | 0 | 6 | 6 | 8 | 3 | 8 | 4 | =W |

**Points:** 178 per model *(framework derivation under §13: stat-baseline 20.5 + rules 9.5 + equipment 10.5 = 40.5 raw × wound factor 5.48 (W 8) × 0.8 scaling = 177.6 → 178. Sits below the Wild Terrorgheist (181 pts) and above the Wyvern mount-adder (+84 pts) — fitting the Slaughterbrute as a W 8 mid-to-upper Monster with state-dependent skill (MA 3 / MD 2 base; inherits Master's MA / MD when Bound). The W 8 wound factor (5.48) combined with NA 4+ (chitin shell, one step above standard Monster scales) gives the Slaughterbrute meaningful durability per pt invested. **Note: the base statline shows the Slaughterbrute's *Unbound* MA 3 / MD 2** — when Bound to a Master, the effective MA / MD scales with the Master's combat profile, which can reach MA 7 / MD 7 if Bound to a Chaos Lord. The framework price reflects an expected mix of Bound and Unbound states across a typical battle. See `design.md` for full working)*

**Unit size:** 1

**Unit type:** Monster (single model, no rider)

**Natural Armour:** 4+ (Scaly Skin — chitinous, creased, and spiked hide with runes of binding etched into the flesh; one step better than typical Monster scales, same tier as Kharibdyss chitin)

**Base Size:** 100mm × 75mm

**Keywords:** Chaos, Beast, Bound, Monster, Rare

## Equipment

- **Equipment:** Brutal Claws-and-Fangs (natural — four front arms of differing sizes, plus the toothy multi-row maw and triplex tongue, combined into a single multi-attack profile). No worn armour (the chitin IS the armour, captured in NA 4+), no shield, no rider, no missile weapon.

## Special Rules

- **Will of Chaos** *(Chaos faction-wide identity rule — per Chaos Warriors precedent)* — this unit is **Immune to Psychology** (per §8) AND may **reroll failed Recovery rolls**. The Slaughterbrute's chaos-touched biology is psychologically inert — external Terror, Fear, friendly-unit-destroyed-stress, and similar Psychology-tagged effects do not register. *Important interaction with Unbound state: see Bound/Unbound rule below — the Slaughterbrute's own Unbound Rampaging mandate is explicitly **NOT** a Psychology rule; Imm Psych does not suppress it.*
- **Terror** *(per §8)* — at LiS 4, the Terror aura projects to **(6 + 4)" = 10"**. Four-armed Chaos brute with a cluster of eyes, multiple rows of teeth, and chains rattling against chitinous spikes registers as terror on any battlefield.
- **Bound / Unbound** *(Slaughterbrute unit identity rule — Master-dependent state switch)* —
  - **At deployment**, after both armies have placed their forces, the Chaos player **nominates a single friendly Chaos-keyword Character model** as this Slaughterbrute's **Master**. The nomination is fixed for the battle (the binding-rune is etched at deployment, cannot be re-bound mid-game). A Slaughterbrute may have only one Master; only one Slaughterbrute may be bound to each Master. If no eligible Character is available at deployment, the Slaughterbrute begins the battle **Unbound** for the entire game (no Master to bind to).
  - **Bound state.** At the start of each Movement phase, check the Master's status. If the Master is **alive AND within 12"** of the Slaughterbrute (measured between any model in the Master's unit and the Slaughterbrute's base), the Slaughterbrute is **Bound** for this turn:
    - The Slaughterbrute uses the **Master's MA and MD** characteristics instead of its own base MA 3 / MD 2 (use the Master's current MA / MD as it appears on the Master's profile, including any temporary modifiers active on the Master at the time of the check).
    - **No Frenzy, no Rampaging** — the Slaughterbrute charges, targets, and disengages normally (per standard §4 / §6 rules).
    - The Master's combat skill is mechanically transferred through the binding-rune-marionette dynamic: the beast's strikes are the Master's strikes, channelled through the brute's body.
  - **Unbound state.** If the Master is dead, removed from play, or further than 12" at the start of any Movement phase, the Slaughterbrute is **Unbound** for this turn:
    - Uses its base **MA 3 / MD 2**.
    - Gains **Frenzy** *(per §8 — +1 A, +1 MA, -1 MD, must charge nearest visible enemy, may not voluntarily disengage, must pursue, Immune to Psychology, suppresses Wavering/Broken state effects)*. Effective stats while Unbound + Frenzied: MA 4 / MD 1, A +1 on weapon profile, mandatory combat behaviours.
    - Gains the **Rampaging** sub-state (Slaughterbrute-specific):
      - At the start of the Slaughterbrute's activation in the Movement phase, the controlling player must take one of the following actions, and nothing else, that phase:
        - **Charge** the nearest visible enemy within charge range (must declare the charge if eligible), OR
        - **Advance** its full M directly toward the nearest visible enemy (in any direction — the Slaughterbrute may wheel and pivot freely toward the chosen target), OR
        - If no enemy is visible, **Advance** its full M in a randomly-determined direction (roll the scatter die; if "hit," choose any direction).
      - The Slaughterbrute may not March, may not Rally unless required by Broken status, may not voluntarily target friendly units (it lashes at the *nearest visible enemy*, never friendly).
    - **Rampaging is NOT a Psychology rule** — it's a Slaughterbrute-specific identity rule that captures the brute's primal nature breaking through the chaos-discipline. **Will of Chaos's Immune to Psychology does NOT suppress Rampaging** — the beast's wild biology is more fundamental than its chaos-discipline. Frenzy's Imm Psych similarly does not block Rampaging (Frenzy's Imm Psych blocks Fear / Terror, not unit-specific identity rules).
  - **Re-binding mid-battle.** If the Master dies and the Slaughterbrute becomes Unbound, the Unbound state is **permanent** for the rest of the battle (the binding-rune is broken, cannot be re-established without the deployment ritual). If the Master is merely out of range and later re-enters within 12", the Slaughterbrute re-enters Bound state at the start of the next Movement phase.
  - **Lore-direct expression:** "Under such dominion, a monster that would otherwise lash out with blind fury instead strikes with the skill of a warrior born." The binding-rune carries the Master's combat training into the bound beast; without the binding, the beast is just a clumsy four-armed brute with too many teeth.

## Weapon Profiles

### Close Combat

- **Brutal Claws-and-Fangs** *(natural — four front arms of differing sizes, plus the toothy multi-row maw and triplex tongue combined into a single profile)* — **1" reach | A 5 | S 6 | AP -1 | D D3** — the Extra Claws identity rule, baked into the high attack count. Five strikes per Combat round across the four arms (some arms swinging multi-times) and the maw. **S 6** wounds T 3 on 2+, T 4 on 3+, T 5 on 3+, T 6 on 4+; **AP -1** strips light armour. **D D3** delivers 1-3 wounds per unsaved wound (average 2). When **Bound**, the Slaughterbrute hits at the Master's MA (typically 5-7 against MD 3 = 2+ to-Hit baseline). When **Unbound**, the Slaughterbrute hits at MA 3 + Frenzy +1 = MA 4 (vs MD 3 = 3+ to-Hit), still useful but less consistent. The Extra Claws / multi-arm anatomy is the source of the high attack count; no separate sub-weapon profile. `[Natural]`
