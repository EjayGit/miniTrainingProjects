my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}
# TODO
def multiply_values(my_dict):
    total = 1
    for key in my_dict:
        total = total * my_dict[key]
    return total
   
multiply_values(my_dict)