import math
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

def get_digits(num):
    digits = list(str(num))
    for i in range(len(digits)): digits[i] = int(digits[i])
    digits = sorted(digits)
    return(digits)

nums = []
for i in range(10,50000):
    if i % 10000==0: print(i)
    digits = get_digits(i)
    sum = 0
    for digit in digits: 
        sum+= math.factorial(digit)
        if sum >i: break
    if sum == i: nums.append(i)

print(nums)
sum = 0
for num in nums: sum+= num
print(sum)