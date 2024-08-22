import copy

def deep_copy(original_dict):
    deepCopy = copy.deepcopy(original_dict)
    return deepCopy

original_dict = {
    "names" : ["Elshad", "John", "Edy"],
    "numbers" : [1,2,3,4,5]
}
 
copied_dict = deep_copy(original_dict)
copied_dict["names"].append("Jack")
copied_dict["numbers"].append(6)
 
print(original_dict)
print(copied_dict)