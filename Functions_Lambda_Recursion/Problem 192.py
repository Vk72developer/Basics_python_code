# Recursion vs Iteration Comparison

def  fact_recursive(n):
    return 1 if n <= 1 else n * fact_recursive(n - 1)


def fact_iterative(n):
    result = 1 
    for i in range(2, n + 1):
        result *= i 
    return result 

print(fact_recursive(10))
print(fact_iterative(10))
