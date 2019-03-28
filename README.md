# Python Programming Project
##### Ian Dimitri and Kiel Peterson
##### CIS 4930 - Python Programming
######  Due March 28, 2019

## Modules
### Tickers Module
##### Summary
This module takes an input n and a filename (.txt) and outputs the first n
outputs from the website below and putputs those tickers to the filen passed in
> http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download

###### This module accepts:
- n
	- how many tickers will be output to the file
- fileName
	- the file that the tickers will be printed to

##### How to run:
```python3 tickers.py n fileName```
### Fetcher Module
##### Summary
This module reads all the tickers from a file (say, *tickers.txt*), and fetches the following information for each ticker:

	- Time
	- Ticker
	- latestPrice
	- latestVolume
	- Close
	- Open
	- low
	- high

###### This module accepts:
- time_limit
	- in seconds
- ticker_filename 
	- presumably the one created from fetcher.py
- info_filename
	- output into a .csv file format

##### How to run:
```python3 fetcher.py time_limit ticker_filename info_filename```
### Query Module
##### Summary
Prints the information passed in from a CSV file for a particular ticker at a certain time. The information it prints is based off the header row of the .csv file, as well as what is in the .json this module reads in. We did not test for this, but we would assume that should a column in the csv not be found in the .json the API gathers, then it would not work, since it wouldn't be able to find it in the dictionary.

In short, this queries information from the .csv for a ticker at a particluar time.

###### This module accepts:
- -verbose (flag)
- True/False
	- whether to print the number of columns/rows
- -file (flag)
- info_filename
	- the file that read to gather the column information
- -ticker (flag)
- ticker
	- the ticker that will be queried
- -time (flag)
- time
	- the time that the ticker will be queried at (HH:MM)

##### How to run:
```python3 query.py –verbose True/False –file info_filename –ticker ticker –time time```
### Predictor Module
##### Summary
This module predicts information for a specific ticker based off of historical data passed in from the information file to predict the next *n* minutes. The information is read from the information file, the data is selected for the specified ticker, and then a machine learning module is trained to predict the information for the next *n* minutes. The *Time* column is used to predict the value of *col* based off the historical data.


This module uses the *sklearn.linear model* to predict this. The information is saves and plots the historical variation in the value of col as well as the predicted values. 

###### This module accepts:
- ticker
	- the ticker that is predicted
- infoFilename 
	- the file read to gather the historical data
- graphFilename
	- the file that the graph will be created to
- column
	- either latestPrice or latestVolume
- time
	- the number of minutes that will be predicted

	##### How to run:
```python3 predictor.py ticker infoFilename graphFilename column time```


## Miscellaneous Notes
- For convenience of grading/testing, a bash script, **run.sh**, has been provided. You might need to add executable permissions to this to run it. Please keep in mind that the bash location was updated to work on a local Mac, so it may vary from machine to machine.


- As far as we are aware, there should not be any major issues. As of 3/28/19, everything works and runs correctly on both of our machines. We are both running on Python 3.7.2.


- In regards to both partners contributing equally, we only worked together and in-person so that we could easily communicate with each other. Most of the contributions made to this repo were made together and in-person, just so that we could both continue to work together.

The Query issue has been fixed

When running 
> python3 query.py –verbose True –file info.csv –ticker YI –time 17:40

Assuming it works correct, we get something along the lines of:
```-----------------------------------------------------------
Number of columns in info.csv: 8
Number of rows in info.csv: 774
-----------------------------------------------------------
Time: 17:40
Ticker: YI
latestPrice: 5.69
latestVolume: 56417
Close: 5.69
Open: 6.46
low: 5.6
high: 6.667
