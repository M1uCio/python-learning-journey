def main():
    size = get_positive_number()
    print_pyramid(size)
    
def get_positive_number():
    while True:
        try:
            num = int(input("What should be the height of pyramid?: ").strip())
        except ValueError:
            print("You must insert a number")
            continue
        if num > 0:
            return num
        else:
            print("You must insert a positive number")

def print_pyramid(height):
    for i in range(height):
        row = "#" * (i+1)
        print(f"{row:>{height}}")

main()