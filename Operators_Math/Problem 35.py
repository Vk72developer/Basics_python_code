# All Factors of a number

num = int(input("Enter a number: "))

print("Factors of", num, "are:")

for i in range(1, num+1): # i is a factor if it
    if num % i == 0:
        print(i, end=" ") # prints on the same line

print() 