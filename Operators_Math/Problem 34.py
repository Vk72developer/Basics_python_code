# Palindrome Number
# eg -> 121 ==> 121 is not

num = int(input("Enter a number: "))

rev = 0
n = num 
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if rev == num:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
