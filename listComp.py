# list comprehension
simpleList = [f'{j}{i}' for i in range(0,11,1) for j in ('a','b','c') if j == 'a']
# for i in range(0,11,1):
#   simpleList.append(i)
print(simpleList)

# lambda func
# def doubleValue(num):
#   return unm * 2
doubleValue = lambda num: num * 2
print(doubleValue(10))

