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
    for i in Titles:
        L.append(textToJson[i])
    
    return L

def indefiniteUpdate(ticker_file, time_limit):
    fieldnames = ["Time", "Ticker", "latestPrice", "latestVolume", "Close", "Open", "low", "high"]
    tickerList = []
    returnList = []
    for x in ticker_file:
        tickerList.append(x.strip())

    with open("info.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        writer.writeheader()
        for x in tickerList:
            returnList.append(UpdateStockInformation(x))
        while time.time() < time_limit:
            for x in tickerList:
                if x[0] < strftime("%H:%M"):
                    returnList[tickerList.index(x)] = UpdateStockInformation(x)
        for row in returnList:
            writer.writerow({"Time": row[0], "Ticker": row[1], "latestPrice": row[2], "latestVolume": row[3], "Close": row[4], "Open": row[5], "low": row[7], "high": row[7]})

    ticker_file.close()
    return

if __name__ == "__main__":
    time_limit =  time.time() + 10 #sys.argv[1]

    ticker_filename = "tickers.txt" #sys.argv[2]
    # info_filename = sys.argv[3]
    # file = open("info.csv",'a')

    ticker_file = open(ticker_filename, "r")
    indefiniteUpdate(ticker_file, time_limit)