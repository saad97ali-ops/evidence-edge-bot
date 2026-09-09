# Owner action — Fall 2026 FutureEval

The bot is ready. These are the minimum account-bound steps that Codex cannot
perform honestly or safely.

**Progress update — 2026-09-10:** The owner created the first bot and public
fork, regenerated an accidentally exposed Metaculus token, saved the replacement
as the `METACULUS_TOKEN` repository secret, and submitted the sponsored-credit
request. The replacement token remained private. Await the organizer-funded key;
do not attach personal billing.

Public deployment fork:
<https://github.com/saad97ali-ops/evidence-edge-bot>

## Do now (estimated 8–12 minutes)

1. Open <https://www.metaculus.com/futureeval/participate/> and sign in or create
   a personal Metaculus account.
2. Create exactly one prize-eligible bot under that owner account. Save its bot
   token in a password manager; do not paste it into chat or commit it to Git.
3. Submit the organizer's sponsored-credit form at
   <https://forms.gle/aQdYMq9Pisrf1v7d8>. Request credits for the Fall 2026
   FutureEval tournament. Do not add a card, fund OpenRouter, or use a personally
   billed API key.
4. Fork <https://github.com/Metaculus/metac-bot-template> into the same GitHub
   account you want to run the bot from. A fork of this public repository will be
   public; that also avoids private-repository Actions-minute limits and is
   consistent with the contest's code-disclosure requirement.
5. Return with only the public fork URL and the statements `bot token saved` and
   `credit request submitted`. Do not send either secret.

After that, Codex can prepare the fork contents. When the donated key arrives,
the owner will add two GitHub Actions secrets directly in the repository UI:
`METACULUS_TOKEN` and `OPENROUTER_API_KEY`. That is the final credential action.

## Permissions and financial boundary

- `METACULUS_TOKEN` authenticates the bot account so the workflow can read
  tournament questions and post forecasts/reasoning comments. It is not a bank,
  wallet, trading, payment, or spending credential.
- `OPENROUTER_API_KEY` authorizes model inference. Use only the organizer-funded,
  sponsor-limited key. Never attach personal billing, deposit funds, or provide a
  personally funded key for this experiment.
- The workflow declares GitHub `contents: read`; it does not request repository
  write permission.
- Identity, W-8BEN and bank/payment details are supplied only if Metaculus awards
  a prize. Those details remain owner-controlled.

## Current economics

- Entry cost: $0.
- Published Fall prize pool: $50,000.
- Published minimum payable prize: $50.
- Historical reference: 37 of 133 Spring 2026 participating bot owners won money
  (28%). This is not a forecast of our result.
- Conservative planning probability after discounting that reference: 10%–25%.
- Conservative expected-value floor: $5–$12.50, calculated only from the $50
  minimum prize; actual prize upside is higher.
- Earliest result/payment path: after the tournament closes on January 6, 2027.

## Prepared artifact

`EvidenceEdgeBot` is based on the official template and targets
`fall-futureeval-2026`. Static tests, syntax validation, dependency import and
model-identifier construction have passed. End-to-end forecasting remains
impossible until the two owner-controlled credentials exist and the tournament
opens on September 28, 2026.
