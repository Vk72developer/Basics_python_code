# LCM of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b

while y != 0: #first find the GCD
    x, y = y , x % y

lcm = a * b // x  # // keeps the result an integer
print(f"LCM of {a} and {b} is {lcm}")