import sys
import time
import json
import requests as r
from iex import Stock

def UpdateStockInformation(ticker):
    return



if __name__ == "__main__":
    #time_limit = sys.argv[1]
    ticker_filename = "tickers.txt" #sys.argv[2]
    #info_filename = sys.argv[3]
    ticker_file = open(ticker_filename, "r")

    for x in ticker_file:
        URL = f"https://ws-api.iextrading.com/1.0/stock/{x.strip()}/quote/"
        ahhhhh = r.get(URL).text
        #print(ahhhhh)
        yeet = json.loads(ahhhhh)
        print(yeet["symbol"] , yeet["high"])
        