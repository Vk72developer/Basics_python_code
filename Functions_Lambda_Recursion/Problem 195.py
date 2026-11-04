# Generator Function with yield 

def  countdown(n):
     while n > 0:
           yield n
           n -= 1 

gens = countdown(3)
print(next(gens))
print(next(gens))


for value in countdown(5):
    print(value, end='')
    print()