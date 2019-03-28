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

def indefiniteUpdate(ticker_file,info_filename, time_limit):
    for x in ticker_file:
        if time.time() < time_limit:
            L = UpdateStockInformation(x)
            with open(info_filename, "a") as csv_file:
                fieldnames = ["Time", "Ticker", "latestPrice", "latestVolume", "Close", "Open", "low", "high"]
                writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                writer.writerow({'Time': L[0], 'Ticker': L[1],'latestPrice': L[2], 'latestVolume': L[3], 'Close': L[4], 'Open': L[5], 'low': L[6], 'high': L[7]})
                csv_file.close()
        else:
            break    

if __name__ == "__main__":
    time_limit =  time.time() + int(sys.argv[1])

    ticker_filename = sys.argv[2]
    info_filename = sys.argv[3]
    #file = open("info.csv",'a')
    HeaderWritten = False

    with open(info_filename,'w') as info: ##this just goes ahead and prints the headers into the first line of the file
        headerWriter = csv.writer(info, delimiter=',')

        headerWriter.writerow(["Time", "Ticker", "latestPrice", "latestVolume", "Close", "Open", "low", "high"])
    
    while time.time() < time_limit:
        starting_time = strftime("%H:%M")
        ticker_file = open(ticker_filename, "r")
        indefiniteUpdate(ticker_file,info_filename, time_limit)
        ticker_file.close()
        while starting_time == strftime("%H:%M") and time.time() < time_limit:
            pass
