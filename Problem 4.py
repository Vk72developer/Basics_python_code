# Write a python program to swap two numbers 

# input two variables 
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")

# display the original values

print(f"original values: a = {a}, b = {b}")

# swap the values using a temp variable 

temp = a 
a = b 
b = temp 

# display the swapped values

print(f"Swapped values: a = {a}, b = {b}")
