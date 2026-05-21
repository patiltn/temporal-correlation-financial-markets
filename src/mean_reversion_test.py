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

    lagged_returns = (
        returns[ticker]
        .shift(1)
        .dropna()
    )

    future_returns = (
        returns[ticker]
        .iloc[1:]
    )

    correlation = (
        lagged_returns
        .corr(future_returns)
    )

    print(
        f"Lag-1 correlation ({ticker}): "
        f"{correlation:.4f}"
    )

    plt.figure(figsize=(8,6))

    plt.scatter(
        lagged_returns,
        future_returns,
        alpha=0.3
    )

    plt.xlabel(
        "Yesterday Return"
    )

    plt.ylabel(
        "Today Return"
    )

    plt.title(
        f"Momentum vs Mean Reversion: {ticker}"
    )

    plt.tight_layout()

    plt.savefig(
        f"figures/momentum_vs_mean_reversion_{ticker}.png"
    )

    plt.show()
