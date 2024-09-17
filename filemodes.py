""" with open("sample1.txt", "w") as sfile:
    for i in range(11):
        sfile.write(f"{i}\n")
sfile.close()

with open("sample1.txt", "a") as sfile:
    for i in range(11,20):
        sfile.write(f'{i}\n')
sfile.close() """

with open('samplePrint.txt', 'a') as tFile:
    for i in range(20,30):
        print(i,file=tFile)

with open("samplePrint.txt") as file:
    for element in file:
        print(element, end='')

myList = [1,2,3,4]
textRep = myList.__str__()
print(type(myList))
print(type(textRep))