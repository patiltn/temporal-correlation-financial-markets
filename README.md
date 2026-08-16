# Temporal Correlation Analysis of Financial Time Series

A quantitative finance project analysing temporal dependence, autocorrelation, volatility clustering, and regime-dependent market behaviour in financial time series.

## Overview

This project investigates whether daily equity returns contain temporal structure and whether market behaviour exhibits momentum, mean reversion, or volatility persistence.

The analysis focuses on SPY as a proxy for the US equity market.

## Methods

The project includes:

- Historical market data collection
- Daily return computation
- Autocorrelation analysis
- Lag-1 return correlation
- Momentum vs mean-reversion diagnostics
- Volatility clustering analysis
- Rolling temporal correlation analysis

## Key Results

### 1. Autocorrelation of Daily Returns

Daily SPY returns show weak autocorrelation, suggesting limited direct predictability from past returns.

![Autocorrelation](figures/autocorrelation_SPY.png)

### 2. Volatility Clustering

Absolute returns show clear clustering, indicating that market volatility is persistent over time.

![Volatility Clustering](figures/volatility_clustering_SPY.png)

### 3. Momentum vs Mean Reversion

Lag-1 correlation was found to be mildly negative, suggesting weak short-term mean reversion.

![Momentum vs Mean Reversion](figures/momentum_vs_mean_reversion_SPY.png)

### 2. Volatility Clustering

Absolute returns show visible bursts of activity, suggesting market volatility is persistent over time rather than evenly spread out.

![Volatility Clustering](figures/volatility_clustering_SPY.png)

To formally test this rather than relying on visual inspection, I computed the autocorrelation of absolute returns. Every lag from 1 to 30 days sits well outside the 95% confidence band (roughly 0.25-0.39 versus a band of about ±0.06), confirming genuine, statistically significant clustering -- in sharp contrast to raw returns, which show no such structure at any lag.

![Autocorrelation of Absolute Returns](figures/acf_abs_returns_SPY.png)

## Key Insight

Daily returns are difficult to predict directly, but volatility exhibits temporal persistence. This supports the idea that market risk has memory even when returns themselves appear close to random.

## Skills Demonstrated

- Financial time-series analysis
- Autocorrelation modelling
- Volatility clustering
- Rolling-window statistics
- Momentum and mean-reversion diagnostics
- Python: Pandas, NumPy, Statsmodels, Matplotlib

## Repository Structure

data/  
figures/  
notebooks/  
src/
