#!/usr/bin/env python3
"""Build TrainToEarn-Guide.pdf from the guide content using reportlab.

Layout: cover header block, styled headings, a real tier table, readable
body text, page-number footer. Run: python3 build_pdf.py
"""
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
)

PURPLE = colors.HexColor("#9945FF")
GREEN = colors.HexColor("#14F195")
DARK = colors.HexColor("#14141f")
GREY = colors.HexColor("#555560")
LIGHT = colors.HexColor("#f2f0fa")

styles = {
    "cover_title": ParagraphStyle("cover_title", fontName="Helvetica-Bold", fontSize=30,
                                  leading=36, textColor=colors.white, alignment=TA_LEFT),
    "cover_sub": ParagraphStyle("cover_sub", fontName="Helvetica", fontSize=13,
                                leading=18, textColor=colors.white, alignment=TA_LEFT),
    "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=17, leading=22,
                         textColor=PURPLE, spaceBefore=18, spaceAfter=6),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13, leading=17,
                         textColor=DARK, spaceBefore=12, spaceAfter=4),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10.5, leading=15,
                           textColor=DARK, spaceAfter=7, alignment=TA_LEFT),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=10.5, leading=15,
                             textColor=DARK, spaceAfter=4, leftIndent=14, bulletIndent=4),
    "mono": ParagraphStyle("mono", fontName="Courier", fontSize=8.6, leading=12,
                           textColor=GREY, spaceAfter=7),
    "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=10, leading=13, textColor=DARK),
    "cell_b": ParagraphStyle("cell_b", fontName="Helvetica-Bold", fontSize=10, leading=13,
                             textColor=colors.white),
    "footer": ParagraphStyle("footer", fontName="Helvetica", fontSize=8, leading=10,
                             textColor=GREY, alignment=TA_CENTER),
}


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)
    canvas.drawCentredString(LETTER[0] / 2, 0.55 * inch,
                             f"TrainToEarn Guide — earn.onchainai.fund — page {doc.page}")
    canvas.restoreState()


def build(path="TrainToEarn-Guide.pdf"):
    doc = BaseDocTemplate(path, pagesize=LETTER,
                          leftMargin=0.85 * inch, rightMargin=0.85 * inch,
                          topMargin=0.7 * inch, bottomMargin=0.8 * inch,
                          title="TrainToEarn Guide", author="OnchainAI")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="page", frames=[frame], onPage=footer)])

    s = styles
    story = []

    # ---- Cover header block ----
    cover = Table(
        [[Paragraph("TrainToEarn", s["cover_title"])],
         [Paragraph("Get your Solana training data rated by an AI judge. Earn $CLAWD.", s["cover_sub"])],
         [Paragraph("The complete user guide — OnchainAI", s["cover_sub"])]],
        colWidths=[doc.width],
    )
    cover.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PURPLE),
        ("LEFTPADDING", (0, 0), (-1, -1), 22),
        ("RIGHTPADDING", (0, 0), (-1, -1), 22),
        ("TOPPADDING", (0, 0), (0, 0), 20),
        ("BOTTOMPADDING", (0, -1), (0, -1), 20),
        ("TOPPADDING", (0, 1), (0, 1), 2),
        ("BOTTOMPADDING", (0, 1), (0, 1), 2),
    ]))
    story.append(cover)
    story.append(Spacer(1, 16))
    story.append(Paragraph(
        "<b>App:</b> https://earn.onchainai.fund &nbsp; <b>Token:</b> $CLAWD (Solana) — "
        "mint 8cHzQHUS2s2h8TzCmfqPKYiM4dSt4roa3n7MyRLApump<br/>"
        "<b>Rewards treasury:</b> 6rEiHJ4JUTWcC4wCUosTbaoBmpjHvUGLAQcogUwADB4Z", s["body"]))

    # ---- What is TrainToEarn ----
    story.append(Paragraph("What is TrainToEarn?", s["h1"]))
    story.append(Paragraph(
        "AI models are only as good as the data they train on, and good Solana-specific training "
        "data is scarce. TrainToEarn turns the community into the data pipeline: you submit Solana "
        "training data, the Jev AI decision model rates it in realtime, you earn $CLAWD based on "
        "quality, and you claim your earnings to your own wallet. There is no sign-up form, no "
        "email, no password — your Solana wallet is your account, your identity, and your payout "
        "address.", s["body"]))

    # ---- Step 1 ----
    story.append(Paragraph("Step 1 — Connect your Solana wallet", s["h1"]))
    story.append(Paragraph(
        "Install Phantom (phantom.app), Solflare (solflare.com), or Backpack (backpack.app). "
        "Go to https://earn.onchainai.fund, click <b>Select Wallet</b>, choose your wallet, and "
        "approve the connection. Connecting is free and does not give the site access to your "
        "funds — it only proves which wallet you control so ratings and rewards are credited "
        "to you. Write your wallet recovery phrase down on paper and keep it offline; never "
        "type it into any website, including this one.", s["body"]))

    # ---- Step 2 ----
    story.append(Paragraph("Step 2 — Submit training data", s["h1"]))
    story.append(Paragraph(
        "Open the <b>Portfolio</b> tab and find the Jev rating panel. Paste your data directly, "
        "or upload a file (.txt, .md, .json, .jsonl, .csv, up to 256 KB). The best format is one "
        "or more instruction/response pairs that teach something concrete about Solana — PDAs, "
        "accounts, rent, Anchor patterns, SPL tokens, debugging write-ups. Click <b>Rate my "
        "data</b>: your score, tier, verdicts, and $CLAWD earned come back in realtime, the "
        "rating is saved to your wallet's ledger, and your submission appears in the public "
        "live feed on the homepage. Very short samples score low; one focused, complete topic "
        "per submission scores best.", s["body"]))

    story.append(Paragraph("The five Jev checks", s["h2"]))
    for text in [
        "<b>Solana-specific</b> — actually about Solana, not generic blockchain filler.",
        "<b>Teaches something</b> — a model or person learns something concrete from it.",
        "<b>Original</b> — not copied boilerplate or repeated submissions.",
        "<b>Well-formed</b> — clear structure, a complete answer, working code where given.",
        "<b>Safe to train</b> — no secrets, no personal data, nothing harmful. Failing this "
        "check caps your score at 20.",
    ]:
        story.append(Paragraph(text, s["bullet"], bulletText="•"))

    story.append(Paragraph("Good vs. bad", s["h2"]))
    story.append(Paragraph(
        "<b>Good:</b> “Why does creating a token account fail with 'insufficient funds for "
        "rent', and how do you fix it? — Every account must hold the rent-exempt minimum for "
        "its byte size; a token account is 165 bytes, so fund it with at least "
        "getMinimumBalanceForRentExemption(165) lamports at creation.” Specific, teaches a "
        "cause and a fix, complete.", s["body"]))
    story.append(Paragraph(
        "<b>Bad:</b> “Solana is a fast blockchain. Crypto is the future. To the moon.” "
        "Generic hype, teaches nothing, keyword-stuffed — expect a score in the teens or "
        "lower.", s["body"]))

    # ---- Engine ----
    story.append(Paragraph("How the Jev rating engine works", s["h1"]))
    story.append(Paragraph(
        "Ratings come from Jev, a decision model from TypeSafe AI, reached through the Neon AI "
        "Gateway (model typesafeai-jev-1-14-0). Jev returns typed judgments — true/false "
        "verdicts with probabilities and a 0–5 quality rubric — which the platform blends "
        "deterministically: <b>55% Jev, 45% local heuristic</b>. If the gateway is unreachable, "
        "the rating falls back to the heuristic alone and is honestly labeled "
        "<i>heuristic-fallback</i>. If Jev judges data unsafe to train, the score is capped at "
        "20. Every rating is persisted against your wallet; your content itself is never "
        "published — the public feed shows only filename, size, score, tier, reward, and "
        "verdicts, with wallets truncated.", s["body"]))

    # ---- Tiers table ----
    story.append(Paragraph("Tiers and rewards", s["h1"]))
    tier_data = [
        [Paragraph("Tier", s["cell_b"]), Paragraph("Score", s["cell_b"]),
         Paragraph("Multiplier", s["cell_b"])],
        [Paragraph("Bronze", s["cell"]), Paragraph("0+", s["cell"]), Paragraph("×1", s["cell"])],
        [Paragraph("Silver", s["cell"]), Paragraph("65+", s["cell"]), Paragraph("×2.5", s["cell"])],
        [Paragraph("Gold", s["cell"]), Paragraph("75+", s["cell"]), Paragraph("×4", s["cell"])],
        [Paragraph("Diamond", s["cell"]), Paragraph("85+", s["cell"]), Paragraph("×6", s["cell"])],
        [Paragraph("Platinum", s["cell"]), Paragraph("92+", s["cell"]), Paragraph("×8", s["cell"])],
    ]
    table = Table(tier_data, colWidths=[doc.width / 3.0] * 3)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PURPLE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cfc8ee")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(table)
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "Reward per submission = <b>max(25, (size in KB + 100) × multiplier)</b> CLAWD. A 2 KB "
        "Gold submission earns (2 + 100) × 4 = 408 CLAWD; even a small Bronze submission earns "
        "at least the 25 CLAWD floor.", s["body"]))

    # ---- Claim ----
    story.append(Paragraph("Step 3 — Claim your $CLAWD", s["h1"]))
    story.append(Paragraph(
        "Open the Portfolio tab and find the CLAWD Rewards panel — it shows your earned, "
        "already-paid, pending, and claimable balances from the real ledger. Click <b>Claim</b> "
        "(minimum claim: 100 CLAWD). Your claim is recorded as a pending payout for the full "
        "claimable amount and settled from the project treasury wallet "
        "(6rEiHJ4JUTWcC4wCUosTbaoBmpjHvUGLAQcogUwADB4Z) <b>to the wallet that earned it — and "
        "only that wallet</b>. When a payout is sent, its transaction signature appears in your "
        "payout history with a Solscan link. Payouts are settled in batches by the project; "
        "the web server never holds private keys and cannot move funds.", s["body"]))

    # ---- Live feed ----
    story.append(Paragraph("The live feed and showcase", s["h1"]))
    story.append(Paragraph(
        "The homepage carries the public pipeline, refreshing live: a stats band (total "
        "submissions, contributors, CLAWD earned, average score), a live ratings feed, and "
        "the top-rated showcase of the highest-scoring submissions of all time. Study the "
        "showcase before you submit — it is the quality bar. Nothing in the feed is simulated.",
        s["body"]))

    # ---- API ----
    story.append(Paragraph("Public API reference", s["h1"]))
    story.append(Paragraph(
        "Base URL: https://traintoearn-backend-y6co.onrender.com — public, read-only, no key "
        "required.", s["body"]))
    for text in [
        "GET /api/submissions/recent?limit=20 — latest rated submissions (max 50).",
        "GET /api/submissions/top?limit=10 — highest-rated submissions of all time (max 25).",
        "GET /api/submissions/stats — totals: submissions, contributors, CLAWD earned, "
        "average score, last-24h count, best score.",
        "GET /api/rewards/balance/&lt;wallet&gt; — a wallet's earned / paid / pending / "
        "claimable CLAWD and payout history.",
        "GET /api/rewards/treasury — the treasury's live on-chain CLAWD and SOL balances.",
        "GET /api/jev/status — Jev gateway configuration and model in use.",
    ]:
        story.append(Paragraph(text, s["mono"], bulletText="•"))

    # ---- Safety ----
    story.append(Paragraph("Safety — read this", s["h1"]))
    for text in [
        "<b>Never submit seed phrases, private keys, or keypair files.</b> They fail the "
        "safety check, cap your score at 20 — and TrainToEarn never asks for them, in the app, "
        "in Discord, or anywhere else. Anyone who does is scamming you.",
        "<b>Payouts only ever go to the wallet that earned them.</b> A claim can never be "
        "redirected to another address, by you or anyone else.",
        "<b>Verify addresses character-for-character:</b> app earn.onchainai.fund; $CLAWD mint "
        "8cHzQHUS2s2h8TzCmfqPKYiM4dSt4roa3n7MyRLApump; treasury "
        "6rEiHJ4JUTWcC4wCUosTbaoBmpjHvUGLAQcogUwADB4Z.",
        "<b>Your wallet, your keys.</b> Keep your recovery phrase offline, in a wallet you "
        "control.",
    ]:
        story.append(Paragraph(text, s["bullet"], bulletText="•"))

    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Full guide, quick start, campaign, and agent skill: see README.md, GUIDE.md, "
        "CAMPAIGN.md, and SKILL.md in this repository. MIT licensed — © OnchainAI / "
        "TrainToEarn contributors.", s["body"]))

    doc.build(story)
    print(f"Built {path}")


if __name__ == "__main__":
    build()
