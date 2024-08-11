def concatenate(list1, list2):
    # TODO
    list3 = []
    for word1 in list1:
        for word2 in list2:
            list3 = list3 + [word1 + word2]
    return list3
    
list1 = ['Hello', 'take']
list2 = ['Dear', 'Sir']
concatenate(list1, list2)