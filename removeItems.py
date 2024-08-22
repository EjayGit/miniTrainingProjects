def remove_empty_items(p_dict):
    # TODO
    for key, value in list(p_dict.items()):
        if value == None or value == "":
            p_dict.pop(key)
    return p_dict
    
custom_dict = {
    "name" : "Elshad",
    "age" : 28,
    "city" : None
}
remove_empty_items(custom_dict)