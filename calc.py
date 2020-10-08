import math
from decimal import Decimal

fiftythree = True
def fun():
    fiftythree = False

equals = "="
add_symbol = "+"
subtract_symbol = "-"
multiply_symbol = "x"
divide_symbol = "/"


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Pythagorean Theorem - Hypotenuse")

while True:
    choice = input("Enter choice(1/2/3/4):  ")
    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number:  "))
        num2 = float(input("Enter second number:  "))

        if choice == '1':
            print(num1, add_symbol, num2, equals, add(num1, num2))

        elif choice == '2':
            print(num1, subtract_symbol, num2, equals, subtract(num1, num2))

        elif choice == '3':
            print(num1, multiply_symbol, num2, equals, multiply(num1, num2))

        elif choice == '4':
            print(num1, divide_symbol, num2, equals, divide(num1, num2))
        
        elif choice == '5':
            sum1 = int(num1**2) + int(num2**2)
            answer1 = math.sqrt(sum1)
            print(answer1)
            answer1 = Decimal(answer1)
            YORN = input("Round?[y][n]  ")
            if YORN == 'Y':
                print("Select option for rounding.")
                print("1. Nearest tenth")
                print("2. Nearest hundredth")
                while True:
                    choice2 = input("Enter choice(1/2):  ")
                    if choice2 in ('1', '2'):
                        if choice2 == '1':
                            print(round(answer1, 1))

                        elif choice2 == '2':
                            print(round(answer1, 2))

                        break
                    else:
                        print("invalid input")
            elif YORN == 'Y':
                fiftythree
        break
    else:
        print("invalid input")
