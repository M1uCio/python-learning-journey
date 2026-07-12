def classify_number(num):
    if num<0:
        return "negative"
    elif num > 0 and is_even(num):
        return "positiveEven"
    elif num > 0 and not is_even(num):
        return "positiveOdd"
    else:
        return "0"

def is_even(num):
    return num % 2 == 0

def main():
    x = int(input("Insert a number:"))
    match classify_number(x):
        case "negative":
            print("The number is negative")
        case "positiveEven":
            print("The number is positive and even")
        case "positiveOdd":
            print("The number is positive and odd")
        case _:
            print("The number is 0")
main()