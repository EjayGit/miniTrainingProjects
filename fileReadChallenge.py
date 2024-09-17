def numberOfLines():
    # check filename is correct and get file obj
    filename = input("Enter the filename: ")
    try:
        file = open(filename)
    except FileNotFoundError:
        print("Please enter a correct filename: ")
        exit()
    # if line starts with word, count line
    word = input("Enter the word: ")
    count = 0
    # print each line
    for line in file:
        line = line.rstrip()
        if line.startswith(word):
            count += 1
    print(f"There are {count} occurrences of {word} in {filename}")
    

numberOfLines()
