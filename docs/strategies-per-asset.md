# Trading Strategies per Asset Class (Enhanced)

All strategies produce **informational signals only**. No order execution, no API trading keys required for core logic.

## Bitcoin (BTC) - Digital Gold / Macro Trend Asset
- **Primary**: Adaptive SMA crossover (5/20) with ATR volatility filter.
- **Secondary**: RSI divergence on higher timeframes for confirmation.
- **Rationale**: BTC exhibits strong trend persistence driven by institutional flows and macro liquidity. Volatility filter reduces whipsaws in choppy regimes.
- **Risk controls**: Position size scaled by inverse ATR; hard drawdown alerts.

## Ethereum (ETH) - Smart Contract Platform / DeFi Beta
- **Primary**: Momentum (ROC) + on-chain activity proxy (volume + funding rate stub).
- **Enhancement**: Gas fee regime detection (high gas = congestion = caution).
- **Rationale**: ETH is more sensitive to network usage, DeFi TVL changes, and staking flows than pure price trends.

## Large/Mid-cap Alts (e.g., SOL, AVAX, LINK)
- **Primary**: Bollinger Band mean reversion + relative strength vs BTC.
- **Enhancement**: Correlation filter — only mean-revert when BTC is ranging.
- **Rationale**: Alts have higher beta and mean-reversion frequency after extreme moves relative to BTC.

## Stablecoins & Yield Monitoring
- Informational only: depeg detection (price vs $1), yield spread alerts across protocols (stub).
- No directional trading; pure risk monitoring.

## Cross-asset enhancements
- Regime classifier (trend / range / high-vol) shared across assets.
- Portfolio-level risk: max correlated exposure.
- Backtest harness using synthetic regimes (bull, bear, sideways, crash).

## Next steps for production (out of scope for this demo)
- Multi-exchange data aggregation with signed requests.
- Real-time websocket adapters (injected).
- Independent risk engine with circuit breakers.
