import numpy as np
import pandas as pd
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('my_model')

# Take input from the user
input_data = input("Enter the stock prices for the last 30 days separated by commas: ")
input_data = input_data.split(',')
input_data = [float(x) for x in input_data]

# Preprocess the input
input_data = np.array(input_data).reshape(1, 30, 1)

# Predict the stock price
predicted_price = model.predict(input_data)

# Display the predicted stock price
print("The predicted stock price for tomorrow is: $", predicted_price[0][0])
