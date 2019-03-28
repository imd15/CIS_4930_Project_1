import sys,time
from sklearn import linear_model as lm  
import numpy as np
import csv
import matplotlib.pyplot as plt
def predictor(fileName, ticker, column, t, graphFile):
    columnVal = []
    timeVal=[]
    with open(infoFileName, "r") as infoFile:
        reader = csv.DictReader(infoFile)
        for row in reader:
            if(row['Ticker'] == ticker):
                columnVal.append(float(row[column]))
                timeVal.append(row["Time"])

    print(timeVal)
    print(columnVal)
    newTimeVal = []

    for x in timeVal:
        x = x[:2] + '.' + x[3:]
        newTimeVal.append(float(x))
    print(newTimeVal)
    
    holy = []

    for x,y in zip(columnVal,newTimeVal):
        print([x, y])
        holy.append([x,y])

    print(holy)
    


if __name__ == "__main__":
    ticker = "YI"               #argv[1]
    infoFileName = "info.csv"   #argv[2]
    graphFileName = ""          #argv[3]
    column = "latestPrice"      #argv[4]
    time = 10                   #argv[5]
    #predictor(fileName,ticker,column, )
    predictor(infoFileName,ticker,column,time,graphFileName)
    
    '''
    regr = lm.LinearRegression()
    regr.fit(holy,newTimeVal)
    #predict = lm.predict()
    plt.scatter(newTimeVal,columnVal,  color='black')
    plt.title('Scatter plot pythonspot.com')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    #print(regr.coef_)
    #plt.show()


    data = pd.read_csv(infoFileName)
    index = data.index
    col = data.columns
    values=data.values
    latest = ''+column
    X=data.drop(['Close','Open','low','high'], axis=1)
    #print(X)
    print(X.loc[X['Ticker']==ticker])
    print(X.values)
    '''