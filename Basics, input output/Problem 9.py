# Write a python program to solve quadratic equation. 

import math 

# Calculate coefficients 

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

#  calculate the discriminant

discriminant = b ** 2 - 4 * a * c 

# check if the discriminant is positive, negative or zero 

if discriminant > 0:

    root1 = ( -b + math.sqrt(discriminant)) / (2*a)
    root2 = ( -b + math.sqrt(discriminant)) / (2*a)
    
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")

elif discriminant == 0: 

    root = -b / (2*a)
    print(f"Root : {root}")

else: 
    # complex roots 
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a) 

    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} + {imaginary_part}i")