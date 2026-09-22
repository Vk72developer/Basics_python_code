# Write a program to find the sum of Natural numbers. 

limit = int(input("Enter the limit:  "))

# initialize the sum 
sum = 0
for i in range(1, limit + 1):
            sum += i 


print("The sum of Natural numbers up to", limit, "is:", sum)