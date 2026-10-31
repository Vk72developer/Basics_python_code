# Separate Even and Odd Numbers

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = []
odds = []

for n in num:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n) 

print("Evens:", evens)
print("Odds:", odds)
