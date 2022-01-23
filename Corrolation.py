import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        figure = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        figure.show()

def getDataSource(data_path):
    coffeeamount = []
    sleeptime = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffeeamount.append(float(row["Coffee in ml"]))
            sleeptime.append(float(row["sleep in hours"]))

    return {"x" : coffeeamount, "y": sleeptime}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation[0,1])

def setup():
    data_path  = "./coffeevssleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)


setup()