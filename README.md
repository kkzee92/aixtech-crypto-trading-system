# AIxTech Crypto Trading Information System (Enhanced)

> **What this is:** a reference implementation and AI-agent harness for building
> automated cryptocurrency trading *information* systems. It demonstrates modular
> strategies per asset class, a robust cyber/data security architecture, CI quality gates,
> synthetic data only, and full AI-disclosure trails.
>
> **Not financial advice. No live trading. Synthetic data only. Research and education.**

[![CI](https://github.com/kkzee92/aixtech-crypto-trading-system/actions/workflows/ci.yml/badge.svg)](https://github.com/kkzee92/aixtech-crypto-trading-system/actions)

## Key features (enhanced)

- **Asset-class strategies**
  - Bitcoin (BTC): Adaptive trend-following with volatility filter
  - Ethereum (ETH): Momentum + volume / network activity confirmation
  - Large/mid-cap alts: Volatility-adjusted mean reversion + BTC relative strength
  - Stablecoins: Informational yield/depeg monitoring (no execution)
- **Cyber & data security architecture**
  - Secrets exclusively via environment variables / external managers
  - gitleaks + PDPA-style tripwires + audit logging
  - Input validation, injectable data fetchers, least-privilege design
  - No private keys, API keys, or personal data in repo
  - Threat model and operational security notes
- **AI-agent harness** (inspired by aixtech-agent-harness-demo)
  - AGENTS.md rules tailored for financial systems
  - Task briefs
  - CI gates (lint, test, secrets, licences)
  - Human review + disclosure logs

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt && pip install -e .
python -m cryptoinfo demo
```

See [docs/architecture.md](docs/architecture.md), [docs/security-architecture.md](docs/security-architecture.md), and [docs/strategies-per-asset.md](docs/strategies-per-asset.md).

## Licence

MIT. Synthetic data only. Not for production trading without independent audit, risk controls, and regulatory compliance.
