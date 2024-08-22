def even_index_items(p_tuple):
    # TODO
    temp = []
    for index, value in enumerate(p_tuple, 1):
        if index % 2 != 0:
            temp.append(value)
    nTuple = tuple(temp)
    return nTuple

my_tuple = ("a", "b", "c", "d", "e", "f", "g")
even_index_items(my_tuple)