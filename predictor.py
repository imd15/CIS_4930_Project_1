import sys,time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  
import numpy as np
import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
def predictor(fileName, ticker, column, t, graphFile):    
    curr = datetime.now()
    convertToMin=int(curr.hour)*60 + int(curr.minute)
    timeToPredict= convertToMin + t
    
    test = []
    test.append(timeToPredict)

    data = pd.read_csv(infoFileName)
    df=data.loc[data['Ticker']==ticker]
    print(df)
    latest = ''+column

    X = df[[latest]]
    Y=df['Time'].str.split(':').apply([lambda a: int(a[0])*60+int(a[1])])

    print(X)
    print(Y)
    xTrain, xTest, yTrain, yTest = train_test_split(Y,X, test_size = 1/3, random_state = 0)

    regr = LinearRegression()
    regr.fit(xTrain,yTrain)
    yPredict= regr.predict(xTest)

    plt.scatter(xTrain,yTrain,color = 'red')
    plt.plot(xTrain, regr.predict(xTrain), color = 'blue')
    plt.xlabel('xxxxxxxxx')
    plt.ylabel('yyyyyyyyy')
    #plt.show()
    plt.savefig(graphFile)

    print(regr.predict([test]))
    #print(X.loc[X['Ticker']==ticker])
    #print(X.values)


if __name__ == "__main__":
    ticker = "YI"               #argv[1]
    infoFileName = "info1.csv"   #argv[2]
    graphFileName = "graph.png"          #argv[3]
    column = "latestVolume"      #argv[4]
    time = 10                   #argv[5]
    #predictor(fileName,ticker,column, )
    predictor(infoFileName,ticker,column,time,graphFileName)