from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
import datetime
import pandas_datareader.data as web
# from stockdata import get_stockdata
# from stockreturns import get_stockreturns
# from sentiment import get_sentiment


#We're going to initialize the app
app = Flask(__name__)


#Create our main page that redirects to index
@app.route('/')
def start():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results')
def result():
    #We're going to import a dataframe then submit it into a table
    top10 = pd.read_csv('csv/finaltop10_returns.csv', index_col=0)
    bottom10 = pd.read_csv('csv/finalbottom10_returns.csv', index_col=0)

    top_Ticker = top10['Ticker'].tolist()
    colname = top10.columns[1]
    top_Return = top10[colname].tolist()
    top_Sentiment = top10['Sentiment'].tolist()
    top_Name = top10['Name'].tolist()
    top_Sector = top10['Sector'].tolist()

    bottom_Ticker = bottom10['Ticker'].tolist()
    colname = bottom10.columns[1]
    bottom_Return = bottom10[colname].tolist()
    bottom_Sentiment = bottom10['Sentiment'].tolist()
    bottom_Name = bottom10['Name'].tolist()
    bottom_Sector = bottom10['Sector'].tolist()

    #We need to create a nested list to make it easier to template
    table_values = list(zip(top_Ticker, top_Return, top_Sentiment, top_Name, top_Sector))
    table_values1 = list(zip(bottom_Ticker, bottom_Return, bottom_Sentiment, bottom_Name, bottom_Sector))
    return render_template('results.html', table_values=table_values, table_values1=table_values1)

@app.route('/returns')
def returns():
    #We're going to import a dataframe then submit it into a table
    ytd = pd.read_csv('csv/finalytd_returns.csv', index_col=0)
    oneyear = pd.read_csv('csv/finaloneyr_returns.csv', index_col=0)

    ytd_Ticker = ytd['Ticker'].tolist()
    colname = ytd.columns[1]
    ytd_Return = ytd[colname].tolist()
    ytd_Name = ytd['Name'].tolist()

    oneyear_Ticker = oneyear['Ticker'].tolist()
    colname = oneyear.columns[1]
    oneyear_Return = oneyear[colname].tolist()
    oneyear_Name = oneyear['Name'].tolist()

    #We need to create a nested list to make it easier to template
    table_values = list(zip(ytd_Ticker, ytd_Return, ytd_Name))
    table_values1 = list(zip(oneyear_Ticker, oneyear_Return, oneyear_Name))
    return render_template('returns.html', table_values=table_values, table_values1=table_values1)



#Create a running condition
if __name__ == '__main__':
    app.run(debug=True)
