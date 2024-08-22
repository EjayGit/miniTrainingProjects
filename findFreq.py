def most_frequent(my_tuple):
    max = 0
    for el in my_tuple:
        num = my_tuple.count(el)
        if num > max:
            max = num
            value = el
    return (value, max)

my_tuple = ("a","b","c","d","e","a","c","e","b","e","c","a","f","e","r")
most_frequent(my_tuple)