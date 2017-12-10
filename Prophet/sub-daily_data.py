import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# csv data read needs to be dynamic
data_frame = pd.read_csv('data.csv')
# change first column to datetime
data_frame['ds'] = pd.DatetimeIndex(data_frame['ds'])

# make a plot of the historical data
# threshold needs to be extracted from user preferences
threshold = 5.0
ax = data_frame.set_index('ds').plot(figsize=(12, 8))

# Provide a way to use these graphs on the website
# add a threshold line to historical data vis
ax.axhline(y=threshold, color='r', linestyle='-')
ax.set_ylabel('Temperature recordings')
ax.set_xlabel('DateTime')

model = Prophet(changepoint_prior_scale=0.01).fit(data_frame)
# produce 300 future timestamps in 5 minute increments
future_times = model.make_future_dataframe(periods=300, freq='5min', include_history=False)
# use the model to predict temps for these times
forecast = model.predict(future_times)

# predictions stored in a csv file and overwritten each time? Or update a database with predictions
# Write the date and temp to file
forecast.to_csv('Predict_Output', columns=('ds', 'yhat'), index_label=False, index=False, header=('Timestamp', 'Temps'), float_format='%.2f')
# display the last 5 observations and their predicted temps with upper and lower boundaries
print()
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# plot the forecast results
model.plot(forecast, uncertainty=True)
# plot the overall and daily trend
model.plot_components(forecast)

plt.show()
