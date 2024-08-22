general_items = {
    "Sand toys",
    "Beach towels",
    "Beach umbrella",
    "Camp chair",
    "Snacks",
    "Hats",
    "Camera",
    "Sunglasses",
    "Alcholic Drinks",
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects"
}

restricted_items = {
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects",
    "Amplified Audio",
    "Drugs"
    }

# TODO
selection = int(input("Select Beach Type (1 - Family beach, 2 - Normal Beach): "))
if selection == 1:
    for item in restricted_items:
        general_items.discard(item)
else:
    for item in restricted_items:
        general_items.add(item)
general_items.discard("Drugs")
print("See below the list of items that you can take.")
print(general_items)