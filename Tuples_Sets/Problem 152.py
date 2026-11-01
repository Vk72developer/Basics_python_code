# Frozen Set Demo 

fs = frozenset([1, 2, 3])
print(fs)

try:
    fs.add(4)
except AttributeError as e:
    print("Error:", e)

routes = {frozenset(["Delhi", "Mumbai"]): 1400}
print(routes[frozenset(["Delhi", "Mumbai"])])
