with open("EuropePopulation.csv") as file:
    data = file.readlines()
    print(data)

import csv
with open("EuropePopulation.csv") as file:
    data = csv.reader(file)
    population = []
    for row in data:
        print(row)
        if row[2] != "pop":
            population.append(int(row[2]))
    print(population)

import pandas
data = pandas.read_csv("EuropePopulation.csv")
print(data["pop"])
print(type(data))
basicStats = data.describe(include="all")
print(basicStats)

dataList = data["pop"].to_list()
print(dataList)
print(sum(dataList)/len(dataList))  #avg
print(data["pop"].mean())           #avg
print(data["pop"].max())            #max
#print(data.pop.max()) # would work if .pop was not an in built menthod

population = pandas.Series([1000,2000,500], index=["London", "Berlin", "Tokyo"])
revenue = pandas.Series({"London": 1000000, "Berlin":2030292})
colours = pandas.Series(["blue", "green", "yellow", "red", "purple"], index=[1, 2, 4, 6, 8])
print(colours[4])
print(colours.loc[2])               #label index
print(colours.iloc[2])              #positional index
print(colours.loc[1:4])
print(colours.iloc[1:4])

officeCount= pandas.Series([10,20], index=["London", "Berlin"])

cityData = pandas.DataFrame({"population": population, "office_count":officeCount})
print(cityData.axes)
print(cityData.iloc[2])
print("pop" in data.keys())
print(data.iloc[-3:])

print(cityData[cityData.office_count.notnull()])