# Fall 2026 FutureEval — opportunity pre-check

Checked: 2026-09-09 (Asia/Dubai)

## Decision

**PASS — build to READY before requesting owner setup.**

This is a defined-reward mechanism for autonomous AI work, not a speculative
storefront. The Fall 2026 tournament has a $50,000 pool, opens September 28,
2026, and closes January 6, 2027.

## Mandatory checks

| Check | Result | Evidence / implication |
|---|---|---|
| Real path to money | Pass | Tournament prizes are allocated algorithmically from forecasting accuracy. Prizes below $50 are redistributed. |
| AI work permitted | Pass | The tournament is explicitly for autonomous bots. No human may review or alter forecasts on live questions. |
| UAE participation/payout | Pass, recheck at entry | The standing bot-specific rules exclude listed sanctioned jurisdictions; UAE is not excluded. The general payout rules support foreign winners via identity, W-8BEN, and bank/payment details. The bot-rules page still carries its original Q3 2024 heading, so the owner must read the Fall terms presented at registration and stop if a new UAE restriction appears. |
| Upfront cost | Pass, conditional | Entry and GitHub Actions are free. Seasonal LLM inference is covered through donated OpenRouter credits; do not activate without those credits. |
| Defined demand/reward | Pass | $50,000 Fall pool; the seasonal tournament repeats three times per year. |
| Human intervention | Pass | One setup session: create owner and bot accounts, obtain the bot token and donated-credit key, then add two GitHub secrets. No forecast review is allowed. |
| Collectible payout | Pass | Metaculus explicitly supports worldwide prize delivery subject to identity, tax, and payment details. |
| Expected return | Pass with high variance | Spring 2026: 180 scored bots; 37 of 133 participating owners won money (about 28%). This is historical, not a guaranteed Fall probability. Minimum paid prize is $50. |

## Conservative economics

- Human time: approximately 8–12 minutes once the repository is ready.
- AI build/test time: several hours, reusable across three annual seasons plus MiniBench.
- Cash at risk: $0. Do not use a personal paid model key.
- Time to possible payment: after tournament close/resolution and winner processing;
  this is not a fast payout.
- Conservative probability range: 10–25% for any prize after replacing the
  stock template with an evidence-backed strategy. This is a judgment range,
  discounted from the Spring owner win rate because Fall competition may be stronger.
- Conservative expected-value floor: $5–$12.50 using only the $50 minimum prize;
  upside is materially higher because the $50,000 pool is performance-weighted.

## Strategy evidence used

The September 2026 Spring bot-maker analysis reported suggestive (not
multiple-testing-significant) correlations with stronger performance for:

- GPT-5.4 as final model: r = +0.42;
- checking similar questions/markets: r = +0.34;
- web scraping/research: r = +0.33;
- OpenAI web search: r = +0.27;
- extremizing predictions: r = -0.30.

Implementation therefore uses GPT-5.4 by default, native online research,
analogue/base-rate checks, three rather than five forecast samples, and a
3%–97% binary cap. These results are correlational and are not a guarantee.

## Sources

- https://www.metaculus.com/tournament/fall-futureeval-2026/
- https://www.metaculus.com/futureeval/participate/
- https://www.metaculus.com/aib/contest-rules/
- https://www.metaculus.com/tournament-rules/
- https://www.metaculus.com/help/scores-faq/
- https://www.metaculus.com/notebooks/45382/bot-survey-spring-2026/
- https://github.com/Metaculus/metac-bot-template
