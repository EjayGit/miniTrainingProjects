def convert_to_dict(tuple_list):
    myDict = {}
    for tup in tuple_list:
        key, value = tup
        myDict.setdefault(key, value)
    return myDict

tuple_list = [("one", 1), ("two", 2), ("three", 3), ("four", 4)]

convert_to_dict(tuple_list)