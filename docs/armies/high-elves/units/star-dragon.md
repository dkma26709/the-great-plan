# Star Dragon

> The oldest and most powerful of Ulthuan's Dragons — "as ancient as the very stars of the firmament." Where the Sun Dragons are *young*, hot-tempered and rich-scaled, and the Moon Dragons are *mature*, surpassing the Suns in might and enlightenment, the Star Dragons are *ancient* — millennia-old apex predators that have outlived the rise of empires and the fall of races. "While any Dragon can savage an entire regiment of warriors, tear a Manticore apart or rip the head off a Wyvern, a Star Dragon is so physically powerful that it can battle against even the Greater Daemons of Chaos and prevail." The eldest, most powerful Dragons "can melt armour and the flesh beneath with a molten blast of their white-hot breath." Ridden only by the most ancient Asur Lords — Phoenix Kings, the Lords of Caledor, the Princes who can negotiate with Dragons on something approaching equal terms — the Star Dragon is the apex non-Daemon mortal mount in the codebase. Drafted here as the **super-apex Monster Mount profile** for High Elf Lord-tier characters (specifically Caledorian Princes / Lord-on-Dragon). Sister-pieces: Sun Dragon (Young, mid-Monster), Moon Dragon (Mature, apex), Star Dragon (Ancient, super-apex). The High Elf battlefield read: bind the Star Dragon to the army's apex Lord, commit it to the critical fight (often vs Greater Daemons, Chaos Lords on Dragons, or apex enemy commanders), and let the combined Lord-on-Star-Dragon decide that engagement in 1-2 rounds of combat through the sheer weight of stats + Solarflare Breath.

## Profile

**Star Dragon (Mount profile):**
| M | MA | MD | BS | S | T | W | I | Res | LiS | US |
|---|----|----|----|---|---|---|---|----|-----|----|
| 6 | 7 | 7 | 0 | 7 | 7 | 12 | 6 | 10 | 5 | =W |

**Points:** +511 added to the rider's base cost (Star Dragon + Rider combined per Rider and Mount Profiles §1). *(Framework derivation under §13: stat-baseline 31.5 + rules 4.5 + equipment 19.3 = 55.3 raw × wound factor 11.56 (W 12) × 0.8 scaling = 511.4 → +511. **Super-apex tier mount-adder**, comparable to the Stonehorn (+509 at W 14) — the Star Dragon's lower W (12 vs 14) is offset by far richer stats (apex MA 7 / MD 7 / I 6, S 7, T 7). The premium reflects the entire apex offensive + defensive package combined into a single super-apex Monster. **Pass 2 (2026-05-18):** Magical Attacks and Disciplined removed — Dragons are *pure biology*, not magical; faction overlays (Disciplined, Elven Grace) come from the rider. The Asur Dragons are the canonical baseline; other faction Dragons (Black, Chaos, Zombie, etc.) modify the breath weapon and add faction-specific identity rules. -28 pts from initial +539. See `design.md` for full working)*

**Unit size:** 1 (combined model — Asur Lord-tier rider + Star Dragon mount)

**Unit type:** Monster Mount (single model combining Star Dragon + Rider — see §1 Rider and Mount Profiles)

**Natural Armour:** 3+ (Scaly Skin — ancient star-touched scales, the apex tier in the Asur Dragon armour progression. Matches the Stonehorn at the codebase's heaviest natural armour; one step better than the Moon Dragon's NA 4+ mature scales and two steps better than the Sun Dragon's NA 5+ young scales)

**Fly:** 8" (per §8 — Star Dragons are heavy-bodied flyers; Fly 8 matches Hippogryph / Wyvern / Terrorgheist Mount tier rather than the faster Pegasus Knight Fly 12)

**Base Size:** 100mm × 75mm (apex Monster footprint)

**Keywords:** High Elves, Asur, Dragon, Ancient, Monster, Character Mount (the rider's keywords — Character, Lord, Asur — apply to the combined model as usual)

## Equipment

- **Equipment:** Star Fang-and-Claws (natural — apex Dragon claws + fanged maw + serpentine neck reach combined into a single multi-attack profile) + Solarflare Breath (natural breath weapon — white-hot molten blast). No worn armour, no shield, no rider weapons (the rider's own equipment per their character entry).

## Special Rules

- **Terror** *(Psychology — per §8)* — at LiS 5, the Terror aura projects to **(6 + 5)" = 11"**. A Star Dragon is one of the most ancient and physically imposing creatures on the battlefield — its arrival shakes the morale of all but the most disciplined enemies.
- **Fly (8")** *(per §8)* — apex Dragon wings carry the Star Dragon over terrain and intervening models on the Fly move. Heavy-bodied flyer pace (Fly 8" tier).

*Pure Dragon biology — no Magical Attacks, no faction-specific overlays.* Faction rules (Disciplined, Elven Grace, Martial Prowess for Asur; Murderous Prowess for Druchii; Will of Chaos for Chaos; Undead for VC) come from the rider's profile and project onto the combined model per §1 Rider and Mount Profiles. The Star Dragon biology itself is just *Dragon* — apex predator with massive scales, fangs, claws, fire, and ancient wisdom.

## Weapon Profiles

### Close Combat

- **Star Fang-and-Claws** *(natural — apex Dragon claws + fanged maw + serpentine neck-reach)* — **2" reach** | **A 5** | **S 7** | **AP -2** | **D D3** — five apex-Dragon strikes per Combat round. **S 7** wounds T 5 on 2+, T 6 on 3+, T 7 on 4+, T 8 on 5+ — apex strength bar, matching Carnosaur / Kharibdyss / Necrosphinx. **AP -2** strips heavy armour (4+ heavy → 6+ effective, 3+ heavy → 5+ effective). **D D3** delivers 1-3 wounds per unsaved wound (average 2). **2" reach** lets the long serpentine neck strike past front-rank bodyguards into second-rank models. `[Natural]`

### Ranged

- **Solarflare Breath** *(natural Breath Weapon — white-hot molten blast)* — **Flame Template** | **S 5** | **AP -2** | **D 1** | **Flaming** | **Slow to Fire** | **Scatter (Artillery Die)** — the iconic Star Dragon signature: "the eldest, most powerful Dragons can melt armour and the flesh beneath with a molten blast of their white-hot breath." The Flame Template covers a cone projected from the model's front arc (per §7.4 templates). **Flaming** triggers the standard interactions per §8 (negates Regeneration on targets, Flame-panic on US 2+ beast units — though the Star Dragon is itself US 12, so its own attacks are immune to the Flame-panic effect by the "any Flaming weapon in profile" clause per §8). **AP -2** is one step heavier than the Hydra Breath's AP -1 — the lore "melts armour" reads through directly: heavy plate cracks and melts under the white-hot blast. **Slow to Fire** means the Breath cannot be used as a Stand-and-Shoot reaction to enemy charges. **Scatter Artillery Die** models the imprecision of belching molten flame at range. `[Breath Weapon]`
