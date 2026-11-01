# Invert a Dictionary

capitals = {"India": "Delhi", "Japan": "Tokyo"}

inverted = {city: country for country, city in capitals.items()}

print(inverted)