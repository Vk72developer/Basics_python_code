# Triangle Type Checker 

# Read three side lengths. First check whether they can form a valid triangle {sum of any two sides greater than the third}.
# if valid, print whether the triangle is equilateral, isosceles or scalene. 

a, b, c = map(int, input("Enter three sides: ").split())

# triangle inequality: every pair of sides must outweigh the third side 

if a+b > c and b+c > a and a+c > b:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

else:
    print("Not a valid triangle")