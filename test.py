import math
nums = "1234567890"
nums2 = "0987654321"

for i in range(math.floor(len(nums)/2)):
    print(i, nums[i])
    print(i-1, nums[i-1])
