# Dict from Two Lists via zip()

names = ["Asha", "Ravi", "Meena"]

ages = [25, 30, 28]

people = dict(zip(names, ages))
print(people)