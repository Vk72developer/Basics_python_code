# Digital Root 

n = int(input("Enter a number: "))

while n >= 10:
    s = 0
    temp = n 
    while temp > 0:
        s += temp % 10 
        temp //= 10 

    n = s 
    print("Step: ", n)
print(f"Digital root: {n}")