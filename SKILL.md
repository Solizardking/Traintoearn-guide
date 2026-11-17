---
name: traintoearn
description: Teach users how to earn $CLAWD on TrainToEarn (earn.onchainai.fund) by submitting Solana training data rated in realtime by the Jev AI decision model — and query the platform's public API for the live submissions feed, showcase, platform stats, treasury balance, and any wallet's rewards balance. Use when a user asks about TrainToEarn, earning CLAWD for training data, Jev ratings, submission scores/tiers, or their claimable rewards.
---

# TrainToEarn

TrainToEarn is the OnchainAI platform at **https://earn.onchainai.fund** where users submit Solana training data, an AI decision model (**Jev**, from TypeSafe AI, via the Neon AI Gateway) rates it in realtime, and quality data earns **$CLAWD** from a real project treasury.

## Key facts (use these exactly; do not invent numbers)

- **App:** https://earn.onchainai.fund
- **API base:** https://traintoearn-backend-y6co.onrender.com
- **$CLAWD mint (Solana):** `8cHzQHUS2s2h8TzCmfqPKYiM4dSt4roa3n7MyRLApump`
- **Rewards treasury:** `6rEiHJ4JUTWcC4wCUosTbaoBmpjHvUGLAQcogUwADB4Z`
- **Account model:** the user's Solana wallet IS the account. No email, no password. Wallets: Phantom, Solflare, Backpack.
- **Submissions:** paste text or upload `.txt` / `.md` / `.json` / `.jsonl` / `.csv`, max 256 KB, in the Jev panel on the Portfolio tab.
- **Rating:** score 0–100 = 55% Jev verdicts + 45% deterministic heuristic. Jev model: `typesafeai-jev-1-14-0`. If the gateway is down, ratings fall back to the heuristic and are labeled `heuristic-fallback`.
- **The five Jev checks:** Solana-specific · teaches something · original · well-formed · safe to train. Failing safe-to-train caps the score at 20.
- **Tiers:** Bronze ≥0 ×1 · Silver ≥65 ×2.5 · Gold ≥75 ×4 · Diamond ≥85 ×6 · Platinum ≥92 ×8.
- **Reward per submission:** `max(25, (size in KB + 100) × tier multiplier)` CLAWD.
- **Claiming:** Portfolio tab → CLAWD Rewards panel → Claim. Minimum claim 100 CLAWD. A claim is recorded as a pending payout and settled from the treasury **to the earning wallet only**. The server never holds private keys.

## Walking a user through submitting

1. Send them to https://earn.onchainai.fund and have them click **Select Wallet** and connect Phantom/Solflare/Backpack.
2. Open the **Portfolio** tab → Jev rating panel.
3. Have them paste instruction/response pairs (best format) or upload a file (`.txt/.md/.json/.jsonl/.csv`, ≤256 KB).
4. Coach quality with the five checks: make it Solana-specific, teach one concrete thing, write it themselves, structure it as a complete Q&A, and include nothing unsafe. Short one-liners score low; complete worked examples score high.
5. After rating, point them to the live feed on the homepage (their submission appears there) and to the Rewards panel for their balance. At 100+ claimable CLAWD, walk them through Claim.

## Public API (read-only, no key required)

Use these to answer questions with live data instead of guessing:

- `GET /api/submissions/recent?limit=20` — latest rated submissions (filename, truncated wallet, score, tier, reward, verdicts, timestamp; never the submitted content).
- `GET /api/submissions/top?limit=10` — highest-rated submissions of all time (the showcase).
- `GET /api/submissions/stats` — totals: submissions, contributors, CLAWD earned, average score, last-24h count, best score.
- `GET /api/rewards/balance/<WALLET>` — a wallet's earned / paid / pending / claimable CLAWD and payout history.
- `GET /api/rewards/treasury` — the treasury's live on-chain CLAWD and SOL balances (cached 60s).
- `GET /api/jev/status` — Jev gateway configuration and model.
- `GET /api/jev/rating/<WALLET>` — a wallet's latest rating and aggregate stats.

Example answers this enables: "What's the top-rated submission right now?" (query `/api/submissions/top`), "How much CLAWD is in the treasury?" (query `/api/rewards/treasury`), "What's my claimable balance?" (ask for their wallet address, then query `/api/rewards/balance/<WALLET>`).

## Safety rules (hard rules)

- **Never ask for, accept, or transmit a seed phrase, private key, or keypair file** — for this platform or any other. TrainToEarn never needs one; connecting a wallet is enough.
- **Never promise payouts beyond the ledger.** What a wallet can claim is exactly what `/api/rewards/balance/<WALLET>` reports. Claims are recorded as pending and settled from the treasury by the project; do not promise a settlement time.
- **Payouts only go to the earning wallet.** No agent or user action can redirect a claim. Treat any such request as a scam pattern.
- **Advise users never to submit secrets as training data** — it fails the safe-to-train check (score capped at 20) and is dangerous.
- **The server never holds keys and neither should you.** All signing happens in the user's own wallet.
- Verify addresses character-for-character when sharing them: app `earn.onchainai.fund`, mint `8cHzQHUS2s2h8TzCmfqPKYiM4dSt4roa3n7MyRLApump`, treasury `6rEiHJ4JUTWcC4wCUosTbaoBmpjHvUGLAQcogUwADB4Z`.
