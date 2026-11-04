# Function Returning Multiple Values

def  min_max(nums):
    return  min(nums), max(nums) 


low, high = min_max([4, 1, 9, 6])

print("Min:", low)
print("Max:", high)
print(min_max([4, 1, 9, 6]))