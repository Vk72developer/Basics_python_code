# Flatten a Nested List

def flatten(items):

    flat = []
    for item in items:
        if isinstance(item, list):
            flat.extend(flatten(item))

        else:
            flat.append(item)
    return flat 

nested = [1, [2, 3], [4, [5, 6]], 7]
print("flattened:", flatten(nested))