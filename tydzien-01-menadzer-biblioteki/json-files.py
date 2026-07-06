with open("items.txt", "r") as file:
    position = 0
    for line in sorted(file, reverse=True):
        position += 1
        print(position,line, sep=".", end="")



