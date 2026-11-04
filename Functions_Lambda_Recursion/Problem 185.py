# sorted() with key=lambda 

students = [("Amit", 82), ("bela", 91), ("Vikash", 82), ("chad", 77)]

by_marks = sorted(students, key=lambda s: s[1], reverse=True)

print(by_marks)

words = ["kiwi", "banana", "fig"]
print(sorted(words, key=len))