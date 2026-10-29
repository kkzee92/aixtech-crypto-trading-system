# Cyber & Data Security Architecture (Enhanced)

## Core Principles for Crypto Trading Information Systems
1. **Zero secrets in repository** — All API keys, private keys, seeds via environment variables or external secret managers (AWS Secrets Manager, HashiCorp Vault, etc.). Never commit.
2. **Least privilege by design** — Information system only. No withdrawal, no trading execution scopes on any API keys. Read-only market data preferred.
3. **Defense in depth**
   - Input validation and sanitisation on all external data.
   - Rate limiting and circuit breakers on data fetchers.
   - Anomaly detection stubs (sudden volume spikes, price gaps).
   - Structured audit logging of every signal generation (timestamp, inputs, output, data source).
4. **Synthetic data only for development and CI** — All fixtures explicitly labelled SYNTHETIC. Real exchange data never stored in repo.
5. **AI-agent constraints** — AGENTS.md strictly forbids loading real keys, user PII, or production data into agent context. PDPA-style tripwires extended to crypto identifiers (wallet addresses in certain contexts).
6. **Supply-chain security** — Licence allow-list, Dependabot, gitleaks on full history, signed commits recommended.
7. **Operational security notes**
   - Separate environments (dev/staging/prod).
   - Immutable infrastructure where possible.
   - Regular key rotation.
   - Monitoring for unusual API usage.

## Controls Implemented in This Repo
- gitleaks CI gate.
- Injectable data fetchers (tests remain offline).
- Explicit risk disclaimers on every signal.
- Human review mandatory for strategy or risk changes.
- No private key handling code paths.

## Threat Model Highlights
- API key compromise → limited by read-only scopes and no withdrawal rights.
- Prompt injection / agent misuse → constrained by AGENTS.md and CI gates.
- Data leakage → synthetic fixtures + secret scanning.
- Supply chain → pinned dependencies + licence checks.

This architecture is a demonstration suitable for research and education. Production deployment requires independent security audit, formal threat modeling, and regulatory compliance review (where applicable).
