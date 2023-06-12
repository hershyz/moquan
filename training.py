# imports
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.optimizers import Adam

# get dataframe
df = pd.read_csv('stock_dataset.csv')

# input = first 5 values of all stocks, output = 6th value of all stocks
df.drop('Date', axis=1, inplace=True)
X = []
y = []

df_as_np = df.to_numpy()
left = 0
for right in range(left + 5, len(df_as_np)):
    X_row = []
    for pointer in range(left, right):
        X_row.append(df_as_np[pointer])
    X.append(X_row)
    y.append(df_as_np[right])
    left += 1

X = np.array(X)
y = np.array(y)

# construct the model
model = Sequential()
model.add(LSTM(64, input_shape=(5, 10), return_sequences=True))
model.add(LSTM(32))
model.add(Dense(10))

model.compile(optimizer='adam', loss='mse')

# train the model
model.fit(X, y, epochs=1000)

# finally, save model
model.save('stock_model.h5')