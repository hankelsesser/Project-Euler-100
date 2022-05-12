# The decimal number, 585 = 1001001001(sub2) (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)
import math
def get_binary(n):
    num = str(bin(i))
    num = int(num[2::])
    return(num)

def palindrome(i):
    num = str(i)
    if len(num) == 1: return True
    else:
        for i in range(math.floor(len(num)/2)):
            if num[i]!=num[-(i+1)]: return False
        return True

sum = 0
for i in range(0, 1000000):
    if palindrome(i)== True:
        if palindrome(get_binary(i)) == True: sum += i


print(sum)