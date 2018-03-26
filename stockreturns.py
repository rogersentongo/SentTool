import pandas as pd
import numpy as np
import pandas_datareader.data as web
from datetime import datetime, timedelta, date


#We read the csv data into three dataframes
thirty_day = pd.read_csv('csv/30DayStocks.csv', index_col=0)
one_year = pd.read_csv('csv/OneyearStocks.csv', index_col=0)
ytd = pd.read_csv('csv/YTDStocks.csv', index_col=0)

#Function that creates final returns dataframe
def final_returns(dataframe):
    index_no = len(dataframe.index)-1
    returns = dataframe.pct_change(periods=index_no)*100
    final_returns = pd.DataFrame(returns.iloc[index_no])
    final_returns = final_returns.reset_index()
    final_returns = final_returns.rename(columns={'index': 'Ticker'})
    return final_returns

def return_final(name):
    dataframe = final_returns(name)
    date_value = dataframe.columns.values
    date_value = date_value[1]
    dataframe = dataframe.sort_values(by=date_value, ascending=False)
    dataframe = dataframe.reset_index(drop=True)
    return dataframe

oneyear_returns = return_final(one_year)
ytd_returns = return_final(ytd)



thirty_returns = final_returns(thirty_day)
date_value = thirty_returns.columns.values
date_value = date_value[1]
date_value
thirty_returns1 = thirty_returns.sort_values(by=date_value, ascending=False)

thirty_returns2 = thirty_returns.sort_values(by=date_value, ascending=True)

Top10 = thirty_returns1.head(10).reset_index(drop=True)
Bottom10= thirty_returns2.head(10).reset_index(drop=True)

#Function that rounds the return column
def colround(name):
    colname = name.columns[1]
    name = name.round({colname: 2})
    return name

ytd_returns = colround(ytd_returns)
oneyear_returns = colround(oneyear_returns)
Top10 = colround(Top10)
Bottom10 = colround(Bottom10)

print(Top10)
print(Bottom10)


ytd_returns.to_csv('csv/ytd_returns.csv')
oneyear_returns.to_csv('csv/oneyear_returns.csv')
Top10.to_csv('csv/Top10.csv')
Bottom10.to_csv('csv/Bottom10.csv')
