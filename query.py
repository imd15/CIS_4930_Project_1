import sys
import csv

def Query(info_filename, the_time, ticker):
    with open(info_filename, 'r') as f:
        reader = csv.reader(f)
        info_list = list(reader)        # creates a list of lists, each list index being a row  
        info_list = info_list[1:]       # get rid of the column names from the CSV
        the_tickers = []
        for x in info_list:
            the_tickers.append(x[1])    # extract just the ticker names from the CSV

        '''
        if (ticker not in the_tickers):
            print(f"{ticker} not found in {info_filename}")
        '''
    
    L = []

    return L


if __name__ == "__main__":
    # -verbose  = sys.argv[1]
    verbose = sys.argv[1]
    # -file = sys.argv[2]
    # info_filename = sys.argv[3]
    # –ticker = sys.argv[4]
    # ticker = sys.argv[5]
    # -time = sys.argv[6] --> Time sould be in HH:MM
    # the_time = sys.argv[7]

    info_filename = "info.csv"
    the_time = 10
    ticker = 'aapl'

    query_information = Query(info_filename, the_time, ticker)

    if verbose.lower() == "true":
        print("verbose")
    else:
        print("not verbose")
