# Cyber & Data Security Architecture

## Principles
1. **Secrets never in repo** — environment variables + secret managers only.
2. **Least privilege** — read-only information system by default; no withdrawal permissions.
3. **Audit everything** — structured logs of signals, decisions, data sources.
4. **Synthetic data for development** — all fixtures labelled SYNTHETIC.
5. **Defense in depth** — validation, rate limiting notes, anomaly detection stubs, gitleaks, dependency scanning.
6. **AI-agent constraints** — AGENTS.md forbids loading real keys or user data into context.

## Controls
- gitleaks in CI
- Input sanitisation in data.py
- Injectable fetchers (no network in tests)
- Licence allow-list
- Human review required for any strategy or risk change
- Explicit risk warnings in every signal output

This is a demonstration architecture, not a production-ready security certification.
