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

def get_history(ticker):
    pass

import pytz
from datetime import datetime

period_start = datetime(2010,1,1, tzinfo=pytz.utc)
end_time = datetime(2020,1,1, tzinfo=pytz.utc)
print(period_start,end_time)
exit()

for ticker in tickers:
    get_history(ticker)
