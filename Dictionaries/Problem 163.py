# Merge Two Dictionaries

defaults = {"theme": "light", "font": 12}
user = {"theme": "dark", "lang": "en"}

merged = {**defaults, **user}

print(merged)

merged2 = defaults | user 
print(merged2)