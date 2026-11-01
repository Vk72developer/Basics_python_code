# collections.defaultdict Grouping 

from collections import defaultdict 

students = [("A", "Amit"), ("B", "Bela"), ("A", "Asha")]

groups = defaultdict(list)

for grade, name in students:
    groups[grade].append(name)


print(dict(groups))