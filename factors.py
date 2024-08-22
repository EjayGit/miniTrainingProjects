# TODO
def divisible_by_3and4(N):
    resultSet = set()
    for num in range(0,N):
        if (num % 3 == 0) and (num % 4 == 0):
            resultSet.add(num)
    return resultSet

divisible_by_3and4(100)
###

def divisible_by_3and4(N):
    set1 = set(range(0,N,3))
    set2 = set(range(0,N,4))
    set3 = set1.intersection(set2)
    return set3