# Simple Logging Decorator 

def logger(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")
        return result 
    return wrapper 

@logger
def add(a, b):
    return a + b 

print(add(3, 4))