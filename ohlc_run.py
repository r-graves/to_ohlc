import pandas as pd

file_path = "./BTC_crypto_sample/BTC_1min_sample.txt"
data = pd.read_csv(file_path, names=['date_time', 'LTP', 'LQP', 'Price2', 'Exchange Code'], index_col=0)
#data.index(pd.to_datetime(data.index, format='%Y-%m-%d %H:%M:%S'))
data.index = pd.to_datetime(data.index, format='%Y-%m-%d %H:%M:%S')

print(data.head())

# Resample LTP column to 15 mins bars using resample function from pandas
resample_LTP = data['LTP'].resample('15Min').ohlc(_method='ohlc')

# Print the last 5 rows of resampled LTP
print("resampled file") 
print(resample_LTP.head())