import pandas as pd
import matplotlib.pyplot  as plt

bitcoin_data = pd.read_csv('bitcoin_V1.csv', index_col='Date', parse_dates=True)

# print(bitcoin_data.head())  # examine the SPY DataFrame

# Plot the Adj_Close columns for bitcoins
bitcoin_data["Adj_Close"].plot(label='Bitcoin', legend=True)
plt.show()  # show the plot
plt.clf()  # clear the plot space
# plt.savefig("fig1.png")


# Histogram of the daily price change percent of Adj_Close for bitcoins
bitcoin_data['Adj_Close'].pct_change(10).plot.hist(bins=50)
plt.xlabel('adjusted close 1-day percent change')
plt.show()
# plt.savefig("fig2.png")

# Create 5-day % changes of Adj_Close for the current day, and 5 days in the future
bitcoin_data['5d_future_close'] = bitcoin_data['Adj_Close'].shift(-5)
bitcoin_data['5d_close_future_pct'] = bitcoin_data['5d_future_close'].pct_change(5)
bitcoin_data['5d_close_pct'] = bitcoin_data['Adj_Close'].pct_change(5)

# Calculate the correlation matrix between the 5d close pecentage changes (current and future)
corr = bitcoin_data[['5d_close_pct', '5d_close_future_pct']].corr()
print(corr)

# Scatter the current 5-day percent change vs the future 5-day percent change
plt.scatter(bitcoin_data['5d_close_pct'], bitcoin_data["5d_close_future_pct"])
plt.show()
# plt.savefig("fig3.png")