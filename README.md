<div align="center">

**AI product & forward deployed engineer · founder of [mokka](https://mokka-agentur.de)**

I put AI into the systems companies already run, and publish the numbers that show whether it works.

[Hugging Face](https://huggingface.co/Gjusev) · [Kaggle](https://www.kaggle.com/gjusev) · [LinkedIn](https://www.linkedin.com/in/youssef-o-6b93611b7/) · [mokka](https://mokka-agentur.de)

<!-- stats:start -->
<table><tr>
<td align="center" width="200"><h3>4+</h3><sub>products<br>in production</sub></td>
<td align="center" width="200"><h3>1,078</h3><sub>PyPI downloads<br>4 packages</sub></td>
<td align="center" width="200"><h3>647</h3><sub>downloads of the<br>VoxEntity-EU benchmark</sub></td>
<td align="center" width="200"><h3>21</h3><sub>likes on Hugging Face<br>8 models, datasets, demos</sub></td>
</tr></table>
<sub>Live from PyPI and Hugging Face, checked daily · last change 2026-10-31</sub>
<!-- stats:end -->

</div>

### In production

- **[Datenmaske](https://datenmaske.de)** · offline GDPR redaction of PDFs for law firms and authorities. Recall 75% → 85% on a 1,428-entity benchmark.
- **[Klarbescheid](https://klarbescheid.de)** · explains German administrative notices in plain language and flags likely errors. Unknown domain to shipped product in 6 weeks.
- **Nexary** · knowledge platform inside a client's own network: hybrid search, reranking, OCR. [Portfolio export](https://github.com/Gjusev/nexary-platform).

### Models & research

| | What it is | Measured |
|---|---|---|
| **[MK-SH-V](https://github.com/Gjusev/mk-sh-v)** | 260M visual decision model: a choice, or a refusal below a validated gate | **0.839** on real held-out screenshots vs 0.731 for a ~15× larger model; trails it on receipts |
| **[MK-SH-1](https://github.com/Gjusev/MK-SH-1)** | 140M text decision model with calibrated abstention | **97.9%** on numeric thresholds; calibration error 0.073 → 0.016 |
| **[laya-triage](https://github.com/Gjusev/laya-triage)** | support-ticket routing, 77 intents → 8 departments | **89.8%** on the full 3,080-ticket BANKING77 test |
| **[VoxEntity-EU](https://github.com/Gjusev/voxentity-eu)** | does speech recognition catch the exact phone number? DE/FR | best ASR gets **37.1%** of slots exact, against a 90.8% ceiling |
| **[gate-calibrated](https://github.com/Gjusev/gate-calibrated)** | act-or-ask gate for tool-using agents, on tau-bench | wrong writes held at **1.7%** (α 0.02), but no win over simple baselines |

<sub>Each repo carries the sample sizes, confidence intervals and the point where the number stops holding.</sub>

### Tools

- **[nitelos](https://github.com/Gjusev/nitelos)** · did the agent really do what it says? Checks the evidence, not the agent's report
- **[voice-evals](https://github.com/Gjusev/voice-evals)** · replay calls, probe live voice agents, fail CI on a regression
- **[note-lm](https://github.com/Gjusev/note-lm)** · local research notebook where every claim keeps its source passage
- **[hard-mode](https://github.com/Gjusev/hard-mode)** · **[skill-issue](https://github.com/Gjusev/skill-issue)** · **[i-didnt-write-this](https://github.com/Gjusev/i-didnt-write-this)** · tools for working with coding agents

<details>
<summary>More projects</summary>

**Apps** · [HeizPro KI](https://github.com/Gjusev/heizpro-ki) German voice agent for heating-service leads · [Maqrivo](https://github.com/Gjusev/maqrivo) meal planning with CP-SAT · [Somatriq](https://github.com/Gjusev/somatriq) self-hosted wearable data · [Studio Command Center](https://github.com/Gjusev/studio-command-center) · [Falschinfo-Radar](https://github.com/Gjusev/falschinfo-radar) · [Nexary website](https://github.com/Gjusev/nexary)

**Decision-model tooling** on [laya](https://github.com/NandhaKishorM/laya) and [Cloudflare Clef](https://huggingface.co/Cloudflare/clef) · [laya-router](https://github.com/Gjusev/laya-router) · [clef-router](https://github.com/Gjusev/clef-router) · [laya-compactor](https://github.com/Gjusev/laya-compactor) · [clef-compactor](https://github.com/Gjusev/clef-compactor) · [laya-evals](https://github.com/Gjusev/laya-evals) · [clef-evals](https://github.com/Gjusev/clef-evals) · [laya-evals-gate](https://github.com/Gjusev/laya-evals-gate) · [laya-phishield](https://github.com/Gjusev/laya-phishield) · [laya-warden](https://github.com/Gjusev/laya-warden)

**Regression kits** · [locale-invoice-check](https://github.com/Gjusev/locale-invoice-check) invoice extraction in EN/DE/ES · [vision-input-check](https://github.com/Gjusev/vision-input-check) vision APIs across image re-encodes

</details>

---

**Open to** AI engineering, full-stack product and forward deployed roles · EU or relocation · from November 2026 · [LinkedIn](https://www.linkedin.com/in/youssef-o-6b93611b7/)

<sub>4+ years of professional software engineering; mokka runs alongside a full-time role building integrations for enterprise clients.<br>
Python · PyTorch · TypeScript · Next.js · FastAPI · LangGraph · Tauri · PostgreSQL · Qdrant · Docker · Playwright</sub>
