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
    HeaderWritten = False
    fieldnames = ["Time", "Ticker", "latestPrice", "latestVolume", "Close", "Open", "low", "high"]
    with open("info.csv", "w") as csv_file:
        while time.time() < time_limit:
            for x in ticker_file:
                if time.time() < time_limit:
                    # the last time fetched should not equal the current time
                    L = UpdateStockInformation(x)
                    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                    if not HeaderWritten:
                        writer.writeheader()
                        HeaderWritten = True
                    writer.writerow({'Time': L[0], 'Ticker': L[1],'latestPrice': L[2], 'latestVolume': L[3], 'Close': L[4], 'Open': L[5], 'low': L[6], 'high': L[7]})
                else:
                    break
    ticker_file.close()

if __name__ == "__main__":
    time_limit =  time.time() + 10 #sys.argv[1]

    ticker_filename = "tickers.txt" #sys.argv[2]
    # info_filename = sys.argv[3]
    # file = open("info.csv",'a')

    while time.time() < time_limit:
        ticker_file = open(ticker_filename, "r")
        indefiniteUpdate(ticker_file, time_limit)