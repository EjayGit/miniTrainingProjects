import random

cityNames = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']

oldDict = {city: random.randint(20,30) for city in cityNames}
print(oldDict)

# newDict = {newKey: newValue for (key, value) in oldDict.items() if condition}
newDict = {city: temp for (city, temp) in oldDict.items() if temp > 25}
print(newDict)

