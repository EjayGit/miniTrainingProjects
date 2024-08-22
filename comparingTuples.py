def order_words(text):
    numList = list()
    words = text.split()
    for word in words:
        numList.append((len(word), word))
    numList.sort()
    result = list()
    for length, word in numList:
        result.append(word)
    return tuple(result)

order_words("Python is my favorite programming language")