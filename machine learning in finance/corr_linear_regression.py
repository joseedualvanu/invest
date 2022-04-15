import pandas as pd

# Primer parte: correlacion
bitcoin_data_df = pd.read_csv('bitcoin_V1.csv', index_col='Date', parse_dates=True)

feature_names_list = ['5d_close_pct', 'ma14', 'rsi14', 'ma30', 'rsi30', 'ma50', 'rsi50', 'ma200', 'rsi200']
feature_names_list = ['Adj_Close', 'ma14', 'rsi14', 'ma30', 'rsi30', 'ma50', 'rsi50']
feature_names_list = ['Open', 'High', 'Low']

feature_names_df = pd.DataFrame(feature_names_list)

# Drop all na values
bitcoin_data_df = bitcoin_data_df.dropna()

# Create features and targets
# use feature_names for features; '5d_close_future_pct' for targets
features = bitcoin_data_df[feature_names_df]
targets = bitcoin_data_df['Adj_Close']

# Create DataFrame from target column and feature columns
feature_and_target_cols = ['Adj_Close'] + feature_names_df
feat_targ_df = bitcoin_data_df[feature_and_target_cols]

# # Calculate correlation matrix
corr = feat_targ_df.corr()
print(corr)

# Segunda parte: regresion lineal
"""
import statsmodels.api as sm

# Add a constant to the features
linear_features = sm.add_constant(bitcoin_data_df)

# Create a size for the training set that is 85% of the total number of samples
train_size = int(0.85 * targets.shape[0])
train_features = linear_features[:train_size]
train_targets = targets[:train_size]
test_features = linear_features[train_size:]
test_targets = targets[train_size:]
print(linear_features.shape, train_features.shape, test_features.shape)

"""