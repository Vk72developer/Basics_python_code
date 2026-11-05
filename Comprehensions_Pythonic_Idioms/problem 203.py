# Zip Two Lists into Pairs 

names = ["Asha", "Ravi", "Meera"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

score_map = dict(zip(name, scores))
print(score_map) 
