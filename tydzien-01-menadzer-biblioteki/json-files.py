import csv

menu = []

with open("items.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        menu.append({"name": row["name"], "attribute": row["attribute"]})

for dish in sorted(menu, key=lambda dish: dish["name"]):
    print(f"{dish['name']} is {dish['attribute'].lower()}")
