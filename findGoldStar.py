import random
def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))

map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
print("This is our initial map...")
print_map(map1)

starRow = random.randint(0,2)
starCol = random.randint(0,2)
[position] = input('Where do you think the golden star is on the map? Enter the row then column separated by a space: ')
userRow = int(position[0]) - 1
userCol = int(position[1]) - 1

map1[starRow][starCol] = '⭐'
if userRow == starRow and userCol == starCol:
    print_map(map1)
    print("Well done! You got it!")
else:
    map1[userRow][userCol] = 'X'
    print_map(map1)
    print("Not so lucky, try the game again!")

input()