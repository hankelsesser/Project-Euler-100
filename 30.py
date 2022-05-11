# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#notes:
# no single digits numbers work because they will not be sums

def get_digits(num):
    digits = list(str(num))
    for i in range(len(digits)): digits[i] = int(digits[i])
    digits = sorted(digits)
    return(digits)

powers = {}
for i in range(0, 10):
    powers[i] = i**5

#4 digits numbers
nums = []
for i in range(10, 1000000):
    digits = get_digits(i)
    sum = 0
    for digit in digits: 
        sum += powers[digit]
        if sum > i: break
    if sum == i: nums.append(i)

print(nums)
sum = 0
for num in nums: sum+=num
print(sum)
