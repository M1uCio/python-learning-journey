menu = []

with open("items.csv") as file:
    for line in file:
        name, attribute = line.rstrip().split(",")
        dish = {"name": name, "attribute": attribute}
        menu.append(dish)

for dish in menu:
    print(f"{dish['name']} is {dish['attribute'].lower()}")
