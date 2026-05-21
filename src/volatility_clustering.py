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

    volatility_proxy = (
        returns[ticker].abs()
    )

    plt.figure(figsize=(12,5))
    plt.plot(
        volatility_proxy
    )

    plt.title(
        f"Volatility Clustering: {ticker}"
    )

    plt.xlabel("Date")
    plt.ylabel("Absolute Returns")

    plt.tight_layout()

    plt.savefig(
        f"figures/volatility_clustering_{ticker}.png"
    )

    plt.show()
