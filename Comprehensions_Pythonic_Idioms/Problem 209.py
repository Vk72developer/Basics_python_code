# Swap Min and Max in a List (one - Liner)

nums = [3, 9, 1, 7, 5]

print("Before:", nums)

i, j = nums.index(min(nums)), nums.index(max(nums))
nums[i], nums[j] = nums[j], nums[i] 

print("After:", nums)