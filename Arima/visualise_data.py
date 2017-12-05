# line plot of time series
from pandas import Series
from matplotlib import pyplot
# load dataset
series = Series.from_csv('../Prophet/data.csv')
# display first few rows
print(series.head(20))
# line plot of dataset
series.plot()
pyplot.show()