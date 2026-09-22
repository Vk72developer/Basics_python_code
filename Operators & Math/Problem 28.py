# Write a Python Program to find factorial of number using recursion. 

def recur_fact(n):
    if n == 1:
        return n
    else:
        return n*recur_fact(n - 1)

num = int(input("Enter the number: "))

if num < 0:
    print("Factorial does'nt exist ")
elif num == 0:
    print("factorial is 1")
else:
    print("Factorial", num, "is", recur_fact(num))