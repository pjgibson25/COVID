import numpy as np
import pandas as pd
import datetime

# Import Original John's Hopkins Data
data =  pd.read_csv('../JHU dataset/time_series_19-covid-Confirmed.csv')

# Create filter for only US cases
us_data = data[(data['Country/Region']=='US')]
# Create filter for only counties
us_data_np = np.array(us_data['Province/State'])
cond = [',' in option for option in us_data_np]
county_data_raw = us_data[cond]
# Create filter for dates before March 9th.  All data after is empty
county_data = county_data_raw.drop(columns = county_data_raw.columns[52:])

# Send to file
county_data.to_csv('../JHU dataset/JHU_filtered_timeseries.csv', index=False)

