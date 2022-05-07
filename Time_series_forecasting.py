# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import numpy as np
import sklearn as sk
from math import sqrt
from sklearn.metrics import mean_squared_error as MSE
from sklearn import linear_model
from bokeh.io import output_notebook, show, reset_output, output_file, save
from bokeh.plotting import figure
from bokeh.models import BoxAnnotation
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool


cloud_covering = pd.read_csv("ninja_weather_country_CA.AB_merra-2_population_weighted.csv",parse_dates=['time'],infer_datetime_format=True,low_memory=False)

prediction = cloud_covering[["time","cloud_cover"]]
print(prediction.head())

mask = (prediction['time'] >= '2017-01-01') & (prediction['time'] <= '2019-12-31')
prediction = prediction.loc[mask]
# Reset the index
prediction.set_index("time", inplace=True)

print(prediction.head())

result_add = seasonal_decompose(prediction.cloud_cover,model="additive",extrapolate_trend="freq")

plt.rcParams.update({'figure.figsize': (10,10)})
result_add.plot().suptitle('Additive Decomposition', fontsize=22)
plt.show()

predicted_df = prediction["cloud_cover"].to_frame().shift(1).rename(columns = {"cloud_cover": "cc_pred" })
actual_df = prediction["cloud_cover"].to_frame().rename(columns = {"cloud_cover": "cc_actual" })

one_step_df = pd.concat([actual_df,predicted_df],axis=1)

one_step_df = one_step_df[1:]
one_step_df.head(10)

temp_pred_err = MSE(one_step_df.cc_actual, one_step_df.cc_pred, squared=False)
print("The RMSE is",temp_pred_err)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
