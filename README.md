# Poland Macroeconomic Time Series Analysis

# 1. Research Backgroud

The relationship between macroeconomic conditions and housing market dynamics has been widely studied in the economic literature. In particular, a large body of research highlights the role of monetary policy variables, such as interest rates, in shaping housing price movements. Lower interest rates tend to reduce borrowing costs and stimulate housing demand, while higher rates may exert downward pressure on housing prices.

In addition to interest rates, inflation is also considered an important macroeconomic factor affecting housing markets. As a key indicator of overall price dynamics, inflation can influence both real asset values and investment behavior. Prior studies suggest that housing prices may act as a hedge against inflation, although the strength and timing of this relationship remain subject to empirical investigation.

While these relationships are well documented, the interactions between macroeconomic variables and housing prices are inherently dynamic and may involve lagged effects. As a result, time series approaches have been widely used to capture such dynamics and to analyze how shocks to one variable propagate through the system over time.

Building on this literature, this project focuses on the Polish economy and examines the joint behavior of housing prices, interest rates, and inflation within a time series framework. By doing so, we aim to provide empirical evidence on how these key variables interact over time and whether their relationships exhibit systematic patterns in a country-specific context.


# 2. Research Objective

The objective of this project is to examine how housing prices in Poland are related to interest rates and inflation over time.

Specifically, we aim to investigate whether changes in interest rates and inflation are associated with subsequent movements in housing prices, and whether these effects occur immediately or with a time lag.


# 3. Data

This script constructs a consistent monthly dataset by processing raw data on inflation, interest rates, and housing prices, ensuring comparability across variables for subsequent analysis.

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

## 3.4 How to run

Run the data processing pipeline:
``` bash
python src/pipeline.py
```





