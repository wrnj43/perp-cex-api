# perp-cex-api

Python API for perp.fi similar to centralized exchange APIs

1. Open position with amount of collateral, amount of leverage, asset name, long/short.
2. Close position, fully or partially.
3. Account info (wallet USDC amount, open positions, total current pnl).
4. Get open position info (position size, pnl, liquidation price, opened timestamp, margin ratio).
5. Get market current data (funding rate, volume 24, price impact values, mark price, index price).
6. Get historical market values (price candles with time window).
7. Fetch order book, past x positions for a given market pair.
8. Increase/decrease leverage using USDC deposit/withdraw.
9. Get liquidation history (market overall, user address specific).
10. async REST calls.
