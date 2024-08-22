def value_length(p_dict):
    # TODO
    newDict = {}
    for key, value in p_dict.items():
        newDict[key] = {}
        newDict[key][value] = len(p_dict[key])
    return newDict

names_dict = {
    1 : "Elshad",
    2 : "Renad",
    3 : "Johanna",
    4 : "Appmillers"
}
value_length(names_dict)