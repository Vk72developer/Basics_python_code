# Tuple vs List Immutability 

nums_tuple = (1, 2, 3)
nums_list = [1, 2, 3]

try:
    nums_tuple[0] = 99
except TypeError as e:
    print("Tuple error:", e)

nums_list[0] = 99 
print("List after change:", nums_list)