# Remove Duplicates Preserving order

def  dedupe(items):
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return  result 

print(dedupe([3, 1, 3, 2, 1, 5])) 