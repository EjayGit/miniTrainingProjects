def count_letter(word, letter):
    count = 0
    for index in word:
        if index == letter:
            count += 1
    return count