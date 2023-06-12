# moquan
TensorFlow LSTM Time Series Algorithm for Stock Market Forecasting

[This inference model](https://github.com/hershyz/moquan/releases/tag/v1) was trained to forecast 10 stocks on data from May 18th, 2012 to June 9th, 2023:
- AAPL
- AMD
- AMZN
- AVGO
- GOOG
- INTC
- META
- MSFT
- NVDA
- ORCL

**Step 1:**  
Use the [build_dataset script](https://github.com/hershyz/moquan/blob/main/build_dataset.py) to convert individual ticker CSV data from [Yahoo Finance's Historical Data tool](https://finance.yahoo.com/quote/MSFT/history?period1=511056000&period2=1686528000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true) to a [complete training dataset](https://github.com/hershyz/moquan/blob/main/stock_dataset.csv).

**Step 2:**  
Run the [TensorFlow training algorithm](https://github.com/hershyz/moquan/blob/main/training.py), updating the ticker array and input shape as needed. Currently, the input shape is ```(5, 10)``` -- (10 input features and 5 previous time series point per prediction).    

```
Dependencies (pip):
- tensorflow
- numpy
- pandas
- matplotlib
```

**Step 3:**  
Update the ticker array in the [model wrapper class](https://github.com/hershyz/moquan/blob/main/wrapper.py) as needed. Then, [test predictions](https://github.com/hershyz/moquan/blob/main/test_predictions.py).
