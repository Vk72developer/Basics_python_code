# Reverse a List in Place 
# Reverse a list in place by swapping elements, without using reverse() or slicing

num = [1, 2, 3, 4, 5]
left = 0
right = len(num) - 1

while left < right:
    num[left], num[right] = num[right], num[left]
    left += 1
    right -= 1

print("Reversed:", num)