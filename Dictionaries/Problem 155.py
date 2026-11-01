# Safe Key Lookup with.get()

person = {"name": "Ravi", "age": 30}

print(person.get("name"))
print(person.get("city"))

print(person.get("city", "Not found"))

print("city" in person)