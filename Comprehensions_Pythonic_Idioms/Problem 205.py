# any() and all() checks

marks = [55, 89, 70, 91, 86]

everyone_passed = all(m >= 40 for m in marks)

has_distinction = any(m >= 90 for m in marks)

print("Everyone passed: ", everyone_passed)
print("Has a distinction: ", has_distinction)