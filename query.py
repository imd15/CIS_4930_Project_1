import sys, csv
from time import localtime, strftime
import time
import requests as r
import json

def Query(info_filename, the_time, ticker, column_names):
    with open(info_filename, 'r') as f:
        reader = csv.reader(f)
        info_list = list(reader)[1:]    # creates a list of lists, each list index being a row

        the_tickers = []
        for x in info_list:
            if not x:
                pass
            else:
                the_tickers.append(x[1].lower())    # extract just the ticker names from the CSV
        
        if ticker not in the_tickers:
            raise Exception(f"Ticker {ticker} not found in {info_filename}")

    while strftime("%H:%M") != the_time:
        continue

    URL = f"https://ws-api.iextrading.com/1.0/stock/{ticker}/quote/"
    pureURLtext = r.get(URL).text
    textToJson = json.loads(pureURLtext) #creates dict from what was in url
    Titles = ["symbol","latestPrice", "latestVolume","close","open","low","high"]
    timee = strftime("%H:%M")
    L = [timee]
    for i in Titles:
        L.append(textToJson[i])
    
    return L

if __name__ == "__main__":
    # -verbose  = sys.argv[1]
    verbose = sys.argv[2]
    # -file = sys.argv[3]
    info_filename = sys.argv[4]
    # –ticker = sys.argv[5]
    ticker = sys.argv[6]
    # -time = sys.argv[7] --> Time sould be in HH:MM
    the_time = sys.argv[8][0:5]

    # gather the information on the columns
    column_names = []
    with open(info_filename, 'r') as f:
        reader = csv.reader(f)
        info_list = list(reader)
        column_names = info_list[0]

    # gather the necessary information on the ticker
    ticker_information = Query(info_filename, the_time, ticker.lower(), column_names)

    if verbose.lower() == "true":
        print("-----------------------------------------------------------")
        print(f"Number of columns in {info_filename}: {len(column_names)}")
        print(f"Number of rows in {info_filename}: {len(info_list[1:])}")
        print("-----------------------------------------------------------")

    zipped = zip(column_names, ticker_information)
    for col, info in zipped:
        print(f"{col}: {info}")
    