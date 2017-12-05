import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')



# Python
df = pd.read_csv('data.csv')
print(df.head(5), end='\n')
print(df.dtypes, end='\n')
# change first column to datatime
df['ds'] = pd.DatetimeIndex(df['ds'])
print(df.dtypes, end='\n')

ax = df.set_index('ds').plot(figsize=(12,8))
ax.set_ylabel('Temperature recordings')
ax.set_xlabel('DateTime')

model = Prophet(changepoint_prior_scale=0.01).fit(df)
future_times = model.make_future_dataframe(periods=300, freq='5min', include_history=False)
forecast = model.predict(future_times)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

model.plot(forecast)
model.plot_components(forecast)
plt.show()