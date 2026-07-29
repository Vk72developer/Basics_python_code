# Write a Python to make a simple Calculator with 4 basic mathematical operations. 

def   add(x, y):
    return x + y 


def   sub(x, y):
    return x - y 


def   mul(x, y):
    return x * y 


def   div(x, y):
    return x / y 

print("Select operations: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")

while True:

    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
        except ValueError:
            print("invalid input. please enter a number.")
            continue

        if choice == '1':
            print(num1, "+",num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))

        next_result = input("Let's do next acalculation? ")
        if next_result =="no":
            break

    else:
        print("invalid input ")