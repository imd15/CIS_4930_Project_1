import sys
import requests as r
from iex import Stock

def save_tickers(n, fileName):
    #URL = r.get("https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download").text
    tickerList = []
    pure = r.get("https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&pagesize=150").text #get pure text from the website
    i =0 #counter
    #print(URL)
    baseStockUrl = "https://api.iextrading.com/1.0/stock"
    for curr in pure.splitlines(): #splits lines at new line
        if i == n:
            break
        else:
            try:
                subst = curr[curr.rfind("symbol/")::1] # parse all lines until 'symbol/' is found https://www.nasdaq.com/symbol/asps/stock-report">
                ticker = subst[subst.find("/")+1::1] # parse subst which contains 'asps/stock-report">'
                ticker2 = ticker[:ticker.find("/")] #parse to just get the symbol
                if ticker2.find("\"") == -1 and ticker2 != "":
                    Stock(ticker2).price() ## checks if valid ticker, if its not found go to except
                    i = i +1
                    tickerList.append(ticker2)
            except:
                pass

    file = open(fileName,"w") #creates ticker.text to write to it.
    file.write("\n".join(tickerList)) #puts everything that was in the list created with tickers on a new line
    file.close() #closes file


if __name__ == "__main__":
    # argv[1] = number of tickers
    # argv[2] = filename
    save_tickers(int(sys.argv[1]), sys.argv[2])
