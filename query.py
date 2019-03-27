import sys, csv

def Query(info_filename, the_time, ticker):
    with open(info_filename, 'r') as f:
        reader = csv.reader(f)
        info_list = list(reader)[1:]    # creates a list of lists, each list index being a row

        the_tickers = []
        for x in info_list:
            the_tickers.append(x[1].lower())    # extract just the ticker names from the CSV
        
        if ticker not in the_tickers:
            raise Exception(f"Ticker {ticker} not found in {info_filename}")

        # return the information of the corresponding ticker at the index in the information list
        return info_list[the_tickers.index(ticker)]


if __name__ == "__main__":
    # -verbose  = sys.argv[1]
    verbose = sys.argv[2]
    # -file = sys.argv[3]
    info_filename = sys.argv[4]
    # –ticker = sys.argv[5]
    ticker = sys.argv[6]
    # -time = sys.argv[7] --> Time sould be in HH:MM
    the_time = sys.argv[8][0:5]

    # gather the necessary information on the ticker
    ticker_information = Query(info_filename, the_time, ticker.lower())

    # gather the information on the columns
    column_names = []
    with open(info_filename, 'r') as f:
        reader = csv.reader(f)
        info_list = list(reader)
        column_names = info_list[0]
        num_columns = len(column_names)
        num_rows = len(info_list[1:])

    if verbose.lower() == "true":
        # num rows and columns
        zipped = zip(column_names, ticker_information)
        for col, info in zipped:
            print(f"{col}: {info}")
        # print("verbose")
    else:
        for info in ticker_information:
            print(info)
        # print("not verbose")
    