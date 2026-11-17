# TrainToEarn — Quick Start (One Page)

**Your Solana knowledge is training data. Get it rated by an AI judge. Earn $CLAWD.**

Full guide: [README.md](README.md) · App: https://earn.onchainai.fund

---

## 1. Sign in (30 seconds)

- Install a Solana wallet: [Phantom](https://phantom.app), [Solflare](https://solflare.com), or [Backpack](https://backpack.app).
- Go to **https://earn.onchainai.fund** and click **Select Wallet**.
- Your wallet is your account — no email, no password, nothing to sign.

## 2. Submit (2 minutes)

- Open the **Portfolio** tab → **Jev rating panel**.
- **Paste** Solana training data, or **upload** a `.txt` / `.md` / `.json` / `.jsonl` / `.csv` file (max 256 KB).
- Best format — instruction/response pairs that teach something real:

```
Instruction: How is a Solana PDA derived, and who can sign for it?
Response: A PDA is derived from a program ID + seed bytes and lies off the
ed25519 curve, so no private key exists. Only the owning program can sign
for it, via invoke_signed with the same seeds and bump.
```

- Click **Rate my data**.

## 3. Get rated (realtime)

Jev (a TypeSafe AI decision model) checks five things: **Solana-specific · teaches something · original · well-formed · safe to train**. Unsafe data caps at 20 points.

| Tier | Score | Reward multiplier |
|------|-------|-------------------|
| Bronze | 0+ | ×1 |
| Silver | 65+ | ×2.5 |
| Gold | 75+ | ×4 |
| Diamond | 85+ | ×6 |
| Platinum | 92+ | ×8 |

Reward per submission = `max(25, (KB + 100) × multiplier)` CLAWD. Your submission instantly appears in the **live feed** on the homepage, and top scores land in the **showcase**.

## 4. Claim (from 100 CLAWD)

- **Portfolio** tab → **CLAWD Rewards** panel → **Claim**.
- Minimum claim: **100 CLAWD**. Your claim becomes a pending payout, settled from the project treasury (`6rEiHJ…ADB4Z`) **to your wallet only**, with the transaction link recorded in your payout history.

## Safety in one breath

Never submit seed phrases or private keys (it also tanks your score). TrainToEarn never asks for them. Payouts can only go to the wallet that earned them — anyone saying otherwise is scamming you.

**$CLAWD** · Solana · mint `8cHzQHUS2s2h8TzCmfqPKYiM4dSt4roa3n7MyRLApump`
