# Key with the Maximum Value

scores = {"Amit": 82, "Bela": 91, "Chad": 77 }

best = max(scores, key=scores.get)

print(f"{best} scored the highest: {scores[best]}")