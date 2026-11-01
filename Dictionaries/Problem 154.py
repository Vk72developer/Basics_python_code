# Iterate Keys, Values & Items 

marks = {"math": 90, "science": 85}

for subject in marks:
    print(subject) 

for score in marks.values():
    print(score)

for subject, score in marks.items():
    print(f"{subject} = {score}")