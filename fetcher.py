import sys
from time import localtime, strftime
import time
import json
import csv
import requests as r
from iex import Stock

def UpdateStockInformation(ticker):
    URL = f"https://ws-api.iextrading.com/1.0/stock/{ticker.strip()}/quote/"
    pureURLtext = r.get(URL).text
    textToJson = json.loads(pureURLtext) #creates dict from what was in url
    Titles = ["symbol","latestPrice", "latestVolume","close","open","low","high"]
    timee = strftime("%H:%M")
    L = [timee]
    print(Titles)
    for i in Titles:
        L.append(textToJson[i])
    
    print(L)
    
    #print(ahhhhh)
    
    return

def indefiniteUpdate(ticker_file):
    for x in ticker_file:
        if time.time() < time_limit:
            UpdateStockInformation(x)
        else:
            break

if __name__ == "__main__":
    time_limit =  time.time() + 10#sys.argv[1]

    ticker_filename = "tickers.txt" #sys.argv[2]
    #info_filename = sys.argv[3]
    file = open("info.csv",'w')
    
    
    

    while time.time() < time_limit:
        ticker_file = open(ticker_filename, "r")
        indefiniteUpdate(ticker_file)
        