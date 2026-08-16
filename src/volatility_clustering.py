import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf


if __name__ == "__main__":

    prices = pd.read_csv(
        "data/stock_prices.csv",
        index_col=0,
        parse_dates=True
    )

    returns = prices.pct_change().dropna()

    ticker = "SPY"

    volatility_proxy = returns[ticker].abs()

    plt.figure(figsize=(10, 5))
    plt.plot(volatility_proxy)

    plt.title(f"Volatility Clustering: {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Absolute Returns")

    plt.tight_layout()

    plt.savefig(f"figures/volatility_clustering_{ticker}.png")
    plt.show()

    # Autocorrelation of the absolute-return series itself -- this is
    # the formal test for volatility clustering, rather than relying on
    # visual inspection of the raw magnitude series above.
    plt.figure(figsize=(10, 5))
    plot_acf(volatility_proxy, lags=30)

    plt.title(f"Autocorrelation of Absolute Returns: {ticker}")
    plt.tight_layout()
    plt.savefig(f"figures/acf_abs_returns_{ticker}.png")
    plt.show()

    print("Autocorrelation of |returns| (volatility clustering check):")
    for lag in range(1, 11):
        corr = volatility_proxy.autocorr(lag=lag)
        print(f"Lag {lag}: {corr:.4f}")
