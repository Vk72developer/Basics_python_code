# Generator for Evens Numbers 

def  evens(limit):
    n = 2
    while n <= limit:
        yield n
        n += 2 

print(list(evens(10)))
print(sum(evens(100)))
