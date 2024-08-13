# TODO
custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
def group_types(custom_list):
    myDict = {}
    myDict = myDict.fromkeys(custom_list)
    for key in myDict:
        if isinstance(key, str):
            myDict[key] = "String"
        else:
            myDict[key] = "Integer"
    return myDict

print(group_types(custom_list))