# Pallindrome check

text = input("Enter a string: ").lower()

if text == text[::-1]:
    print("it is a palindrome")
else:
    print("not a pallindrome")