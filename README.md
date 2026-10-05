<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg?v=2" />
  <img src="assets/hero-light.svg?v=2" width="640" alt="Animated Medusa turns from profile to meet the viewer's gaze" />
</picture>

### Voice agents, open-source AI tools & independent software.

I'm Youssef, founder of [**mokka**](https://mokka-agentur.de), based in Siegen, Germany.<br>
I build tools to test AI systems, make their decisions inspectable, and keep data under your control.

[Selected work](#selected-work) · [AI tooling](#ai-tooling) · [More projects](#more-projects) · [Get in touch](https://www.linkedin.com/in/youssef-o-6b93611b7/)

<sub>Siegen, DE / web · AI · privacy / palestina libre</sub>

</div>

---

## Selected work

Open-source projects with code, examples, and a way to try them.

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/Gjusev/voice-evals"><img src="https://raw.githubusercontent.com/Gjusev/voice-evals/main/docs/assets/voice-evals-demo-poster.jpg" width="100%" alt="voice-evals: replay scoring, live probes and inspectable session artifacts" /></a>
      <h3><a href="https://github.com/Gjusev/voice-evals">voice-evals</a></h3>
      <p>Replay calls or probe a live WebSocket agent. Gate on transcription, latency, interruptions, and task outcomes.</p>
      <p><sub>Python · CLI + library · Apache-2.0</sub></p>
      <p><a href="https://github.com/Gjusev/voice-evals">Code</a> · <a href="https://pypi.org/project/voice-evals/">PyPI</a> · <a href="https://github.com/Gjusev/voice-evals#watch-the-demo">Demo</a> · <a href="https://www.kaggle.com/code/gjusev/voice-evals-offline-benchmark">Kaggle</a></p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/Gjusev/note-lm"><img src="https://raw.githubusercontent.com/Gjusev/note-lm/main/docs/screenshots/note-lm-launch-poster.jpg" width="100%" alt="note-lm: a local research notebook with sources and traceable evidence" /></a>
      <h3><a href="https://github.com/Gjusev/note-lm">note-lm</a></h3>
      <p>A local research notebook with versioned sources, cited claims, and evidence you can trace back to the original passage.</p>
      <p><sub>Windows desktop · Local storage and models · MIT</sub></p>
      <p><a href="https://github.com/Gjusev/note-lm">Code</a> · <a href="https://github.com/Gjusev/note-lm/releases/latest">Download</a> · <a href="https://github.com/Gjusev/note-lm#see-it-in-20-seconds">Demo</a></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Gjusev/laya-triage">laya-triage</a></h3>
      <p>Local support-ticket routing with urgency signals and human handoff. Includes a fine-tuned BANKING77 model and reproducible evaluations.</p>
      <p><sub>Python · Local decision model · Apache-2.0</sub></p>
      <p><a href="https://github.com/Gjusev/laya-triage">Code</a> · <a href="https://laya-triage-8spuhg8fa5qjy8hiteomux.streamlit.app/">Try the app</a> · <a href="https://huggingface.co/Gjusev/laya-triage-banking77">Model</a> · <a href="https://github.com/Gjusev/laya-triage#measured-results">Results</a></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Gjusev/heizpro-ki">HeizPro KI</a></h3>
      <p>A German-speaking voice agent that qualifies heating-service leads, with a dashboard and a two-agent call simulator.</p>
      <p><sub>Next.js · ElevenLabs · PostgreSQL · MIT</sub></p>
      <p><a href="https://github.com/Gjusev/heizpro-ki">Code</a> · <a href="https://mischa.mokka-dev.de">Live demo</a></p>
    </td>
  </tr>
</table>

## AI tooling

Small Python packages for routing, retrieval, and evaluation. The laya tools use a local decision model; the Clef tools integrate with Cloudflare's decision models.

| Task | Local · laya | Cloudflare · Clef |
| --- | --- | --- |
| **Evaluate** — confidence audits & CI gates | [laya-evals](https://github.com/Gjusev/laya-evals) · [PyPI](https://pypi.org/project/laya-evals/) | [clef-evals](https://github.com/Gjusev/clef-evals) · [PyPI](https://pypi.org/project/clef-evals/) |
| **Route** — choose an LLM per request | [laya-router](https://github.com/Gjusev/laya-router) · [PyPI](https://pypi.org/project/laya-router/) | [clef-router](https://github.com/Gjusev/clef-router) · [PyPI](https://pypi.org/project/clef-router/) |
| **Compact** — fit evidence to a token budget | [laya-compactor](https://github.com/Gjusev/laya-compactor) · [PyPI](https://pypi.org/project/laya-compactor/) | [clef-compactor](https://github.com/Gjusev/clef-compactor) · [PyPI](https://pypi.org/project/clef-compactor/) |

**[laya-phishield](https://github.com/Gjusev/laya-phishield)** applies the same approach to phishing detection: local semantic signals, deterministic email checks, and an explainable risk score. [PyPI](https://pypi.org/project/laya-phishield/)

These are independent tools built on [laya](https://github.com/NandhaKishorM/laya) and [Cloudflare Clef](https://huggingface.co/Cloudflare/clef). Each repository documents its setup, benchmarks, and current limitations.

## More projects

Application code, architecture notes, and demos. Status reflects each repository's current scope.

- **[Nexary](https://github.com/Gjusev/nexary-platform)** — AI collaboration with hybrid RAG and audit trails for customer-controlled networks. Public portfolio export. [Architecture](https://github.com/Gjusev/nexary-platform/blob/main/docs/architecture.md) · [Screenshots](https://github.com/Gjusev/nexary-platform#screenshots).

- **[Studio Command Center](https://github.com/Gjusev/studio-command-center)** — inventory, equipment maintenance, and staff workflows for fitness studios. Prototype with demo data. [Setup](https://github.com/Gjusev/studio-command-center#quickstart) · [Screenshots](https://github.com/Gjusev/studio-command-center#screenshots).

- **[Somatriq](https://github.com/Gjusev/somatriq)** — self-hosted wearable data, traceable calculations, and personal experiments. Active prototype. [Architecture](https://github.com/Gjusev/somatriq/blob/main/docs/architecture.md) · [Screenshots](https://github.com/Gjusev/somatriq#screenshots).

[Browse all repositories →](https://github.com/Gjusev?tab=repositories)

## Working with

**Build** — Python, TypeScript, React, Next.js, FastAPI, Tauri.<br>
**Data & infrastructure** — PostgreSQL, Qdrant, Docker, n8n.<br>
**AI systems** — voice agents, RAG, local models, evaluation, Playwright testing.

## Document & vision evaluation

Your extractor reads the same invoice in three locales. Your vision API gets the same pixels. Measure both — offline-first regression kits with deterministic CI gates.

- **[locale-invoice-check](https://github.com/Gjusev/locale-invoice-check)** — EN/DE/ES invoice extraction, deterministic CI gates · [PyPI](https://pypi.org/project/locale-invoice-check/)
- **[vision-input-check](https://github.com/Gjusev/vision-input-check)** — pixel-identical vs lossy image variants, variance-aware gates · [PyPI](https://pypi.org/project/vision-input-check/)

---

**[mokka](https://mokka-agentur.de)** — websites, AI products, and automation for small businesses.<br>
Also building [klarbescheid](https://klarbescheid.de) for understandable benefits notices and [datenmaske](https://datenmaske.de) for PDF redaction.

[Let's build something useful →](https://www.linkedin.com/in/youssef-o-6b93611b7/)
