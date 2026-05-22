# Poland Macroeconomic Time Series Analysis

## Objective
This project prepares a clean and consistent dataset for analyzing the relationship between key macroeconomic variables in Poland, including inflation, interest rates, and housing prices.

The focus of this part is to ensure that the data is properly cleaned, aligned, and ready for further analysis.


## Data Processing

The following steps were performed:

- Collected data on inflation, interest rates, and housing prices
- Cleaned and formatted each dataset
- Converted all variables to a common monthly frequency
- Aligned time series across datasets
- Merged datasets into a single structured dataset


## Output

The final processed dataset is available at:

data/processed/final_dataset.csv

This dataset is ready to be used for further analysis and visualization.


## How to Run
### Run with Python

``` bash
python src/pipeline.py
```

### Run with Docker

1. Build the Docker image
``` bash
docker build -t poland-project .
```
2. Run the container (with volume mapping)
``` bash
docker run -v "${PWD}/data/processed:/app/data/processed" poland-project
```

This ensures that the generated dataset is saved to your local machine.
