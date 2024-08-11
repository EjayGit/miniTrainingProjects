def numbers_divisible_byfive(p_list):
    # TODO
    for num in p_list:
        if num > 130:
            break
        if (num%5 == 0):
            print(num)
    print("STOP")
