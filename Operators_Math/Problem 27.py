# Write a Python program to find fibonacci sequence using Recursion.

def  rec_fib(n):
    if n <= 1:
        return n 
    else:
        return(rec_fib(n - 1) + rec_fib(n - 2))

nterms = int(input("Enter the number of terms: "))

if nterms <= 0:
    print("Please enter a positive integer: ")
else:
    print("fibonacci sequence: ")
    for i in range(nterms):
        print(rec_fib(i))