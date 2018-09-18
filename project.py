import csv


def getArea(stateName):
    """ Function that takes in state name and returns the area of the state"""
    with open('area.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            if row[0] == stateName:
                return row[1]


def getPopulation(stateName,year):
    """ Function that takes in state name and year to returns the population for that year"""
    with open('population.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        row0= next(csvReader)
        print row0
        for row in csvReader:
            if row[0] == stateName and year == row0[1]:
                return row[1]
            elif row[0] == stateName and year == row[2]:
                return row[2]
            elif row[0] == stateName and year == row[3]:
                return row[3]

