# moquan
TensorFlow LSTM Time Series Algorithm for Stock Market Forecasting

[This inference model](https://github.com/hershyz/moquan/releases/tag/v1) was trained to forecast the following 10 stocks on data from May 18th, 2012 to June 9th, 2023:
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
Run the [TensorFlow training algorithm](https://github.com/hershyz/moquan/blob/main/training.py), updating the ticker array and input shape as needed. By default, the input shape is ```(5, 10)``` -- (10 input features and 5 previous time series point per prediction).    

```
Dependencies (pip):
- tensorflow
- numpy
- pandas
- matplotlib
```

**Step 3:**  
Update the ticker array in the [model wrapper class](https://github.com/hershyz/moquan/blob/main/wrapper.py) as needed. Then, [test predictions](https://github.com/hershyz/moquan/blob/main/test_predictions.py).  

<br>

### Training Results ([view in notebook](https://deepnote.com/workspace/hershey-081c52c1-1c94-4f55-bc37-630a0fb3fcd3/project/moquan-bca18ada-d83c-41f4-9d91-200d3dfbef3b/notebook/Training-a2269410652c458c9eff766cbdb2ffb1)):
![AAPL](https://raw.githubusercontent.com/hershyz/moquan/main/matplotlib/AAPL.png)
![AMD](https://raw.githubusercontent.com/hershyz/moquan/main/matplotlib/AMD.png)
![AMZN](https://raw.githubusercontent.com/hershyz/moquan/main/matplotlib/AMZN.png)
![AVGO](https://raw.githubusercontent.com/hershyz/moquan/main/matplotlib/AVGO.png)
![GOOG](https://raw.githubusercontent.com/hershyz/moquan/main/matplotlib/GOOG.png)
![INTC](https://raw.githubusercontent.com/hershyz/moquan/main/matplotlib/INTC.png)
![META](https://raw.githubusercontent.com/hershyz/moquan/main/matplotlib/META.png)
![MSFT](https://raw.githubusercontent.com/hershyz/moquan/main/matplotlib/MSFT.png)
![NVDA](https://raw.githubusercontent.com/hershyz/moquan/main/matplotlib/NVDA.png)
![ORCl](https://raw.githubusercontent.com/hershyz/moquan/main/matplotlib/ORCL.png)
