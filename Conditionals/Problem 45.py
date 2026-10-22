# Division by both 5 and 11 

num = int(input('Enter your number: '))

num1 = num % 5 == 0
num2 = num % 11 == 0

if num1 and num2:
    print(num, "is divisible by 5 and 11")
elif num1 or num2:
    print(num, "is divisible by only one of 5 and 11. ")
else:
    print(num, "is divisible by neither 5 nor 11")