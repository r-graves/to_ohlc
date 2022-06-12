import pandas as pd

file_path = "./BTC_crypto_sample/BTC_1min_sample.txt"
data = pd.read_csv(file_path, names=['date_time', 'LTP', 'LTQ', 'Price2', 'Exchange Code'], index_col=0)
#data.index(pd.to_datetime(data.index, format='%Y-%m-%d %H:%M:%S'))
data.index = pd.to_datetime(data.index, format='%Y-%m-%d %H:%M:%S')

print(data.head())

# Resample LTP column to 15 mins bars using resample function from pandas
resample_LTP = data['LTP'].resample('15Min').ohlc(_method='ohlc')

# Resample LTQ column to 15 mins bars using resample function from pandas
resample_LTQ = data['LTQ'].resample('15Min').sum()

# Print the last 5 rows of resampled LTP
print("resampled file") 
print(resample_LTP.head())

# Concatenate resampled data
resample_data = pd.concat([resample_LTP, resample_LTQ], axis=1,)

# Print the last 5 rows
print("Resampled header")
print(resample_data.head())