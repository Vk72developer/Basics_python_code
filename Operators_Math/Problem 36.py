# Armstrong Number
# eg-: 153 = cube(1) + cube(5) + cube(3)

num = int(input("Enter a number: "))

digits = len(str(num))
total = 0
n = num
while n > 0:
    total += (n % 10) # ** digits
    n //= 10

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")