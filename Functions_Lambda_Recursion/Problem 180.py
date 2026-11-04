# Prime check as a Function 

def is_prime(n):
    if n < 2:
        return False 
    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False 

    return True 

print(is_prime(29))
print(is_prime(30))
print([n for n in range(2, 20) if is_prime(n)])