-- Top 10 Stocks by Average Daily Return
SELECT
    Ticker,
    AVG(Daily_Return) AS avg_daily_return
FROM stock_data
GROUP BY Ticker
ORDER BY avg_daily_return DESC
LIMIT 10;


-- Most Volatile Stocks
SELECT
    Ticker,
    AVG(Volatility) AS avg_volatility
FROM stock_data
GROUP BY Ticker
ORDER BY avg_volatility DESC
LIMIT 10;


-- Overbought Stocks (RSI > 70)
SELECT
    Date,
    Ticker,
    RSI
FROM stock_data
WHERE RSI > 70
ORDER BY Date DESC;


-- Oversold Stocks (RSI < 30)
SELECT
    Date,
    Ticker,
    RSI
FROM stock_data
WHERE RSI < 30
ORDER BY Date DESC;