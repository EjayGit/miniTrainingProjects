# ToDo
def count_character(word):
    myDict = {}
    for char in word:
        if char in myDict:
            # add value to key by +1
            myDict[char] = myDict[char] + 1
        else:
            # add key and make value = 1
            myDict[char] = 1

print(count_character("BABACDAS"))