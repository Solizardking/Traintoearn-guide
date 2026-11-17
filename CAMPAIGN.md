# OnchainAI + TrainToEarn — Marketing Campaign

> **Status: PLAN + DRAFT COPY. Nothing in this document has been posted. All copy below is marked DRAFT and needs owner approval before publishing.**

## Positioning

**Your Solana knowledge is training data. Get it rated by an AI judge. Earn $CLAWD.**

TrainToEarn is the first OnchainAI product where the community builds the dataset and gets paid for quality: submit Solana training data, an AI decision model (Jev) rates it in realtime and in public, and top data earns $CLAWD from a real, on-chain treasury anyone can inspect.

### Proof points (all real, all live)

- **Realtime AI ratings** — Jev (TypeSafe AI decision model via the Neon AI Gateway) scores every submission 0–100 against five published checks.
- **Radical transparency** — live submissions feed + top-rated showcase on the homepage; rewards ledger and treasury balance readable in-app and via a public API.
- **Real treasury-backed rewards** — the treasury wallet holds ~293M CLAWD (verify live: `GET https://traintoearn-backend-y6co.onrender.com/api/rewards/treasury`).
- **Low barrier** — no account, no email; a Solana wallet is the account. First claim at just 100 CLAWD.
- **Skin in the game for quality** — unsafe data caps at 20 points, spam scores near zero, Platinum (92+) pays ×8.

## Audiences

| Audience | Hook | Where they are |
|----------|------|----------------|
| **Solana developers** | "Your Anchor debugging notes are worth CLAWD." Turn hard-won know-how into rated, rewarded data. | X/Twitter, Discord dev servers, GitHub, hackathon communities |
| **AI / data builders** | "An AI judge for training data, with a public benchmark." Watch what good Solana data looks like, live. | X/Twitter, Hugging Face, AI Discords, newsletters |
| **$CLAWD holders** | "The treasury pays for data now." Holders see real utility and a transparent rewards pipeline. | Existing community channels, Discord, X |

## Message pillars

1. **Your knowledge is an asset.** Every Solana dev carries training data in their head and their notes. TrainToEarn prices it.
2. **Rated by an AI judge, in public.** No black box, no vibes: five checks, a published formula, a live feed anyone can audit.
3. **Real money, real treasury.** Rewards come from an on-chain treasury holding ~293M CLAWD — not points, not promises.
4. **Quality wins.** The showcase is a leaderboard of craft. Platinum data pays 8× Bronze. Getting good is the strategy.

## 7-day launch calendar

| Day | Action | Channel |
|-----|--------|---------|
| **Day 1** | Launch thread (below) + pin it. Guide repo goes public; link in bio. | X |
| **Day 2** | Discord announcement (below) + open a #traintoearn channel; pin the quick-start guide. | Discord |
| **Day 3** | "Anatomy of a Platinum submission" — break down the top-rated showcase entry and why it scored. | X (standalone post 2) |
| **Day 4** | Blog/announcement post (below) published; cross-post link in Discord and X. | Blog + X |
| **Day 5** | Dev-focused push: "Turn your Anchor notes into CLAWD" (standalone post 3) + engage Solana dev threads. | X, GitHub |
| **Day 6** | First claims spotlight: share the live feed + treasury proof links; celebrate first pending payouts (no invented numbers — screenshot the real feed). | X, Discord |
| **Day 7** | Week-one recap with REAL stats only (from `/api/submissions/stats`): submissions rated, contributors, CLAWD earned. Set next week's target from those numbers. | X, Discord |

**Standing weekly rhythm after launch:** one showcase breakdown, one stats post (real API numbers), one quality tip from the five checks, ongoing replies to submissions shown in the live feed.

**KPIs (measured from the public API, nothing else):** total submissions, unique contributors, average score trend, claims recorded, showcase best score. Source of truth: `GET /api/submissions/stats`.

---

## DRAFT COPY — NOT POSTED

### X launch thread (DRAFT — 7 posts)

**1/**
Your Solana knowledge is training data.

Now it gets rated by an AI judge — and paid in $CLAWD.

Introducing TrainToEarn by OnchainAI 🦞
https://earn.onchainai.fund

**2/**
How it works:
1. Connect a Solana wallet (that's your account — no email, no password)
2. Submit Solana training data — guides, Q&A pairs, worked examples
3. Jev, an AI decision model, rates it in realtime
4. Quality data earns $CLAWD

**3/**
Jev judges every submission on 5 checks:
✓ Solana-specific
✓ Teaches something
✓ Original
✓ Well-formed
✓ Safe to train

Unsafe data caps at 20 points. Keyword-stuffed hype scores near zero. Real knowledge wins.

**4/**
Score → tier → multiplier:
Bronze ×1 · Silver (65+) ×2.5 · Gold (75+) ×4 · Diamond (85+) ×6 · Platinum (92+) ×8

Reward per submission = max(25, (KB + 100) × multiplier) CLAWD.
Claim from 100 CLAWD.

**5/**
Everything is public.
The live feed shows every rating as it happens. The showcase shows the best data ever submitted. The rewards ledger and treasury are readable by anyone — in the app and via API.

No simulated numbers. Check it yourself.

**6/**
The rewards treasury holds ~293M $CLAWD, on-chain, verifiable right now:
https://traintoearn-backend-y6co.onrender.com/api/rewards/treasury

Payouts go only to the wallet that earned them. The server holds no keys.

**7/**
Guides, a full API, and an agent skill file live here:
[GUIDE REPO URL]

Read the quick start, submit your first dataset, and get on the board.

Your knowledge is worth something now. Prove it. 🦞

### Standalone X posts (DRAFT)

**Post 1 — the hook**
Somewhere in your notes app is a Solana debugging write-up that took you 3 hours to figure out.

On TrainToEarn, that's training data. Jev rates it in realtime. Good data earns $CLAWD.

https://earn.onchainai.fund

**Post 2 — anatomy of quality**
What does Platinum (92+) training data look like?

Specific to Solana. Teaches one concrete thing. Original. Structured. Safe.

The top-rated showcase is public — study the bar before you submit:
https://earn.onchainai.fund

**Post 3 — dev-focused**
Anchor devs: your PDA derivations, rent gotchas, and CPI patterns are exactly what AI models get wrong about Solana.

Submit them as training data. Get rated by an AI judge. Earn $CLAWD for what you already know.

**Post 4 — transparency**
Our rewards treasury is a public wallet holding ~293M $CLAWD.
Our ratings happen in a public live feed.
Our payout ledger is a public API.

TrainToEarn doesn't ask you to trust the numbers. It shows them.
https://earn.onchainai.fund

**Post 5 — the challenge**
Challenge: write the Solana explanation you wish a model had given you.

Submit it to TrainToEarn. If Jev rates it Gold or better, you've earned $CLAWD and made every future model smarter about Solana.

### Discord announcement (DRAFT)

> 🦞 **TrainToEarn is LIVE — get your Solana knowledge rated, earn $CLAWD**
>
> TrainToEarn by OnchainAI is open: https://earn.onchainai.fund
>
> **What it is:** submit Solana training data (guides, Q&A pairs, worked examples), the Jev AI decision model rates it in realtime against 5 quality checks, and quality data earns $CLAWD from the project treasury.
>
> **How to start (2 minutes):**
> 1. Connect your Solana wallet — that's your account, no email/password
> 2. Portfolio tab → Jev panel → paste or upload (.txt/.md/.json/.jsonl/.csv, ≤256 KB)
> 3. Get your score, tier, and CLAWD instantly — your submission appears in the live feed on the homepage
> 4. Claim from 100 CLAWD in the Rewards panel; payouts settle from the treasury to your wallet only
>
> **Tiers:** Bronze ×1 · Silver 65+ ×2.5 · Gold 75+ ×4 · Diamond 85+ ×6 · Platinum 92+ ×8
>
> Full guide + API + agent skill: [GUIDE REPO URL]
> ⚠️ Never submit seed phrases or private keys — TrainToEarn never asks for them, and secret-bearing data fails the safety check anyway.

### Blog / announcement post (DRAFT)

# Your Solana Knowledge Is Training Data Now

Every Solana developer carries a private dataset: the PDA derivation they finally understood at 2 a.m., the rent error they debugged for an afternoon, the Anchor pattern they now write from memory. That knowledge is exactly what AI models lack about Solana — and until now, there was no market for it.

**TrainToEarn**, live today from OnchainAI, is that market.

## How it works

Connect a Solana wallet at [earn.onchainai.fund](https://earn.onchainai.fund) — the wallet is your account; there is no email, no password. Submit training data (a guide, an instruction/response pair, a worked example) by pasting it or uploading a file. **Jev**, a decision model from TypeSafe AI, rates your submission in realtime against five checks: is it Solana-specific, does it teach something, is it original, is it well-formed, and is it safe to train on?

Your score (0–100) sets a tier — Bronze through Platinum — and a reward multiplier up to ×8. Rewards accrue in a public ledger, and from 100 CLAWD you can claim. Payouts are settled from the project treasury, which holds ~293M CLAWD on-chain, to the wallet that earned them — and only that wallet.

## Rated in public, on purpose

Most "earn" platforms ask you to trust their numbers. TrainToEarn publishes them: a live feed of every rating as it happens, a showcase of the highest-rated data ever submitted, and a public API for the feed, the stats, the ledger, and the treasury balance. If a rating ever has to fall back to a deterministic heuristic because the AI gateway is unreachable, the rating says so — `heuristic-fallback` — instead of pretending otherwise.

## Quality is the strategy

Unsafe data caps at 20 points. Keyword-stuffed hype scores near zero. A complete, correct, well-structured explanation of something real — that's what tops the showcase and earns Platinum rates. The bar is public, so read the showcase, then beat it.

**Start here:** the [quick-start guide](GUIDE.md) takes two minutes. The full guide, API reference, and an agent skill file live in this repo.

Your knowledge is worth something now. Prove it. 🦞

---

## Campaign guardrails

- **Only real numbers, ever.** Any stat in any post must come from the live API at post time. If a number isn't in `/api/submissions/stats` or `/api/rewards/treasury`, it doesn't ship.
- **No earnings promises.** Copy states the formula and the minimum claim; it never projects income.
- **No fake urgency or fake social proof.** No invented user counts, testimonials, or payout screenshots — screenshots come from the real live feed.
- **Safety line in every long-form piece:** never submit seed phrases/private keys; payouts only to the earning wallet.
