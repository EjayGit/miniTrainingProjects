def print_pattern(n):
    # TODO
    for i in range(n):
        print("* "*i)
    for i in range(n,0, -1):
        print("* "*i)
        
        
names = ['John', 'Edy', 'Jane', 'Kane']
scores = [90, 95, 80, 75]
print("{0:<10} {1:<5}".format("Name","Score"))
for index in range(len(names)):  
    print("{0:<10} {1:<5}".format(names[index],scores[index]))