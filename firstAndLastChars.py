def count_words(p_list):
    # TODO
    count = 0
    for string in p_list:
        if len(string) > 2:
            if string[0] == string[-1]:
                count += 1
    return count