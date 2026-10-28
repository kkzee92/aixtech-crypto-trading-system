# Trading Strategies per Asset Class

All strategies produce **informational signals only**. No order execution.

## Bitcoin (BTC) - Store of value / macro trend
- Primary: SMA crossover (5/20)
- Rationale: BTC often exhibits stronger trends; persistence of direction.
- Risk: High drawdowns possible; use volatility filter in production.

## Ethereum (ETH) - Smart contract platform / DeFi beta
- Primary: Rate-of-change momentum confirmed by volume spike
- Rationale: ETH reacts to network activity and DeFi flows; volume confirms conviction.

## Large/mid-cap Alts
- Primary: Bollinger-band mean reversion
- Rationale: Higher relative volatility; more frequent mean-reverting moves after extremes.

## Stablecoins
- Informational only: monitor depeg spreads and yield differentials.
- No directional trading; focus on risk alerts.

## Enhancement roadmap
- Multi-timeframe confirmation
- Regime detection (trend vs range)
- Correlation filters across assets
- Backtest harness with synthetic regimes
- Integration with risk module for position sizing
