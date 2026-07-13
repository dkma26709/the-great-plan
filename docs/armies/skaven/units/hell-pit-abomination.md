# Hell Pit Abomination

> The masterwork horror of Clan Moulder — the flesh-shaper guild of the Under-Empire. Standing taller than eight men, the Hell Pit Abomination is a *stitched* monstrosity: claws, jaws, limbs, eyes, and warp-driven mechanical augmentations crudely combined from whatever the Moulder vat-masters had on hand. "This grotesque mutant creature is a mass of deformed flesh, moving with unnatural spasms. The Hell-Pit Abomination features several mechanical components, with wheels, cogs, and fluid pumps embedded into the beast to enhance its mobility and speed, and these parts also aid in the consistent injection of warpstone mutated growth agents." No two Abominations are alike — each is the unique product of whatever atrocity Moulder's Pack Masters last assembled. The lore signature is twofold: **Too Horrible to Die** *(when killed, the warpstone-mutated flesh refuses to remain dead — D6 roll on death: 1-2 dies permanently, 3+ regenerates at full W; the only catch is that **all stats degrade by 1** each rebirth, so the Abomination slowly diminishes into a less-and-less-coherent flesh-amalgam)* and the **dual-weapon stitched-body** *(Massive Claws + Whirling Death — the Abomination has too many limbs to count, attacking with both heavy crushing strikes and a multi-armed flailing whirl)*. **First Skaven unit drafted in the codebase** — establishes the apex Skaven Monster reference for future Skaven faction expansion. The Under-Empire battlefield read: send the Abomination into the enemy line, accept that it might die 3+ times before going down for good, and watch as each successive rebirth makes it weaker until eventually the Pack Masters' last warpstone-injection fails.

## Profile

| M | MA | MD | BS | S | T | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|----|-----|----|
| **Random** *(4D3")* | 3 | 3 | 0 | 6 | 5 | 12 | 2 | 5 | 5 | =W |

**Points:** 310 per model *(framework derivation under §13: stat-baseline 16.0 + rules 7.5 + equipment 10.0 = 33.5 raw × wound factor 11.56 (W 12) × 0.8 scaling = 309.9 → 310. **Pass 2.2 (2026-05-18):** Random Movement changed from 3D6 → **4D3** (caps mobility at 12" vs the previous 18" ceiling; mean 8" vs 10.5"; lower variance, more gradual degradation curve across rebirths). **Pass 2.1:** Movement characteristic replaced with Random Movement; rebirth roll restructured (1-2 die / 3-4 half W / 5-6 full W); W max does not degrade. No net pricing change from Pass 2.1's +310 — the lower mean of 4D3 offsets the lower variance. See `design.md` for full working)*

**Unit size:** 1

**Unit type:** Monster (single model, no rider)

**Natural Armour:** 5+ (warpstone-fused flesh-and-mechanical hide — the Abomination's body is stitched together with iron plates, cogs, and warpstone-infused tissue. Mid-Monster armour tier)

**Base Size:** 50mm × 50mm (the Abomination is *tall* — taller than eight men per lore — but the base footprint is moderate; the model's height is captured in LiS 5 and the Terror radius)

**Keywords:** Skaven, Clan Moulder, Warpstone-Touched, Monster, Rare

## Equipment

- **Equipment:** Massive Claws (natural — multiple oversized clawed limbs) + Whirling Death (natural — additional flailing limbs and tooth-mouths) + warpstone-injection apparatus (lore-only flavour; not a separate weapon). No worn armour, no shield, no rider.

## Special Rules

- **Terror** *(Psychology — per §8)* — at LiS 5, the Terror aura projects to **(6 + 5)" = 11"**. The Abomination is a horror to behold — a writhing mass of flesh, teeth, and warpstone-fused mechanical components. Most enemy soldiers have never seen anything like it and recoil from the sight.

- **Random Movement** *(per §8 — Pass 2.1 replaces the M characteristic; Pass 2.2 tuned to 4D3)* — The Hell Pit Abomination doesn't *walk* — it spasms, lurches, and rolls forward in unpredictable bursts driven by the warpstone-injection pumps. At the start of each Movement phase, **roll the Abomination's Random Movement dice** (initially **4D3"**, reduced with each rebirth — see Too Horrible to Die below):

  - The result is the Abomination's total movement for this Movement phase. **Range: 4" minimum to 12" maximum, mean ~8".**
  - The Abomination must move *toward the nearest visible enemy*, by the rolled distance, in as close to a straight line as positioning allows. The player controls minor deviations to avoid friendly units / impassable terrain, but cannot deliberately choose direction.
  - The Abomination cannot March (the Random Movement *is* its full movement).
  - If the Abomination cannot move (no visible enemy, blocked completely by terrain), it stays in place for that turn.
  - Charging: the Random Movement roll *is* the charge range when the Abomination charges. It may charge any enemy unit within the rolled distance.

  **Lore-direct:** The Abomination's mobility is driven by warp-machinery spasms — sometimes the pumps fire hard and the body rolls 12 inches in a single phase; sometimes they sputter and the body shambles 4 inches. The Pack Masters can goad the direction but not the speed.

- **Too Horrible to Die** *(Hell Pit Abomination unit identity rule — Pass 2.1 degrading rebirth mechanic)* — When this model is reduced to **0 W** (i.e., would be removed as a casualty), **immediately roll a D6**:

  | D6 | Outcome |
  |---|---|
  | **1-2** | The Abomination is removed normally as a casualty. The warpstone-fusion finally gives out. **Permanent death.** |
  | **3-4** | **The Abomination regenerates at HALF W** (rounded up — initially 6 W from starting W 12). The Abomination stays at its current battlefield position. **All other stats degrade by 1** per the degradation rule below |
  | **5-6** | **The Abomination regenerates at FULL W** (initially 12 W). Same position. **All other stats degrade by 1** per the degradation rule below |

  **Stat-degradation mechanic.** Each time Too Horrible to Die triggers a rebirth (D6 result 3+), reduce the following stats by **1** each (with floors as noted). **W does NOT degrade** — the Abomination's starting W max remains 12 throughout all rebirths; only the *quality* of resurrection (half vs full) varies per roll.

  - **MA -1** (minimum MA 1)
  - **MD -1** (minimum MD 1)
  - **S -1** (minimum S 1) — affects both weapon profiles' wielder-S
  - **T -1** (minimum T 1)
  - **I -1** (minimum I 1)
  - **A -1** on **both weapon profiles** (Massive Claws A 3 → 2 → 1; Whirling Death A 4 → 3 → 2 → 1; minimum A 1 per profile)
  - **Random Movement dice reduced by 1 die per rebirth** *(Pass 2.2)*: **4D3 → 3D3 → 2D3 → 1D3 → fixed 1"**. Once the Random Movement reaches "fixed 1"", further rebirths do not reduce it further; the Abomination shambles at 1" per turn for any subsequent rebirths.
  - All other stats (W max, BS, Res, LiS, US) unchanged

  **Cumulative degradation.** A second rebirth degrades stats *again*. After ~3-4 rebirths the Abomination has degraded to minimum-floor combat stats and 1D6"-or-less mobility — a high-W shambler with token combat output.

  **Expected lifetime degradation curve:**

  | Rebirth # | MA | MD | S | T | I | Claws A | Whirl A | Random Mov *(Pass 2.2)* | W on rebirth |
  |---|---|---|---|---|---|---|---|---|---|
  | Initial (0) | 3 | 3 | 6 | 5 | 2 | 3 | 4 | **4D3 (mean 8, range 4-12)** | 12 (start) |
  | 1 | 2 | 2 | 5 | 4 | 1 | 2 | 3 | **3D3 (mean 6, range 3-9)** | 6 or 12 |
  | 2 | 1 | 1 | 4 | 3 | 1 | 1 | 2 | **2D3 (mean 4, range 2-6)** | 6 or 12 |
  | 3 | 1 | 1 | 3 | 2 | 1 | 1 | 1 | **1D3 (mean 2, range 1-3)** | 6 or 12 |
  | 4+ | 1 | 1 | 2 → 1 | 2 → 1 | 1 | 1 | 1 | **1" fixed** | 6 or 12 |

  **No limit on rebirths.** Too Horrible to Die may trigger any number of times across a battle, until either (a) the death roll fails on 1-2, or (b) the Abomination's stats degrade to the point of irrelevance.

  **Lore-direct:** "The Hell Pit Abomination's warpstone-injection apparatus refuses to let the body remain dead. Each time the flesh-amalgam is broken, the Moulder-installed pumps inject another dose of warpstone-mutated growth agents, and the body reassembles itself — cruder each time, more chaotic each time. The W max remains the same (the warpstone-pumps can always reflate the body to full volume), but the *coherent function* of the limbs and mechanical components degrades steadily."

  **Tactical implication.** The opposing player has to commit to killing the Abomination *multiple times*, accepting the wound-pool cost of each successive kill. With W max constant at 12 and 67% rebirth probability (3+), the expected absorption per rebirth attempt is ~(0.33 × 6 + 0.33 × 12) = ~6 W per attempt. Across an expected ~3 rebirths (probability of consecutive 3+ rolls): ~12 (initial) + 18 (3 rebirths × 6 W) = ~30 W effective lifetime absorption. **Most W-tank-tier defensive layer in the codebase.**

## Weapon Profiles

### Close Combat

- **Massive Claws** *(natural — primary heavy strikes)* — **1" reach** | **A 3** *(decreases with each rebirth, min 1)* | **S 6** *(decreases with each rebirth, min 1)* | **AP -1** | **D D3** — three crushing strikes per Combat round with the Abomination's largest stitched limbs. **S 6** wounds T 3 on 2+, T 4 on 3+, T 5 on 3+. **AP -1** strips light armour. **D D3** delivers 1-3 wounds per unsaved wound (average 2). Primary heavy melee output. `[Natural]`

- **Whirling Death** *(natural — secondary multi-limb flailing strike)* — **1" reach** | **A 4** *(decreases with each rebirth, min 1)* | **S 5** *(decreases with each rebirth, min 1)* | **AP 0** | **D 1** — four flailing strikes per Combat round with the Abomination's lesser limbs and tooth-mouths. Volume of attacks at modest S 5 / AP 0 / D 1. The "lots of small bites and slashes" complement to the Massive Claws. `[Natural]`
