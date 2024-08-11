def square_list(p_list):
    # TODO
    square_list = []
    for number in p_list:
        square_list.append(p_list[number-1]*p_list[number-1])
    return square_list