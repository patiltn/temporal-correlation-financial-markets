import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":

    prices = pd.read_csv(
        "data/stock_prices.csv",
        index_col=0,
        parse_dates=True
    )

    returns = prices.pct_change().dropna()

    ticker = "SPY"

    rolling_corr = (
        returns[ticker]
        .rolling(window=60)
        .corr(
            returns[ticker].shift(1)
        )
    )

    plt.figure(figsize=(12,5))

    plt.plot(
        rolling_corr
    )

    plt.axhline(
        0,
        linestyle="--"
    )

    plt.title(
        f"Rolling Lag-1 Correlation: {ticker}"
    )

    plt.xlabel("Date")
    plt.ylabel("Lag-1 Correlation")

    plt.tight_layout()

    plt.savefig(
        f"figures/rolling_correlation_{ticker}.png"
    )

    plt.show()
