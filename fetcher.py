import sys
from time import localtime, strftime
import json
import csv
import requests as r
from iex import Stock

def UpdateStockInformation(ticker):
    URL = f"https://ws-api.iextrading.com/1.0/stock/{x.strip()}/quote/"
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



if __name__ == "__main__":
    #time_limit = sys.argv[1]
    ticker_filename = "tickers.txt" #sys.argv[2]
    #info_filename = sys.argv[3]
    file = open("info.csv",'w')
    ticker_file = open(ticker_filename, "r")
    
    for x in ticker_file:
        UpdateStockInformation(x)
        break
        
        