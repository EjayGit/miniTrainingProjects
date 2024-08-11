def add_even_numbers(start, end):
    # TODO
    if start%2 > 0:
        start += 1
    total = 0
    for num in range(start, end+1, 2):
        total += num
    return total