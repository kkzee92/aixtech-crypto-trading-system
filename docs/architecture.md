# Architecture

## Data flow

```mermaid
flowchart LR
    subgraph Inputs
        SYN[Synthetic OHLCV fixtures]
        LIVE["Optional live feed (injectable, env keys)"]
    end
    SYN --> D[data.py - load / validate]
    LIVE --> D
    D --> S[strategies/<asset>.py]
    S --> R[risk.py - position sizing, drawdown]
    R --> SEC[security.py - audit log, validation]
    SEC --> CLI[cli.py]
```

## Asset classes
- BTC: SMA crossover trend
- ETH: ROC momentum + volume
- Alts: Bollinger-style mean reversion
- Stables: Spread monitoring

## Security layers
See docs/security-architecture.md
