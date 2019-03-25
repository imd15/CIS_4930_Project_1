import sys
import requests as r

def save_tickers(n):
    URL = r.get("https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download").text

    pure = r.get("https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&pagesize=150").text #get pure text from the website
    i =0 #counter
    #print(URL)
    baseStockUrl = "https://api.iextrading.com/1.0"
    for curr in pure.splitlines(): #splits lines at new line
        if i == n:
            break
        else:
            subst = curr[curr.rfind("symbol/")::1]
            ticker = subst[subst.find("/")+1::1]
            ticker2 = ticker[:ticker.find("/")]
            if ticker2.find("\"") == -1 and ticker2 != "":
                print(ticker2)
                i+=1
        '''if ticker != "Symbol":
                print(ticker)
                i+=1'''


if __name__ == "__main__":
    save_tickers(int(sys.argv[1]))