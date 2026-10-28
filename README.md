# AIxTech Crypto Trading Information System

> **What this is:** a reference implementation and AI-agent harness for building
> automated cryptocurrency trading *information* systems. It demonstrates modular
> strategies per asset class, a cyber/data security architecture, CI quality gates,
> synthetic data only, and full AI-disclosure trails.
>
> **Not financial advice. No live trading. Synthetic data only.**

[![CI](https://github.com/kkzee92/aixtech-crypto-trading-system/actions/workflows/ci.yml/badge.svg)](https://github.com/kkzee92/aixtech-crypto-trading-system/actions)

## Key features

- **Asset-class strategies**
  - Bitcoin (BTC): Trend-following / moving-average crossover
  - Ethereum (ETH): Momentum + volume confirmation
  - Large/mid-cap alts: Volatility-adjusted mean reversion
  - Stablecoins: Informational yield/arbitrage monitoring (no execution)
- **Cyber & data security architecture**
  - Secrets exclusively via environment variables
  - gitleaks + PDPA-style tripwires
  - Audit logging, input validation, injectable data fetchers
  - No private keys, API keys, or personal data in repo
- **AI-agent harness** (inspired by aixtech-agent-harness-demo)
  - AGENTS.md rules
  - Task briefs
  - 6+ CI gates
  - Human review + disclosure logs

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt && pip install -e .
python -m cryptoinfo demo
```

See [docs/architecture.md](docs/architecture.md) and [docs/security-architecture.md](docs/security-architecture.md).

## Licence

MIT. Synthetic data only. Not for production trading without independent audit and risk controls.
