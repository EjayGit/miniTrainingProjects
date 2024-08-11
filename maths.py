# BODMAS
# +
# -
# *
# /   5 / 2 = 2.5 (and becomes a float)
# //  floor divide i.e. 5 // 2 = 2, not 2.5
# print(round(3.12345, 3) = 3.123 (3 dp from second arg)
# # %


size = input("What size burger would you like? (M/N/L)")
mushroom = input("Would you like mushrooms? (Y/N)")
cheese = input("Would you like extra cheese? (Y/N)")
if size == 'M':
    if mushroom == 'Y':
        costBurger = 6
    else:
        costBurger = 5
elif size == 'N':
    if mushroom == 'Y':
        costBurger = 9
    else:
        costBurger = 8
else:
    if mushroom == 'Y':
        costBurger = 12
    else:
        costBurger = 10

if cheese == 'Y':
    costBurger = costBurger + 1

print(f"Your final bill is: ${costBurger}.")