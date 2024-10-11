ages = [10,12,6,10,24,35]

def custFunc(x):
    if x > 18:
        return True
    else:
        return False

adults = list(filter(custFunc, ages))
print(ages)
print(adults)

nums = list(range(1,31))
print(nums)
even = list(filter(lambda x: x%2 == 0, nums))
odd = list(filter(lambda x: x%2 != 0, nums))
print(even)
print(odd)

names = ['Erik', 'James', 'Jameson', 'Jess']
print(names)

shortNames = list(filter(lambda x: len(x)<5, names))
print(shortNames)

def lenName(a):
    return len(a)

newList = list(range(1,11))
print(nums)
even = list(map(lambda x:x%2==0, nums))
print(even)

wcTeams = [('Brazil',21),('Germany',19),('Argentina',17)]
print(wcTeams)
new = list(map(lambda team: (team[0], team[1]+1), wcTeams))
print(new)