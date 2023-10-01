import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_sp500_tickers():
    
    res = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all('table')[0] 
    df = pd.read_html(str(table))
    tickers = list(df[0].Symbol)
    
tickers = get_sp500_tickers()

def get_history(ticker, period_start, period_end, granularity="1d"):
    import yfinance
    df = yfinance.Ticker(ticker).history(
        start=period_start, 
        end=period_end, 
        interval=granularity, 
        auto_adjust=True
    ).reset_index()
    df = df.rename(columns={
        "Date":"datetime",
        "Open":"Open",
        "High":"High",
        "Low":"Low",
        "Close":"Close",
        "Volume":"Volume"
        
    })
    input(df)

import pytz
from datetime import datetime

period_start = datetime(2010,1,1, tzinfo=pytz.utc)
period_end = datetime(2020,1,1, tzinfo=pytz.utc)

for ticker in tickers:
    get_history(ticker, period_start, period_end)
