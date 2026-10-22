# Sum of First N natural Numbers

n = int(input("Enter N: "))

total = 0
for i in range(1, n + 1):
    total += i 
print(f"Sum of first {n} natural numbers is {total}")
