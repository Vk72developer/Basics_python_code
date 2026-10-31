# Cumulative Sum 

# ex-: [1, 2, 3, 4, 5] 
#   output => cumulative sum [1, 3, 6, 10]

numbers = [1, 2, 3, 4]
running = 0
cumulative = []
for n in numbers:
    running += n
    cumulative.append(running)

print("Cumulative sum:", cumulative)