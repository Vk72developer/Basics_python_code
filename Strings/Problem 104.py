# Angram Check 

s1 = input("Enter first word: ").lower()
s2 = input("Enter second word: ").lower()

if sorted(s1) == sorted(s2):
    print("They are anagrams")
else:
    print("Not anagrams")