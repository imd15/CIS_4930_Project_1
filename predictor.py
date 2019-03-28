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

    X = df[[column]]
    Y=df['Time'].str.split(':').apply([lambda a: int(a[0])*60+int(a[1])])

    times= []
    for time in range(convertToMin,timeToPredict):
        times.append(time)
    
    xTrain, xTest, yTrain, yTest = train_test_split(Y,X, test_size = 1/3, random_state = 0)

    regr = LinearRegression()
    regr.fit(xTrain,yTrain)
    yPredict= regr.predict(xTest)
    for time in range(convertToMin,timeToPredict):
        b = plt.scatter(time, regr.predict([[time]]), color='green')
        
    
    c = plt.scatter(xTrain,yTrain,color = 'red')
    a = plt.plot(xTrain, regr.predict(xTrain), color = 'blue',)
    plt.xlabel('Time in Minutes')
    plt.ylabel(column)
    plt.legend((a,c,b),('Line of best Fit','Observed data', 'Predicted data'))
    plt.show()
    plt.savefig(graphFile)


if __name__ == "__main__":
    ticker = sys.argv[1]
    infoFileName = sys.argv[2]
    graphFileName = sys.argv[3]
    column = sys.argv[4]
    time = int(sys.argv[5])
    predictor(infoFileName,ticker,column,time,graphFileName)