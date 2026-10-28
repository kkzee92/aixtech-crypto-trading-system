# AGENTS.md - rules for AI coding agents

## Scope
- Work only on the current task brief.
- Never push to main or weaken CI gates.
- One task = one PR.

## Data & security (critical for crypto)
- Use **only synthetic fixtures** in `fixtures/`. Never real exchange data containing user info, never private keys, seed phrases, or API keys in code/docs/commits.
- Read optional exchange keys from environment variables only (e.g. `EXCHANGE_API_KEY`).
- gitleaks and secret scanning are mandatory. Treat any flag as a real incident.
- No production personal data. PDPA-style checks apply to any identifiers.

## Engineering
- Python >= 3.10, prefer stdlib. New dependencies need approval and licence check.
- Tests first. Never hit real network in tests; inject fetchers.
- Run local CI before review.
- Disclose AI assistance in commits and docs.

## Definition of Done
CI green + recorded human review.
