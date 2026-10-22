# Income Tax calculator with slabs 

# Compute Income tax: 
#     no tax up to Rs. 2,50,000;
#     5% on the next Rs. 2,50,000;
#     20% on the next Rs. 5,00,000;
#     and 30% on income above Rs. 10,00,000.
#  print the total tax.

income = float(input("Enter annual income: "))

tax = 0.0 
if income > 1000000:
    tax += (income - 1000000) * 0.30
    income = 1000000
if income > 500000:
    tax += (income - 500000) * 0.20
    income = 500000
if income > 250000:
    tax += (income - 250000) * 0.05 

print(f"Total tax = Rs. {tax:.2f}")