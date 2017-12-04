import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

df = pd.read_csv('data.csv')
print(df.head(5), end='\n')
print(df.dtypes, end='\n')
df['ds'] = pd.DatetimeIndex(df['ds'])
print(df.dtypes, end='\n')

ax = df.set_index('ds').plot(figsize=(12,8))
ax.set_ylabel('Temperature recordings')
ax.set_xlabel('DateTime')
# plt.show()

my_model = Prophet(interval_width=0.95)
my_model.fit(df)

future_dates = my_model.make_future_dataframe(periods=1, freq='D')
future_dates.tail()
# print(future_dates)
forecast = my_model.predict(future_dates)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

my_model.plot(forecast, uncertainty=True)

my_model.plot_components(forecast)
plt.show()