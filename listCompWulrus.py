import random

def getTemp():
    return random.randint(20,30)


newList = [getTemp() for item in range(11) if getTemp()>25]
print(newList)

print(walrus := False)

inputs = list()
while (current := input('Type something')) != 'quit':
    inputs.append(current)
