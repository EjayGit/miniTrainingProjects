"""
names = ['Paul', 'John', 'Simon', 'Elon', 'Bob', 'Eddy', 'Bill']

def containsN(pNames):
    for name in pNames:
        if 'n' in name:
            yield name  

gen_ob = containsN(names)
print(list(gen_ob))
print(set(containsN(names)))
print(tuple(gen_ob))

#for element in gen_ob:
#    print(element)

#print(list(gen_ob))

print(next(gen_ob))
print(next(gen_ob))
print(next(gen_ob))
print(next(gen_ob))
print(next(gen_ob))
"""

square = (num**2 for num in range(1,6))
print(square)
#square = [num**2 for num in range(1,6)]
#print(square)
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
#print(next(square))