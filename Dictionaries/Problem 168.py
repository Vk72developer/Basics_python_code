# Phone Book: Add, Search, Delete

phone_book = {}

def add(name, number):
    phone_book[name] = number 

def  search(name):
    return phone_book.get(name, "Not found")

def delete(name):
    if name in phone_book:
        del phone_book[name]
        return "Deleted"
    return "Not found"


add("Asha", "98765")
add("Ravi", "91243")

print(search("Asha"))
print(delete("Ravi"))
print(search("Ravi"))