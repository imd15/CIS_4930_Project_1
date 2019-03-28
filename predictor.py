import sys,time
from sklearn.model_selection import train_test_split
from sklearn import linear_model as lm  
import numpy as np
import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt
def predictor(fileName, ticker, column, t, graphFile):
    '''
    columnVal = []
    timeVal=[]
    timeInMinutes = []
    with open(infoFileName, "r") as infoFile:
        reader = csv.DictReader(infoFile)
        for row in reader:
            if(row['Ticker'] == ticker):
                columnVal.append(float(row[column]))
                timeVal.append(datetime.striptime(row["Time"],"%H:%M"))

                
    print(timeVal)
    print(columnVal)
    newTimeVal = []

    for x in timeVal:
        x = x[:2] + '.' + x[3:]
        newTimeVal.append(float(x))
    #print(newTimeVal)
    
    holy = []

    for x,y in zip(columnVal,newTimeVal):
        #print([x, y])
        holy.append([x,y])

    #print(holy)
    '''
    regr = lm.LinearRegression()
    
    data = pd.read_csv(infoFileName)
    df=data.loc[data['Ticker']==ticker]
    print(df)
    latest = ''+column

    X = df[[latest]]
    Y=df['Time'].str.split(':').apply(lambda a: int(a[0])*60+int(a[1]))

    print(X)
    print(Y)

    data.plot(df,y=Y, style = 'o')
    plt.xlabel('Time in Min')
    plt.ylabel('Latest PRice')
    plt.show()  
    #print(X.loc[X['Ticker']==ticker])
    #print(X.values)


if __name__ == "__main__":
    ticker = "YI"               #argv[1]
    infoFileName = "info.csv"   #argv[2]
    graphFileName = ""          #argv[3]
    column = "latestPrice"      #argv[4]
    time = 10                   #argv[5]
    #predictor(fileName,ticker,column, )
    predictor(infoFileName,ticker,column,time,graphFileName)
    
    