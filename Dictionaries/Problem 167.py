# Student Marks Average 

marks = {"Amit": [80, 90, 70], "Bela": [95, 85, 90]}

for name, scores in marks.items():
    average = sum(scores) / len(scores)
    print(f"{name}: {average:.1f}")