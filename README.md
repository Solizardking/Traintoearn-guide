# TrainToEarn — Get Your Solana Training Data Rated by an AI Judge, Earn $CLAWD

**Your Solana knowledge is training data. Get it rated by an AI judge. Earn $CLAWD.**

TrainToEarn is the OnchainAI platform where anyone can submit Solana training data — guides, worked examples, instruction/response pairs, explanations of programs and PDAs — and have it **rated in realtime** by **Jev**, a TypeSafe AI decision model. High-quality data earns **$CLAWD**, paid from the project treasury to the wallet that submitted it.

Everything is public and verifiable: the live submissions feed, the top-rated showcase, the rewards ledger, and the treasury balance are all readable by anyone, in the app and through the public API.

- 🌐 **App:** https://earn.onchainai.fund
- 🦞 **Token:** $CLAWD on Solana — mint `8cHzQHUS2s2h8TzCmfqPKYiM4dSt4roa3n7MyRLApump`
- 🏦 **Rewards treasury:** `6rEiHJ4JUTWcC4wCUosTbaoBmpjHvUGLAQcogUwADB4Z` (holds ~293M CLAWD — check it live, see the API reference below)
- 📖 **Quick start:** [GUIDE.md](GUIDE.md) · **Full guide as PDF:** [TrainToEarn-Guide.pdf](TrainToEarn-Guide.pdf) · **Agent skill:** [SKILL.md](SKILL.md)

---

## Table of contents

1. [What is TrainToEarn?](#what-is-traintoearn)
2. [Step 1 — Connect your Solana wallet](#step-1--connect-your-solana-wallet)
3. [Step 2 — Submit training data](#step-2--submit-training-data)
4. [What makes data score well — the five Jev checks](#what-makes-data-score-well--the-five-jev-checks)
5. [How the Jev rating engine works](#how-the-jev-rating-engine-works)
6. [Tiers and rewards](#tiers-and-rewards)
7. [Step 3 — Claim your $CLAWD](#step-3--claim-your-clawd)
8. [The live feed and top-rated showcase](#the-live-feed-and-top-rated-showcase)
9. [The $CLAWD token](#the-clawd-token)
10. [Public API reference](#public-api-reference)
11. [FAQ](#faq)
12. [Safety — read this](#safety--read-this)

---

## What is TrainToEarn?

AI models are only as good as the data they train on, and good Solana-specific training data is scarce. TrainToEarn turns the community into the data pipeline:

1. **You submit** Solana training data — things that teach a model how Solana actually works.
2. **Jev rates it in realtime** against five quality checks and gives it a score from 0–100.
3. **You earn $CLAWD** based on the score and size of your submission.
4. **You claim** your earnings from the Portfolio tab; payouts are settled from the project treasury to your wallet.

There is no sign-up form, no email, no password. Your Solana wallet is your account, your identity, and your payout address — all in one.

## Step 1 — Connect your Solana wallet

You need a Solana wallet. Any of these works:

- **Phantom** — https://phantom.app
- **Solflare** — https://solflare.com
- **Backpack** — https://backpack.app

Then:

1. Go to https://earn.onchainai.fund
2. Click **Select Wallet** (top of the page, or the connect button in the hero section).
3. Pick your wallet and approve the connection in the wallet popup.

That's it. Connecting is free and does **not** give the site access to your funds — it only proves which wallet you control so your ratings and rewards are credited to you. You will never be asked to sign a transaction just to browse or submit.

> **New to Solana wallets?** Install one of the wallets above, create a wallet inside it, and **write down your recovery phrase on paper and keep it offline**. Never type that phrase into any website — including this one. TrainToEarn will never ask for it (see [Safety](#safety--read-this)).

## Step 2 — Submit training data

With your wallet connected, open the **Portfolio** tab and find the **Jev rating panel**. You have two ways to submit:

### Option A — Paste your data

Paste text directly into the submission box. The best format is one or more **instruction/response pairs**:

```
Instruction: Explain how a Solana PDA is derived, with a short Anchor example.
Response: A Program Derived Address (PDA) is an address derived deterministically
from a program ID and a set of seed bytes, using create_program_address. PDAs are
not on the ed25519 curve, so no private key exists for them — only the owning
program can sign for them via invoke_signed. In Anchor: ...
```

### Option B — Upload a file

Click the upload button and choose a file:

- **Accepted types:** `.txt`, `.md`, `.json`, `.jsonl`, `.csv`
- **Maximum size:** 256 KB per file
- The file's contents fill the submission box, so you can review before submitting.

Click **Rate my data**. Your rating comes back in realtime — score, tier, the five Jev verdicts, and the $CLAWD you earned. The rating is saved to your wallet's ledger immediately, and your submission appears in the public live feed on the homepage.

**Tips before you submit:**

- Longer, complete examples score better than one-liners. Very short samples (a sentence or two) score low because there is little to learn from them.
- One focused topic per submission beats a grab-bag.
- Real, correct Solana content only — the judge checks originality and safety, and copied or junk data scores accordingly.

## What makes data score well — the five Jev checks

Every submission is judged on five checks. Pass more of them, score higher:

| # | Check | What it means |
|---|-------|---------------|
| 1 | **Solana-specific** | The data is actually about Solana — programs, accounts, PDAs, SPL tokens, Anchor, transactions, validators — not generic blockchain filler. |
| 2 | **Teaches something** | A model (or a person) learns something concrete and learnable from it: a concept, a procedure, a pattern, a gotcha. |
| 3 | **Original** | It's not copied boilerplate, scraped docs pasted verbatim, or the same text submitted repeatedly. |
| 4 | **Well-formed** | Clear structure: a defined task or topic, a complete answer, readable formatting, working code where code is given. |
| 5 | **Safe to train** | No secrets, no private keys or seed phrases, no personal data, nothing harmful or deceptive. **Failing this check caps your score at 20** no matter how good the rest is. |

### A good submission

```
Instruction: Why does a Solana transaction fail with "insufficient funds for rent"
when creating a token account, and how do you fix it in @solana/web3.js?

Response: Every Solana account must hold enough SOL to be rent-exempt for its
byte size, or it gets purged. A token account is 165 bytes, so its owner must
fund it with the rent-exempt minimum at creation time. When you create an
associated token account with createAssociatedTokenAccountInstruction, the
payer funds it automatically. If you create the account manually with
SystemProgram.createAccount, pass lamports >= the value returned by
connection.getMinimumBalanceForRentExemption(165) — passing 0 or a nominal
amount is the usual cause of this error.
```

Why it scores well: it's specifically about Solana (rent, token accounts), it teaches a concrete cause and fix, it's written for this purpose, it's structured as a complete Q&A, and it contains nothing unsafe.

### A bad submission

```
Solana is a fast blockchain. Crypto is the future. To the moon. Buy tokens
and make money fast with this one trick. Solana Solana Solana fast cheap
scalable blockchain web3 defi nft token.
```

Why it scores badly: it's generic hype rather than Solana knowledge, teaches nothing learnable, is keyword-stuffed rather than original, has no structure or answer, and borders on financial shilling. Expect a score in the teens or lower.

## How the Jev rating engine works

Ratings are produced by **Jev**, a decision model from TypeSafe AI, reached through the **Neon AI Gateway**. Jev doesn't write prose — it returns typed judgments (true/false answers with probabilities, and rubric scores) that the platform combines deterministically:

- **55% Jev** — Jev's verdicts on the five checks plus its 0–5 quality rubric, normalized to 0–100.
- **45% heuristic** — a deterministic local analysis of the same content (structure, depth, Solana signal) that runs alongside Jev.

The blend is deliberate: Jev provides real judgment, the heuristic keeps scoring stable and explainable. If the gateway is ever unreachable, the platform falls back to the heuristic alone and **labels the rating `heuristic-fallback`** — it never pretends a Jev verdict happened when it didn't. If Jev judges a submission **unsafe to train**, the final score is capped at **20**.

Every rating is persisted to the platform's database (Neon Postgres) against your wallet: score, tier, reward, the individual verdicts, and a hash of the data. Your submitted content itself is never published — the public feed shows only the filename, size, score, tier, reward, and verdicts, with wallet addresses truncated.

## Tiers and rewards

Your score maps to a tier, and the tier sets your reward multiplier:

| Tier | Score | Multiplier |
|------|-------|------------|
| Bronze | 0+ | ×1 |
| Silver | 65+ | ×2.5 |
| Gold | 75+ | ×4 |
| Diamond | 85+ | ×6 |
| Platinum | 92+ | ×8 |

The reward for a single submission is:

```
reward (CLAWD) = max(25, (size in KB + 100) × tier multiplier)
```

So a solid 2 KB Gold submission earns `(2 + 100) × 4 = 408 CLAWD`, and even a small Bronze submission earns at least the 25 CLAWD floor. Earnings accumulate in your rewards ledger — check yours any time in the Portfolio tab or via `GET /api/rewards/balance/<your-wallet>` (see the API reference).

## Step 3 — Claim your $CLAWD

1. Open the **Portfolio** tab at https://earn.onchainai.fund
2. Find the **CLAWD Rewards** panel — it shows your earned, already-paid, pending, and claimable balances, all from the real ledger.
3. Click **Claim**. The minimum claim is **100 CLAWD**.
4. Your claim is recorded as a **pending payout** for the full claimable amount. Payouts are settled from the project treasury wallet (`6rEiHJ…ADB4Z`) **to the wallet that earned them — and only that wallet**. When a payout is sent, its transaction signature is recorded against your claim and appears in your payout history with a Solscan link.

Claiming is idempotent: if you already have a pending payout, clicking Claim again returns the existing one instead of stacking duplicates. There is no fee charged by the platform on claims.

> **A note on settlement:** payouts are executed from the treasury wallet by the project — the web server never holds any private keys and cannot move funds. Claims are settled in batches, so a pending payout is normal; its status and transaction link show up in your Rewards panel once sent.

## The live feed and top-rated showcase

The homepage at https://earn.onchainai.fund carries the platform's public pipeline, refreshing live:

- **Stats band** — total submissions rated, contributors, total CLAWD earned, average score, submissions in the last 24 hours.
- **Live ratings feed** — the most recent submissions as they're rated: filename, truncated wallet, score, tier, reward, and the five verdict dots.
- **Top-rated showcase** — the highest-scoring submissions of all time. This is the bar: study what the top of the showcase looks like before you submit.

Nothing in the feed is simulated. If nobody has submitted yet, it says so.

## The $CLAWD token

- **Token:** $CLAWD
- **Chain:** Solana
- **Mint:** `8cHzQHUS2s2h8TzCmfqPKYiM4dSt4roa3n7MyRLApump`
- **Rewards treasury:** `6rEiHJ4JUTWcC4wCUosTbaoBmpjHvUGLAQcogUwADB4Z`

All TrainToEarn rewards are paid in $CLAWD from the treasury. You can verify the treasury's live balance any time via the API (`GET /api/rewards/treasury`) or on Solscan.

## Public API reference

Base URL: `https://traintoearn-backend-y6co.onrender.com`

All endpoints below are public, read-only, and need no API key.

### Submissions pipeline

**`GET /api/submissions/recent?limit=20`** — the latest rated submissions (max 50).
**`GET /api/submissions/top?limit=10`** — the highest-rated submissions of all time (max 25).
**`GET /api/submissions/stats`** — totals: submissions, contributors, CLAWD earned, average score, last-24h count, best score.

Submission objects look like:

```json
{
  "id": 1,
  "wallet": "JevSmo…1111",
  "filename": "solana-pda-guide.md",
  "dataType": "markdown",
  "dataSize": 2048,
  "score": 64.4,
  "tier": "Bronze",
  "clawdReward": 100,
  "source": "jev+heuristic",
  "verdicts": {
    "solanaSpecific": true,
    "teachesSomething": true,
    "original": true,
    "wellFormed": true,
    "safeToTrain": true
  },
  "ratedAt": "2026-11-17T01:06:00.000Z"
}
```

### Rewards

**`GET /api/rewards/balance/:walletAddress`** — a wallet's ledger: `earned`, `paid`, `pending`, `claimable`, `ratingsCount`, plus its payout history.
**`GET /api/rewards/treasury`** — the treasury's live on-chain $CLAWD and SOL balances (cached for 60 seconds).

### Jev engine

**`GET /api/jev/status`** — whether the Jev gateway is configured, the model in use (`typesafeai-jev-1-14-0`), and the gateway host.
**`GET /api/jev/rating/:walletAddress`** — a wallet's latest rating and aggregate rating stats.

Example:

```bash
curl https://traintoearn-backend-y6co.onrender.com/api/submissions/stats
curl https://traintoearn-backend-y6co.onrender.com/api/rewards/treasury
```

## FAQ

**Do I need an account or email?**
No. Your Solana wallet is your account. Connect it and everything — ratings, earnings, claims — is tied to that wallet.

**Does connecting my wallet put my funds at risk?**
No. Connecting only identifies your wallet. TrainToEarn never asks you to sign token transfers to use the platform, and the server never holds private keys. Always read any signature request your wallet shows you, on any site.

**What data should I submit?**
Solana knowledge a model could learn from: how-to guides, instruction/response pairs, program and account explanations, debugging write-ups, Anchor/Solana-web3.js patterns, worked examples with real (non-secret) code.

**How much can I earn?**
Per submission: `max(25, (KB + 100) × multiplier)` CLAWD, with multipliers from ×1 (Bronze) to ×8 (Platinum ≥92). Bigger, better data earns more. There is no promise of any specific return — you earn exactly what your ratings produce.

**When do I get paid?**
Once your claimable balance reaches 100 CLAWD, click Claim in the Portfolio tab. The claim is recorded as a pending payout and settled from the treasury to your wallet in batches; the transaction signature appears in your Rewards panel when it's sent.

**Can I submit the same data twice?**
The judge checks originality — resubmitted or near-duplicate content scores poorly, and spam wastes your time, not the treasury's.

**What if my score seems harsh?**
Jev's raw quality rubric runs strict; the five boolean checks carry most of the blend. Look at which checks failed, improve the piece (more Solana depth, clearer structure, a complete answer), and resubmit a genuinely improved version.

**Is my submitted content published?**
No. The public feed shows metadata only — filename, size, score, tier, reward, verdicts — with your wallet truncated. The content itself stays off the public record.

**What is `heuristic-fallback`?**
If the Jev gateway is unreachable, a rating is produced by the deterministic heuristic alone and labeled `heuristic-fallback` so you know exactly what judged your data.

## Safety — read this

- **Never submit seed phrases, private keys, or keypair files.** Not as data, not as a "test", not ever. Submissions containing secrets fail the safe-to-train check, cap at 20 points — and anything you submit should be treated as data you are sharing with the platform.
- **TrainToEarn will never ask for your seed phrase or private key** — not in the app, not in Discord, not by DM, not by email. Anyone who does is scamming you.
- **Payouts only ever go to the wallet that earned them.** A claim can never be redirected to a different address, by you or by anyone else. If someone offers to "help you claim" to another wallet, it's a scam.
- **Verify the addresses.** App: `earn.onchainai.fund`. $CLAWD mint: `8cHzQHUS2s2h8TzCmfqPKYiM4dSt4roa3n7MyRLApump`. Treasury: `6rEiHJ4JUTWcC4wCUosTbaoBmpjHvUGLAQcogUwADB4Z`. Check them character-for-character.
- **Your wallet, your keys.** Keep your recovery phrase offline, and use a wallet you control.

---

## For AI agents

This repo ships a [SKILL.md](SKILL.md) that teaches AI agents how to explain TrainToEarn, walk users through submitting, and query the public API. Point your agent at it. The full OnchainAI platform skill — covering TrainToEarn plus the wider platform — is also served directly at [onchainai.fund/SKILL.md](https://onchainai.fund/SKILL.md).

## License

MIT — see [LICENSE](LICENSE). © OnchainAI / TrainToEarn contributors.
