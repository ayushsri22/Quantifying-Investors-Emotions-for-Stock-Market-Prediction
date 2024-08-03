# -*- coding: utf-8 -*-
"""arch_garch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1agGNq8P3097f0xAn40Y7ynEfOJ4lgzmD
"""

pip install arch

pip install statsmodels

pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from arch import arch_model

# Load and prepare the data
file_path = '/content/demo_us.xlsx'  # Update with your actual file path
data = pd.read_excel(file_path)

# Selecting relevant columns
returns = data['actual_return']  # This should be your returns column
valence = data[['valence']]  # Ensure this is a DataFrame, not a Series

# Fitting a GARCH(1,1) model with valence as an exogenous variable
model = arch_model(returns, vol='Garch', p=1, q=1, mean='Constant', x=valence)
results = model.fit()

# Extracting the conditional volatility from the model
conditional_volatility = results.conditional_volatility

# Plotting the conditional volatility and valence
fig, ax1 = plt.subplots(figsize=(14, 7))

ax1.set_xlabel('Time')
ax1.set_ylabel('Conditional Volatility', color='tab:blue')
ax1.plot(conditional_volatility, color='tab:blue', label='Conditional Volatility')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()  # Instantiate a second axes that shares the same x-axis
ax2.set_ylabel('Valence', color='tab:orange')  # We already handled the x-label with ax1
ax2.plot(valence, color='tab:orange', label='Valence', alpha=0.6)
ax2.tick_params(axis='y', labelcolor='tab:orange')

fig.tight_layout()  # Otherwise the right y-label is slightly clipped
plt.title('Conditional Volatility and Valence Over Time')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from arch import arch_model

# Load and prepare the data
file_path = '/content/demo_us.xlsx'  # Update with your actual file path
data = pd.read_excel(file_path)

# Selecting relevant columns
returns = data['actual_return']  # This should be your returns column
valence = data[['valence']]  # Ensure this is a DataFrame, not a Series

# Fitting a GARCH(1,1) model with valence as an exogenous variable
model = arch_model(returns, vol='Garch', p=1, q=1, mean='Constant', x=valence)
results = model.fit()

predicted_volatility = results.conditional_volatility

# Calculating the actual (realized) volatility using a rolling window
actual_volatility = returns.rolling(window=20).std()


# Plotting actual vs predicted volatility
plt.figure(figsize=(14, 7))
plt.plot(predicted_volatility, label='Predicted Volatility (GARCH)')
plt.plot(actual_volatility, label='Actual Volatility (Rolling Std Dev)', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Volatility')
plt.title('Comparison of Predicted and Actual Volatility')
plt.legend()
plt.show()

# Align the lengths of predicted and actual volatility for correlation calculation
aligned_data = pd.DataFrame({
    'predicted_volatility': predicted_volatility,
    'actual_volatility': actual_volatility
}).dropna()

# Calculate the correlation between actual and predicted volatility
correlation = aligned_data['predicted_volatility'].corr(aligned_data['actual_volatility'])
print(f"Correlation between actual and predicted volatility: {correlation}")

