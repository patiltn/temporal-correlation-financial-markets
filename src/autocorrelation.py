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

    plt.figure(figsize=(10, 5))
    plot_acf(
        returns[ticker],
        lags=30
    )

    plt.title(f"Autocorrelation of Daily Returns: {ticker}")
    plt.tight_layout()
    plt.savefig(f"figures/autocorrelation_{ticker}.png")
    plt.show()

    print("First 10 autocorrelations:")
    for lag in range(1, 11):
        corr = returns[ticker].autocorr(lag=lag)
        print(f"Lag {lag}: {corr:.4f}")
