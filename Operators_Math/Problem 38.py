# G.C.D of Two Numbers

a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 

x,y = a, b

while y != 0:
    x, y = y, x % y # replace (x,y) with (y, remainder) until remainder is 0

print(f"GCD of {a} and {b} is {x}")