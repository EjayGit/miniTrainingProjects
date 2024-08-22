def merge_dict(d1, d2):
    d3 = {}
    d3.update(d1)
    d3.update(d2)
    return d3

dict1 = {'One': 2, 'Two': 2, 'Three': 3}
dict2 = {'Three': 3, 'Four': 4, 'Five': 5}
merge_dict(dict1, dict2)