# Check if a List is sorted 
# check whether a list is sorted in non - decreasing order.

def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False 
        return True 

print(is_sorted([1, 3, 5, 7])) 
print(is_sorted([4, 2, 9])) 
        