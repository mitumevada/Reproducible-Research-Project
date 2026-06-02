# Poland Macroeconomic Time Series Analysis

# 1. Research Background

The relationship between macroeconomic conditions and housing market dynamics has been widely studied in the economic literature. In particular, a large body of research highlights the role of monetary policy variables, such as interest rates, in shaping housing price movements. Lower interest rates tend to reduce borrowing costs and stimulate housing demand, while higher rates may exert downward pressure on housing prices.

In addition to interest rates, inflation is also considered an important macroeconomic factor affecting housing markets. As a key indicator of overall price dynamics, inflation can influence both real asset values and investment behavior. Prior studies suggest that housing prices may act as a hedge against inflation, although the strength and timing of this relationship remain subject to empirical investigation.

While these relationships are well documented, the interactions between macroeconomic variables and housing prices are inherently dynamic and may involve lagged effects. As a result, time series approaches have been widely used to capture such dynamics and to analyze how shocks to one variable propagate through the system over time.

Building on this literature, this project focuses on the Polish economy and examines the joint behavior of housing prices, interest rates, and inflation within a time series framework. By doing so, we aim to provide empirical evidence on how these key variables interact over time and whether their relationships exhibit systematic patterns in a country-specific context.


# 2. Research Objective

The objective of this project is to examine how housing prices in Poland are related to interest rates and inflation over time. Using quarterly data from the first quarter of 2010 to the fourth quarter of 2025, we investigate the dynamic interactions among these variables within a macroeconomic framework.

Specifically, we aim to investigate whether changes in interest rates and inflation are associated with subsequent movements in housing prices, and whether these effects occur immediately or with a time lag.


# 3. Project Structure

```text
Reproducible-Research-Project/
│
├── data/
│   ├── raw/                     # Raw macroeconomic data
│   │   ├── housing_price.csv
│   │   ├── inflation.csv
│   │   └── interest_rate.csv
│   │
│   └── processed/               # Cleaned and merged dataset
│       └── final_dataset.csv
│
├── src/
│   ├── pipeline.py              # Data cleaning and preprocessing pipeline
│   └── VAR_model.py             # VAR, IRF, and Granger causality analysis
│
├── Dockerfile                   # Docker configuration for reproducibility
├── Macroeconomic TSA.ipynb      # Jupyter Notebook version of the analysis
└── README.md                    # Project documentation
```

# 4. Data

Since inflation and interest rates are originally reported at a monthly frequency, while the housing price index is available at a quarterly frequency, all variables are converted to a common quarterly frequency to ensure temporal consistency and improve the reliability of the time-series analysis.

## 4.1 Data Sources

 - Housing price: Eurostat
 - Interest rate: Eurostat
 - Inflation: OECD Data Explorer

## 4.2 Data Processing

### 4.2.1 Data Cleaning

Standardize variable names, retain relevant fields, and ensure chronological ordering.

### 4.2.2 Frequency Alignment

Convert housing data to monthly frequency via forward filling to match other series.

### 4.2.3 Temporal Standardization

Transform all date variables into a common monthly timestamp format.

### 4.2.4 Data Integration

Merge datasets on the time dimension and remove missing observations to obtain a consistent dataset.

## 4.3 Final Dataset
 - Stored in : data/processed/final_dataset.csv
 - Generated through the data processing pipeline

# 5. Methodology

This study follows a standard time-series econometric framework to investigate the dynamic relationships among inflation, interest rates, and housing prices in Poland.

## 5.1 Data Collection and Preparation

Three macroeconomic variables were collected and merged into a unified quarterly dataset:

* Inflation Rate
* Interest Rate
* Housing Price Index

Since housing prices are measured as an index, the Housing Price Index was transformed using the natural logarithm to stabilize variance and improve interpretability.

## 5.2 Exploratory Data Analysis

Time-series plots were generated to examine the historical behavior of each variable and identify potential trends, cycles, and structural changes. The visual inspection provided preliminary evidence of possible interactions among inflation, interest rates, and housing prices.

## 5.3 Stationarity Testing

Before estimating the VAR model, stationarity was assessed using the Augmented Dickey-Fuller (ADF) test.

The null hypothesis of the ADF test states that a series contains a unit root and is therefore non-stationary. Since non-stationary variables may lead to spurious regression results, stationarity is required for reliable VAR estimation.

## 5.4 Data Transformation

The initial ADF results indicated that the variables were non-stationary. Therefore, first-order differencing was applied to all series to remove trends and stabilize their statistical properties.

After differencing, the ADF test was performed again to confirm stationarity before proceeding with model estimation.

## 5.5 Vector Autoregression (VAR) Model

A Vector Autoregression (VAR) model was employed to capture the dynamic interactions among inflation, interest rates, and housing prices.

The VAR framework allows each variable to be explained by:

* Its own lagged values
* The lagged values of the other variables in the system

The optimal lag length was selected using standard information criteria, including:

* Akaike Information Criterion (AIC)
* Bayesian Information Criterion (BIC)
* Final Prediction Error (FPE)
* Hannan-Quinn Information Criterion (HQIC)

## 5.6 Impulse Response Analysis

Impulse Response Functions (IRFs) were estimated to examine how shocks to one variable affect the others over time.

The IRFs trace the direction, magnitude, and persistence of responses following a one-time innovation in inflation, interest rates, or housing prices, providing insight into the transmission mechanisms within the macroeconomic system.

## 5.7 Granger Causality Testing

Granger causality tests were conducted using the optimal lag length selected by the VAR model.

The purpose of these tests is to determine whether past values of one variable contain statistically significant information for predicting future values of another variable.

The null hypothesis states that one variable does not Granger-cause another variable. Rejection of the null hypothesis indicates predictive causality within the system.

## 5.8 Reproducibility

The entire workflow, including data preprocessing, VAR estimation, impulse response analysis, and Granger causality testing, is fully reproducible through the provided Python scripts and Docker environment.

Running the Docker container automatically executes:

1. `src/pipeline.py`
2. `src/VAR_model.py`

allowing the complete analysis to be reproduced from the raw data to the final results.


# 6.Results
## 6.1 Stationarity Analysis

The Augmented Dickey-Fuller (ADF) tests indicated that the original series were non-stationary. Therefore, first-order differencing was applied to inflation, interest rates, and log housing prices. The differenced series passed the stationarity tests and were subsequently used for VAR estimation.

## 6.2 VAR Model Results

The optimal lag length selected by the Akaike Information Criterion (AIC) was four lags. The estimated VAR(4) model revealed several important dynamic relationships among the variables.

For the housing price equation, the first lag of housing prices was statistically significant (coefficient = 0.356, p = 0.014), indicating strong persistence in housing price dynamics. In addition, the fourth lag of inflation was positive and statistically significant (coefficient = 0.0043, p = 0.024), suggesting that inflation exerts a delayed effect on housing price growth.

Interest-rate coefficients were generally not statistically significant in the housing-price equation, indicating that direct short-run effects of interest rates on housing prices are relatively weak within the sample period.

## 6.3 Impulse Response Analysis

Impulse Response Functions (IRFs) were estimated over a 12-quarter horizon to examine the dynamic transmission of macroeconomic shocks.

The results show that:

A positive inflation shock generates a delayed but positive response in housing prices. Housing prices initially respond weakly but become positive after approximately four quarters and remain above zero for most of the forecast horizon.
A positive interest-rate shock leads to a temporary decline in housing price growth. The strongest negative response occurs around the fourth to fifth quarter before gradually converging toward zero.
Housing prices exhibit strong persistence in response to their own shocks, with positive effects remaining throughout most of the forecast horizon.
All impulse responses gradually converge back toward zero, indicating that the VAR system is dynamically stable.

## 6.4 Granger Causality Results

Using a four-lag specification, the Granger causality tests produced the following results:

Cause	Target	Lag	p-value
Inflation	Housing Price	4	0.0378
Interest Rate	Housing Price	4	0.3915
Inflation	Interest Rate	4	0.0614
Interest Rate	Inflation	4	0.0162

The results suggest that:

Inflation Granger-causes housing prices at the 5% significance level.
Interest rates do not Granger-cause housing prices.
Interest rates Granger-cause inflation.
Evidence that inflation Granger-causes interest rates is weak and only marginally significant at the 10% level.

# 7.Conclusion

This study investigated the dynamic relationships among inflation, interest rates, and housing prices in Poland using a Vector Autoregression (VAR) framework.

The empirical findings indicate that inflation plays a significant role in explaining housing price movements. Both the VAR estimates and Granger causality tests suggest that inflation affects housing prices with a lag rather than immediately. Specifically, the fourth lag of inflation was statistically significant in the housing-price equation, while the Granger causality test confirmed that inflation contains predictive information for future housing price changes.

Interest rates exhibited a weaker direct relationship with housing prices. Although the interest-rate coefficients in the VAR model were generally insignificant and no Granger causality from interest rates to housing prices was detected, the impulse response analysis showed that monetary policy shocks can still exert temporary downward pressure on housing price growth through dynamic transmission channels.

The impulse response analysis further revealed that housing prices are highly persistent and respond strongly to their own shocks. Moreover, all responses gradually converged toward zero over the forecast horizon, indicating that the estimated VAR system is stable and that macroeconomic shocks have temporary rather than permanent effects.

Overall, the results suggest that inflation is a more important driver of housing-price dynamics than interest rates in the sample period examined. The findings highlight the importance of inflationary pressures and delayed transmission mechanisms when analyzing developments in the Polish housing market.


# 8. Reproducibility with Docker
The project can be reproduced using docker:

1. Build the Docker image: 
```bash
docker build -t macro-project .
```
2. Run the project

```bash
docker run macro-project 
```

# 9. Tools and Libraries
- Python 3.11
- pandas
- numpy
- matplotlib
- statsmodels
- docker

<<<<<<< HEAD
=======

## 10. AI Disclosure Statement

Artificial intelligence tools were used in three ways during this project: (1) for language refinement to enhance the clarity of the text, (2) to assist in drawing conclusions and synthesizing insights from our results, and (3) to identify and apply fixes to the code base.





>>>>>>> 22a39f0c788df844836dec71be9ed81540424ba9

