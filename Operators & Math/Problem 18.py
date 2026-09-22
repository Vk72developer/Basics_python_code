# Write a python program to print the Fibonacci sequence.

# F(0) = 0 
# F(1) = 1
# F(n) = F(n - 1) + F(n - 2) for n > 1

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0 , 1
count = 0

# check if the number of terms is valid

if nterms <= 0:
    print("Please enter a positive number ")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)

else:

    print("Fibonacci sequence: ")
    while count< nterms:
        print(n1) 
        nth = n1 + n2

        # update 
        n1 = n2 
        n2 = nth
        count += 1
