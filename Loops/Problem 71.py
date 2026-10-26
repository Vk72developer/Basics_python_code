# Binary to Decimal 

bits = input("Enter a binary number: ")

decimal = 0
for bit in bits:
    decimal = decimal * 2 + int(bit)

print(f"Decimal value: {decimal}") 