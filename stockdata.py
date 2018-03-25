import pandas as pd
import numpy as np
import pandas_datareader.data as web
import quandl
from datetime import datetime, timedelta, date
quandl.ApiConfig.api_key= "Insert your key here"


newlist = pd.read_csv('constituents.csv')
newerlist = pd.Series(newlist['Symbol'])
newestlist = newerlist.tolist()


#Function that returns a list of tickers with the WIKI attachement
def create_tickers(n):
    stock_tickers = []
    wikilist = []
    for i in range(n):
        wikilist.append('WIKI/')
    for i in range(n):
        name = wikilist[i]+newestlist[i]
        stock_tickers.append(name)
    return stock_tickers

list = create_tickers(499)

#Function that creates a list of adj.close tickers such that we only get that column
def create_close_tickers(tickerlist, n):
    adjclose=[]
    AdjClose_tickers=[]
    for i in range(n):
        adjclose.append('.11')
    for i in range(n):
        name = tickerlist[i] + adjclose[i]
        AdjClose_tickers.append(name)
    return AdjClose_tickers

tickerlist = create_close_tickers(list, 499)

#Function that returns the adj close prices for the tickerlist
def get_adjclose(tickerlist, datenow, begindate, csvname):
    data = quandl.get(tickerlist, start_date=begindate, end_date=Date_now, order='asc')
    #Function that takes away the wiki/ portion of the name
    def rename_cols(s):
        if s == 'Date':
            return 'Date'
        else:
            return(s.split(' ')[0]).split('/')[1]
    data = data.rename(rename_cols, axis=1)

    data.to_csv(csvname)

#Function call for 30 days
now = datetime.now()
Thirty_now = now - timedelta(30)
Thirty_now = Thirty_now.strftime('%Y-%m-%d')
#Datetime now
Date_now = now.strftime('%Y-%m-%d')
csvname = '30DayStocks.csv'

get_adjclose(tickerlist, Date_now, Thirty_now, csvname)

#Function call for 360 days
oneyear = now - timedelta(360)
oneyear = oneyear.strftime('%Y-%m-%d')
csvname1 = 'OneyearStocks.csv'

get_adjclose(tickerlist, Date_now, oneyear, csvname1)

#Function call for year to date
YTD = date(date.today().year, 1, 1)
csvname2 = 'YTDStocks.csv'

get_adjclose(tickerlist, Date_now, YTD, csvname2)
