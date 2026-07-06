menu = []

with open("items.csv") as file:
    for line in file:
        name, attribute = line.rstrip().split(",")
        dish = {"name": name, "attribute": attribute}
        menu.append(dish)

def get_name(dish):
    return dish["name"]

for dish in sorted(menu, key=get_name):
    print(f"{dish['name']} is {dish['attribute'].lower()}")
