# Unpacking with * (first, *rest)

nums = [10, 20, 30, 40, 50]

first, *rest = nums 

print("first:", first)
print("rest:", rest)

*init, last = nums 
print("init:", init)
print("last:", last)