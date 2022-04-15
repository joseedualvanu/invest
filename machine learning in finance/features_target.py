import pandas as pd
import talib

bitcoin_data = pd.read_csv('bitcoin_V1.csv', index_col='Date', parse_dates=True)

feature_names = ['5d_close_pct']  # a list of the feature names for later

# Create moving averages and rsi for timeperiods of 14, 30, 50, and 200
for n in [14, 30, 50, 200]:

    # Create the moving average indicator and divide by Adj_Close
    bitcoin_data['ma' + str(n)] = talib.SMA(bitcoin_data['Adj_Close'].values,
                              timeperiod=n) / bitcoin_data['Adj_Close']
    # Create the RSI indicator+
    bitcoin_data['rsi' + str(n)] = talib.RSI(bitcoin_data['Adj_Close'].values, timeperiod=n)
    
    # Add rsi and moving average to the feature name list
    feature_names = feature_names + ['ma' + str(n), 'rsi' + str(n)]
    
print(feature_names)