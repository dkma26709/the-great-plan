# Stormvermin

> *"Only a Skaven with black fur is elevated to the ranks of the Stormvermin."* The Stormvermin are the elite warriors of **Clan Mors** and equivalent Greater Clans — the apex Mors infantry tier, **raised from infancy to be the most deadly killers and soldiers in the entire Skaven horde**. Where the Clanrat is the species's expendable mass-conscript, the Stormvermin is its drilled veteran: faster on the strike (I 5), better-armed and better-armoured, drilled-from-infancy combat-reflexes (**Killer Instinct** — reroll to-Wound 1s in melee), and uniquely **Disciplined** — the rare Skaven exception to the species's Undisciplined rabble baseline. The Stormvermin's body is still the same fragile Skaven T 3 frame as the Clanrat — the species's biological limit holds at the elite tier; what elevates the Stormvermin is *training*, *gear*, and *combat reflex*, not toughness. Their dark coat is the iconic identifier: black-furred Skaven from the natural-selection pool of the warrens, *given the best food and gear available to them.* The fingerprint: an apex-Mors veteran block at the **elite Infantry tier** — Disciplined (+1 Recovery), **Killer Instinct** (the Stormvermin's drilled-killer reflex, captured as melee to-Wound reroll-1s), Verminous Valour (mass-bravery / cowardice toggle), Strength in Numbers (CR bonus from mass), Backstabbing (panic-cascade externality). The default kit is comparatively modest — **Hand weapon + Shield + Medium armour** (combined save 4+) — reflecting the Mors Warlord's frugal arms-issue even at the elite tier; the *better-equipped* sub-tiers (Halberd-armed strike block, Heavy-armour bodyguard formation) are kit upgrades. Stormvermin fight in formed blocks like Clanrats but smaller and tighter — typically 10-20 model regiments rather than the 30-40 mass-blob of Clanrats. The role: the Mors army's *hammer* to the Clanrat *anvil* — the elite formation that holds the line, anchors a flank, or punches a hole in an enemy block when the throwaway Clanrat wave fails.

## Profile

| M | MA | MD | BS | S | T | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|----|-----|----|
| 5 | 4 | 4 | 3 | 3 | 3 | 1 | 5 | 7 | 1 | 1 |

**Points:** 11 per model *(framework derivation under §13: stat-baseline 8.0 + rules ~3.2 (Disciplined +1.0 + Killer Instinct +0.7 + Verminous Valour +1.0 + Strength in Numbers +0.5 + Backstabbing 0 externality) + equipment ~2.5 (HW + Shield + Medium armour = 4+ save) = 13.7 raw × wound factor 1.0 (W 1) × 0.8 scaling = 10.96 → 11 pts; see `design.md` for full working)*

**Unit size:** 10+ (Stormvermin units are smaller and tighter than mass-tier Clanrat blocks; the elite Mors veteran doesn't need 25-model rank-stacks to function)

**Unit type:** Infantry

**Natural Armour:** —

**Base Size:** 25mm × 25mm

**Keywords:** Skaven, Under-Empire, Clan Mors *(default flavour-tag; sub-clan keyword adjustable at list-build)*, Stormvermin, Infantry, Special

## Equipment

- **Worn armour (default):** Medium armour + Shield (combined save **4+** per §8 *Armour Save Stacking* — medium 5+ → +1 step from shield = 4+)
- **Equipment (default):** Hand weapon + Shield + Medium armour

## Special Rules

- **Disciplined** *(per §8 Psychology)*. **+1 to Recovery rolls.** The rare Skaven exception to the species's Undisciplined baseline. Stormvermin are drilled from infancy — formation discipline holds where Clanrat blocks scatter. Lore-canonical: *"raised from infancy to be the most deadly killers and soldiers in the entire Skaven horde."*
- **Killer Instinct** *(Stormvermin unit identity rule)*. A model in this unit may **reroll to-Wound rolls of 1 in melee**. The Stormvermin's drilled-from-infancy killer reflex: every blow is aimed to wound, not merely engage; the rare roll that finds no purchase is *re-attempted* with the veteran's instinct. Mechanically parallel to Druchii **Murderous Prowess** (per §8 *Combat*) but unit-specific to Stormvermin rather than faction-wide. Per the standard reroll-once convention, the "1" is the **unmodified** natural die face; the reroll triggers regardless of any +/- modifiers that would have applied. The reroll cannot itself be rerolled. *(Lore-canonical: the apex Mors warrior is "the most deadly killer in the entire Skaven horde" — drilled, fed, and gear-equipped to ensure every strike finds flesh. Mors Warlords cultivate this killer instinct from the moment a black-furred whelp is identified in the warrens.)*
- **Verminous Valour** *(Skaven faction-wide identity rule — working title; pending §8 promotion)*. **Mass-bravery / cowardice toggle, single threshold at half strength:**
  - While this unit has **more than half** its starting model count remaining (e.g., 6+ out of a 10-strong unit), it **ignores the state effect of Shaken** (per §8).
  - While this unit is reduced to **half or fewer** of its starting model count, it accumulates **+1 additional stress** every time it would normally take stress.
  
  *(Per §1.5 Skaven faction-wide trait — applies identically to Clanrats and Stormvermin. Stormvermin's Res 7 baseline makes the cowardice threshold less catastrophic than for Clanrats Res 5, but the rule still fires.)*
- **Strength in Numbers** *(Skaven faction-wide identity rule — working title; pending §8 promotion)*. **Combat resolution bonus from raw model count — formation shape irrelevant:**
  - **+1 to CR** while this unit has **≥ 15 models** remaining.
  - **+2 to CR** while this unit has **≥ 25 models** remaining.
  
  *(Per §1.5 Skaven faction-wide trait. Rarely fires on Stormvermin units in practice — typical block size 10-15 models means the +1 threshold sometimes triggers, +2 almost never. The rule is faction-wide, but Stormvermin doctrine relies on Discipline + Halberd + 4+ save for combat resolution, not on Skaven mass.)*
- **Backstabbing** *(Skaven faction-wide identity rule — working title; pending §8 promotion)*. When this unit is **Broken** (per §5), every friendly **Skaven** unit within **6"** of any model in this unit immediately gains **+1 stress** beyond the standard panic-cascade. *(Per §1.5 Skaven faction-wide trait. Stormvermin Breaking is *more* damaging to allies than Clanrat Breaking — the elite-tier rout signals to the rest of the army that "even the best are running," compounding panic. The rule applies symmetrically as the Skaven faction externality.)*

## Options

**Worn armour upgrade option:**
- **Heavy armour** (+1.5 pts/model) → upgrades Medium → Heavy. Combined save becomes **3+** (heavy 4+ → +1 step from shield, or 4+ → 3+ marginal step per §8 *Armour Save Stacking*; per Dwarf Warriors heavy-armour-marginal precedent). The Mors veteran's hard-plate variant; favoured by Warlord-bodyguard Stormvermin units.

**Equipment swap option (replaces Hand weapon, pick at most one):**
- **Halberd** (+1 pt/model) → 2" reach, A 1, S+1 (= S 4), AP -1, D 1 (per Empire Halberd precedent in §13.4 Equipment Table). The cavalry-and-line-fighting polearm; lets second-rank Stormvermin strike alongside the front rank, and the +1 S / AP -1 spike makes Stormvermin meaningfully more dangerous in melee. May still pair with Shield. *(Note: the Halberd is 1H with Shield in our system per Empire Halberdier precedent — the project diverges from WHFB 8e canonical 2H Halberd to keep the Halberd-and-shield "Royal Guard" kit accessible.)*

**Combined upgrade — "Mors Royal Guard" loadout** (Halberd + Heavy armour + Shield at +2.5 pts/model = 14.5 pts/model effective): the Stormvermin's apex-kit configuration. 3+ combined save (heavy armour 4+ + shield → 3+) plus Halberd S 4 / AP -1 / 2" reach. The Warlord's personal-guard loadout, expensive but mechanically the apex Mors warrior in a non-character infantry frame.

**Command options:**
- **Fang-Leader (Leader)** (+5 pts) — Stormvermin veteran, the unit's drillmaster and champion. Functions as the unit's champion for Rally / challenge / Leader-snipe purposes.
- **Standard Bearer** (+8 pts, may take Magic Standard up to 50 pts — elite-tier banner budget). The Mors black-and-red banner, or sub-clan equivalent.
- **Musician** (+5 pts) — clan-drummer or piper; provides +1 to Recovery and Rally rolls.

## Weapon Profiles

### Close Combat

- **Hand weapon** *(default, 1H — pairs with Shield)* — 1" reach | **A 1** | S 3 | AP 0 | D 1 — Stormvermin-craft scimitar or short sword; better-forged than the rusted Clanrat blade but still a baseline 1H weapon. `[1H Blade]`
- **Halberd** *(option, 1H — replaces Hand weapon, may pair with Shield)* — 2" reach | **A 1** | S+1 (= S 4) | AP -1 | D 1 — the Mors veteran's polearm; cavalry-and-line-fighting reach, with the +1 S / AP -1 spike that defines the Halberd-class weapon across factions. Lets the second rank participate in melee. `[1H Reach]`
