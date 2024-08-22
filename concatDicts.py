def concatenate(d1,d2,d3):
    nDict = {}
    for dic in [d1,d2,d3]:
        nDict.update(dic)
    return nDict

dict1={
    1: "one",
    2: "two"}
dict2={
    3: "three",
    4: "four"}
dict3={
    5: "five",
    6: "six"}

concatenate(dict1,dict2,dict3)