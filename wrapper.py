# imports
from tensorflow.keras.models import load_model
import numpy as np

# wrapper class
class Wrapper:

    def __init__(self):
        self.model = load_model('stock_model.h5')
        self.tickers = ['ORCL','AMZN','INTC','MSFT','AMD','NVDA','META','GOOG','AVGO','AAPL']

    # prediction function -- X = 10 features, 5 timestamps
    def predict(self, X):
        predictions = self.model.predict(X)[0]
        for i in range(len(predictions)): print(self.tickers[i] + ': ' + str(predictions[i]))