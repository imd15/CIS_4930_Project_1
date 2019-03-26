import sys
import time
from iex import Stock

def UpdateStockInformation(ticker):
    return



if __name__ == "__main__":
    time_limit = sys.argv[1]
    ticker_filename = sys.argv[2]
    info_filename = sys.argv[3]
    ticker_file = open(ticker_filename, "r")

    for x in ticker_file:
        stock = Stock(x)
        quote = stock.get_quote()
        print(quote)