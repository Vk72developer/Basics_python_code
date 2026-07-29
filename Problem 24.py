# Write a program to convert Decimal to Binary, Octal and Hexadecimal. 

dec_num = int(input('Enter a decimal number: '))

print("The decimal value of", dec_num, "is:")
print(bin(dec_num), "in Binary.")
print(oct(dec_num), "in Octal.")
print(hex(dec_num), "in Hexadecimal.")