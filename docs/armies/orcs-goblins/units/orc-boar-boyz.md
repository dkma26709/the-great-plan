# Orc Boar Boyz

> *"'Ere we go, 'ere we go, 'ere we go!"* — Orcs who, "through sheer guts and determination, have managed to tame and ride the vicious War Boar into battle." The War Boar is "an extremely tough animal" of the Badlands deserts, "notoriously bad-tempered, loudly flatulent, wholly dangerous and very unpredictable" — "almost as large as an Imperial warhorse, but considerably bulkier." The boar kills many would-be riders before accepting one; the survivors form **the prestigious ranks of the Boar Boyz**, the heavy shock cavalry of any Orc warlord's army. **Tusker Charge** is the unit signature: "the impact of the Boar Boyz charge shatters bones and sends their victims flying dozens of feet into the air." It takes some distance to build speed, but "the War Boar's churning legs get the beast moving at a rate wholly unexpected from such a lumpen mass," and the ensuing ground-shaking charge delivers D3 Impact hits per model at S 5 (the mount's S 4 brawn + charge momentum) AP -1 (tusks). The boar's **tough hide** (NA 6+) lets the unit "shrug off hails of missile fire" — the natural-armour layer compensates for the bare-Orc-rider baseline. Combat fingerprint: midt-tier Greenskin cavalry, devastating on the charge round, lighter in sustained melee than the price-matched apex chivalric or saurian cavalry tiers. The Tusker Charge is the play — bring the unit into shock range, charge, deliver Impact carnage, then hold the position with the surviving Boar Boyz' melee output.

## Profile

**Rider (Orc Boar Boy):**

| MA | MD | BS | S | T | W | I | Res |
|----|----|----|---|---|---|---|----|
| 4 | 3 | 3 | 4 | 4 | 2 | 2 | 7 |

**Mount (War Boar):**

| M | MA | MD | BS | S | T | W | I | Res |
|---|----|----|----|---|---|---|---|----|
| 8 | 3 | 3 | 0 | 4 | 4 | 1 | 3 | 3 |

**Unit-level:**

| LiS | US |   | Points |
|-----|----|---|--------|
| 2   | 2  |   | **15** |

*(Framework derivation under §13: stat-baseline 11.25 + rules ~3.5 + equipment ~1.0 = 15.75 raw × wound factor 1.16 (combined W 2) × 0.8 scaling = 14.62 → 15; see `design.md` for full working.)*

**Unit size:** 5+

**Unit type:** Cavalry

**Natural Armour:** 6+ (War Boar tough hide — biological armour layer separate from rider's worn kit)

**Base Size:** 50mm × 25mm (Cavalry standard)

**Keywords:** Greenskin, Orc, Cavalry, Special

## Equipment

- **Equipment (default):** Choppa (rider) + Tusks (mount, natural). No worn armour, no shield, no boar barding. The default Boar Boy is a bare-Orc-rider on the boar's tough hide — the mount's NA 6+ provides the only protection.

## Special Rules

- **Animosity** *(Greenskin-wide faction trait — see §8 Psychology)*. D6 at start of each Movement phase when out of combat; on a 1, sub-roll D6 determines charge / self-hits at S 4 (rider's S).
- **Loves a Scrap** *(Orc-specific faction trait — see §8 Psychology)*. Stress relief on melee engagement + sustained-combat +1 A on a single weapon profile from round 2 onwards.
- **Undisciplined** *(Recovery trait — see §8 Psychology)*. -1 to Recovery rolls (floor 1). Common Orc baseline; only Black Orcs break the Greenskin Undisciplined default.
- **Tusker Charge** *(Orc Boar Boyz unit identity rule)* — On the turn this unit successfully charges into melee, before the Combat phase begins, resolve the following Impact attack (per §8 Impact):
  - **D3 Impact hits per model** at **S 5** (mount S 4 + 1) | **AP -1** (tusks) | **D 1**
  - Resolved against the charged unit's models within Reach of any charging model in base contact.
  - Damage does not carry between models. Failed charges produce no Impact attacks.
  
  Lore: "the impact of the Boar Boyz charge shatters bones and sends their victims flying dozens of feet into the air." The boar's churning legs build up to a shock-charge that hits before the Combat phase begins — front-rank casualties drop *before* the defender swings back.

## Options

**Worn armour options:**
- **Light armour** (+1 pt/model) — rider's worn protection. Stacks with mount NA 6+ as separate armour sources per §8 *Armour Save Stacking* → combined save **5+** (NA 6+ base + Light armour as additional source = +1 step).

**Worn armour additive:**
- **Shield** (+1 pt/model) — combined save improves by +1 step per §8 *Armour Save Stacking*. With **no Light armour**: 6+ → 5+. With **Light armour + Shield**: 5+ → 4+ (NA 6+ + worn armour 6+ + shield, three stacking sources).

**Equipment swap options (replace Choppa, pick at most one):**
- **Spear** (+1 pt/model) — 1H, 2" reach, replaces Choppa. Cavalry-charge-spear; on charge round gains +1 S and AP -1, captures the WAP-canonical "Boar Boy spear" charge bonus.
- **Pair of Choppas** (+2 pts/model) — second hand weapon; +1 A on weapon (A 2); cannot pair with shield.

**Command options:**
- **Boss (Leader)** (+5 pts) — champion
- **Standard Bearer** (+10 pts, may take Magic Standard up to 25 pts)
- **Musician** (+5 pts)

## Weapon Profiles

### Close Combat

- **Choppa** *(rider, default, 1H — may pair with shield)* — 1" reach | **A 1** | S 4 | AP -1 | D 1 — iconic Orc cleaver; bites through light armour. `[1H Blade]`
- **Spear** *(rider, option, 1H — may pair with shield, replaces Choppa)* — 2" reach | **A 1** | S 4 baseline (charge: **S 5, AP -1**) | D 1 — cavalry spear; the 2" reach lets the second rank participate; charge bonus delivers the lance-equivalent strike at impact. *(Note: Tusker Charge Impact hits are separate from and resolve before this profile's normal Combat-phase attacks — the rider's Spear charge bonus applies to the Combat phase strikes after Impact.)* `[1H Reach]`
- **Pair of Choppas** *(rider, option, 2× 1H paired — cannot pair with shield, replaces Choppa)* — 1" reach | **A 2** | S 4 | AP -1 | D 1 — second cleaver doubles the swings. `[Paired]`
- **War Boar Tusks** *(mount, natural — always available)* — 1" reach | **A 1** | S 4 | **AP -1** | D 1 — sharp tusks bite into flesh and through light armour. `[Natural]`
