#I didnt know the diffrence between csv and json, thats why its called json-files even though its csv
import csv

name = input("What's the dish's name?: ")
attribute = input("Is it fastfood or fit?: ")

with open("items.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "attribute"])
    writer.writerow({"name": name, "attribute": attribute})