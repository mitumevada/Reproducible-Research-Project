# Poland Macroeconomic Time Series Analysis

# 1. Research Background

The relationship between macroeconomic conditions and housing market dynamics has been widely studied in the economic literature. In particular, a large body of research highlights the role of monetary policy variables, such as interest rates, in shaping housing price movements. Lower interest rates tend to reduce borrowing costs and stimulate housing demand, while higher rates may exert downward pressure on housing prices.

In addition to interest rates, inflation is also considered an important macroeconomic factor affecting housing markets. As a key indicator of overall price dynamics, inflation can influence both real asset values and investment behavior. Prior studies suggest that housing prices may act as a hedge against inflation, although the strength and timing of this relationship remain subject to empirical investigation.

While these relationships are well documented, the interactions between macroeconomic variables and housing prices are inherently dynamic and may involve lagged effects. As a result, time series approaches have been widely used to capture such dynamics and to analyze how shocks to one variable propagate through the system over time.

Building on this literature, this project focuses on the Polish economy and examines the joint behavior of housing prices, interest rates, and inflation within a time series framework. By doing so, we aim to provide empirical evidence on how these key variables interact over time and whether their relationships exhibit systematic patterns in a country-specific context.


# 2. Research Objective

The objective of this project is to examine how housing prices in Poland are related to interest rates and inflation over time. Using quarterly data from the first quarter of 2010 to the fourth quarter of 2025, we investigate the dynamic interactions among these variables within a macroeconomic framework.

Specifically, we aim to investigate whether changes in interest rates and inflation are associated with subsequent movements in housing prices, and whether these effects occur immediately or with a time lag.

# 3. Data

Since inflation and interest rates are originally reported at a monthly frequency, while the housing price index is available at a quarterly frequency, all variables are converted to a common quarterly frequency to ensure temporal consistency and improve the reliability of the time-series analysis.

## 3.1 Data Sources

 - Housing price: Eurostat
 - Interest rate: Eurostat
 - Inflation: OECD Data Explorer

## 3.2 Data Processing

### 3.2.1 Data Cleaning

Standardize variable names, retain relevant fields, and ensure chronological ordering.

### 3.2.2 Frequency Alignment

Convert housing data to monthly frequency via forward filling to match other series.

### 3.2.3 Temporal Standardization

Transform all date variables into a common monthly timestamp format.

### 3.2.4 Data Integration

Merge datasets on the time dimension and remove missing observations to obtain a consistent dataset.

## 3.3 Final Dataset
 - Stored in : data/processed/final_dataset.csv
 - Generated through the data processing pipeline

## 4. Methodology and Key Findings
### 4.1 Stationary Testing (ADF Test)
Macroeconomic variables inherently follow long-term trends. Augmented Dickey-Fuller(ADF) tests on raw levels confirmed non-stationary (P>0.05). First-order differencing was applied to remove trends and stabilize the data, achieving full stationary across all series.

### 4.2 VAR Model 
A Vector Autoregression (VAR) Model was fitted to the stationary, differenced data.
- Lag Order Selection: Based on the minimum Akaike Information Criterion (AIC) and Final Prediction Error (FPE), an optimal lag of 4 quarters was selected.

### 4.3 Empirical Results
- Real Estate has Massive Momentum: Property prices in Poland are highly self-predictive. If the housing market performed strongly in previous quarters, that built-in momentum carries directly over into current property values with high statistical confidence (p=0.014).

- Inflation Hits on a One-Year Fuse: We found a clear, delayed relationship with consumer prices. A spike in inflation takes about a year before it fully pushes property values upward (0.24).This lag reflects the time it takes for broad inflation to raise material construction costs and shift public market expectations.

- Short-Term Interest Rate Insulation: Interestingly, when looking at quarter-to-quarter adjustments within this specific model, short-term fluctuations in interest rates did not show an immediate, overwhelming impact on property prices, indicating that structural market momentum and inflation pass-throughs act as the dominant drivers.


## 5. How to Run
### Run using Python
1.Run the data processing pipeline:
``` bash
python src/pipeline.py

```
2.Run VAR_model.py:
```bash
python src/VAR_model.py
```

## 6. Reproducibility with Docker
The project can be reproduced using docker:
1. Build the Docker image: 
```bash
docker build -t macro-project .
```
2. Run the project

```bash
docker run macro-project 
```

## 7. Tools and Libraries
- Python 3.11
- pandas
- numpy
- matplotlib
- statsmodels
- docker

## 8. Final Conclusion
- This study examined the relationship between inflation, interest rates, and housing prices in Poland using VAR.
- The results show that while the VAR model captures dynamic interactions between the variables, the impulse response analysis indicates how shocks propagate through the system over time.
- The Granger Causality test suggests that inflation plays an important role in predicting housing prices, while the relationship between inflation and interest rates appears to be bidirectional but stronger from interest rates to inflation.
- Overall, the findings indicate that macroeconomic relationships are complex and are likely influenced by broader structural and external factors beyond the scope of this model.






