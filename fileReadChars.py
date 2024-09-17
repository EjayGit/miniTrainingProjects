def number_of_characters(filename):
    with open(filename) as file:
        for index, row in enumerate(file):
            print(f"Line:{index+1} - {len(row)} characters")
        
number_of_characters("countries.txt")