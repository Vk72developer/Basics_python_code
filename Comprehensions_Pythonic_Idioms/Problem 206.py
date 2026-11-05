# sorted() with a key Function 

words = {"kiwi", "banana", "fig", "apple"}

print(sorted(words, key=len)) 

students = [("Asha", 85), ("Ravi", 92), ("Meera", 78)]
by_marks = sorted(students, key=lambda s: s[1], reverse=True)

print(by_marks)