

def main():
    numbers = []
    result = 0

    numbers_count = get_numbers_count()

    for _ in range(numbers_count):
        numbers.append(get_positive_number())

    for number in numbers:
        result += number

    print(f"Sum of your numbers is: {result}")

def get_numbers_count():
    while True:
        try:
            n = int(input("How many numbers would you like to insert?: "))
        except ValueError:
            print("You must insert a number!")
            continue
        if n > 0:
            return n
        else:
            print("You must insert a positive number!")

def get_positive_number():
    while True:
        try:
            num = int(input("What is your number?" ))
        except ValueError:
            print("That is not a number!")
            continue
        if num > 0:
            return num
        else:
            print("You must insert a positive number!")
        
main()
