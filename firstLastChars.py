def first_last_characters(word):
    if len(word) < 2:
        return
    return word[0:2] + word[-2:]