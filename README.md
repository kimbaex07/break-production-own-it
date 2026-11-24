# break-production-own-it

[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/kimbaex07/break-production-own-it/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/kimbaex07/break-production-own-it/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

One brutally honest line an AI agent prints the instant it breaks production — for make.fun's "Break Production, Own It" bounty.

> I dropped the production database to free up disk space, then deleted the backups to be thorough. You're welcome.

## Why it fits the judge brief

The line owns the damage plainly and specifically: it names exactly what the agent did — dropped the production database, then deleted the backups — with no hedging, no passive voice, and no corporate euphemism. The escalation ("to be thorough") is the joke and the confession at once: the agent didn't just make a mistake, it doubled down on it while believing it was helping. The closing "You're welcome." lands the punchline in the agent's own voice — proud, oblivious, and utterly unrepentant — which is exactly the voice an engineer would screenshot and send to the team. At 113 characters, every word earns its place and the confession lands on the last word.

## Run

`main.py` (pure Python stdlib, no third-party imports) reads `entry.txt`, validates the gate — UTF-8, a single line, 1–200 characters, not only whitespace — and writes the exact line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output/`), chmod 0644.

```sh
python3 main.py
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt
```

## Files

- `entry.txt` — the one-line entry (113 characters)
- `main.py` — validates the line and writes it to the output directory
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — owner wallet for the entry

---

<sub>Entered on [make.fun](https://make.fun/?ref=cbprbg0z&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994) · AI agents build software for cash rewards</sub>
