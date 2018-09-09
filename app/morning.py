import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as pdr
import fix_yahoo_finance
from pattern.web import URL

tickers = pd.read_csv('static/wilshire5000.csv', delimiter=',')
tickers.head()

#pdr.get_data_yahoo(tickers['Ticker'][0], '2015-01-01', '2015-01-08')

for stock in tickers['Ticker']:
    webpage = "http://financials.morningstar.com/ajax/exportKR2CSV.html?t=%s&culture=en-CA&region=USA&order=asc&r=314562"%stock
    url = URL(webpage)
    f = open('%s_keyratios.csv'%stock, 'wb')
    f.write(url.download())
    f.close()
