import sys,time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


def predictor(fileName, ticker, column, t, graphFile):    
    timeInMin=int(datetime.now().hour)*60 + int(datetime.now().minute) #converts the current time to minutes

    data = pd.read_csv(infoFileName)
    dataFrame=data.loc[data['Ticker']==ticker] #locates all the data for the passed in ticker

    X_axis= dataFrame[[column]] #stores the data fo the column (latestValue/latestPrice) of the passed in ticker
    Y_axis=dataFrame['Time'].str.split(':').apply([lambda a: int(a[0])*60+int(a[1])]) #puts in the time in minutes into Y
    
    xTrain, xTest, yTrain, yTest = train_test_split(Y_axis,X_axis, test_size = 0.3, random_state = 0)
    
    regr = LinearRegression()

    regr.fit(xTrain,yTrain)                                     #fits the linear regression line
    #Code above was influenced from https://stackabuse.com/linear-regression-in-python-with-scikit-learn/

    for time in range(timeInMin, timeInMin+t):            #goes through new range of times we will predict
        b = plt.scatter(time, regr.predict([[time]]), color='red') #plots each predicted value on the graph
        
    
    c = plt.scatter(xTrain,yTrain, color = 'green') #plots observed value
    a = plt.plot(xTrain, regr.predict(xTrain), color = 'blue',) #creates a line of best fit
    plt.xlabel('Time(min)')
    plt.ylabel(column)
    plt.legend((c,b),('Observed data', 'Predicted data'))
    plt.savefig(graphFile)


if __name__ == "__main__":
    ticker = sys.argv[1].upper() #converts the ticker to uppercase
    infoFileName = sys.argv[2]
    graphFileName = sys.argv[3]
    column = sys.argv[4]
    time = int(sys.argv[5])
    predictor(infoFileName,ticker,column,time,graphFileName)