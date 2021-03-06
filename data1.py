import plotly_express as px 
import csv
import numpy as np

def getDataSource(dataPath):
    marks=[]
    days = [] 
    with open("data1.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append (float(row["Marks In Percentage"]))
            days.append (float(row["Days Present"]))
            
    return {"x":marks, "y":days}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])
    
def SetUp():
    dataPath = "data1.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    
SetUp()
    
    
     