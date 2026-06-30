def calculate(a,b,operator):
    if operator == "+":
        print(f"The result is: {a+b}")
    elif operator == "-":
        print(f"The result is: {a-b}")
    elif operator == "*":
        print(f"The result is: {a*b}")
    elif operator == "/":
        if b != 0:
            print(f"The result is {round(a/b,2)}")
        else:
            print("You can't divide by 0")
    else:
        print("Invalid operator input")

def main():
    num1 = float(input("Insert first number: ").strip())
    num2 = float(input("Insert second number: ").strip())
    operator = input("Insert your operator(+,-,*,/): ").strip()
    calculate(num1,num2,operator)

main()