# map() to square a list 

nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, nums))
print(squares)

names = ["vikash", "ravi"]
print(list(map(str.upper, names)))
