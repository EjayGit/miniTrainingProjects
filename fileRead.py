file = open('test.txt')
content = file.read()
print(content)
file.close()

with open('test.txt', mode='r') as file:
    line = file.readline()
    while line != "":
        print(line, end="")
        line = file.readline()
file.close()