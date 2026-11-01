# Count Items by Category

items = [("apple", "fruit"), ("carrot", "vegetable"),
         ("banana", "fruit"), ("potato", "vegetable"),
         ("mango", "fruit")
        ]

counts = {}

for name, category in items:
    counts[category] = counts.get(category, 0) + 1 

print(counts)