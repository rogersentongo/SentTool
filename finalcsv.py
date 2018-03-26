import pandas as pd
import numpy as np
import pandas_datareader.data as web
import quandl
from datetime import datetime, timedelta

dp = pd.read_csv('csv/ytd_returns.csv', index_col=0)
const = pd.read_csv('csv/constituents.csv')
dp['Name'] = None
dp['Sector'] = None
dp = dp.copy()

length = len(dp.index)

for index_no in range(length):
    name = dp['Ticker'][index_no]
    row = const[const['Symbol'].str.contains(name, case=True)]
    name = row['Name'].tolist()
    sector = row['Sector'].tolist()

    name = name[0]
    sector=sector[0]
    dp['Name'][index_no] = name
    dp['Sector'][index_no] = sector

dp.to_csv('csv/finalytd_returns.csv')

dp = pd.read_csv('csv/oneyear_returns.csv', index_col=0)
const = pd.read_csv('csv/constituents.csv')
dp['Name'] = None
dp['Sector'] = None
dp = dp.copy()

length = len(dp.index)

for index_no in range(length):
    name = dp['Ticker'][index_no]
    row = const[const['Symbol'].str.contains(name, case=True)]
    name = row['Name'].tolist()
    sector = row['Sector'].tolist()

    name = name[0]
    sector=sector[0]
    dp['Name'][index_no] = name
    dp['Sector'][index_no] = sector

dp.to_csv('csv/finaloneyr_returns.csv')

dp = pd.read_csv('csv/finalbottom10.csv', index_col=0)
const = pd.read_csv('csv/constituents.csv')
dp['Name'] = None
dp['Sector'] = None
dp = dp.copy()

length = len(dp.index)

for index_no in range(length):
    name = dp['Ticker'][index_no]
    row = const[const['Symbol'].str.contains(name, case=True)]
    name = row['Name'].tolist()
    sector = row['Sector'].tolist()

    name = name[0]
    sector=sector[0]
    dp['Name'][index_no] = name
    dp['Sector'][index_no] = sector

dp.to_csv('finalbottom10_returns.csv')

dp = pd.read_csv('csv/finaltop10.csv', index_col=0)
const = pd.read_csv('csv/constituents.csv')
dp['Name'] = None
dp['Sector'] = None
dp = dp.copy()

length = len(dp.index)

for index_no in range(length):
    name = dp['Ticker'][index_no]
    row = const[const['Symbol'].str.contains(name, case=True)]
    name = row['Name'].tolist()
    sector = row['Sector'].tolist()

    name = name[0]
    sector=sector[0]
    dp['Name'][index_no] = name
    dp['Sector'][index_no] = sector

dp.to_csv('csv/finaltop10_returns.csv')
