# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 

# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210 

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import math

def get_nth_permutation(og_num, n):
    length = len(og_num)
    result = []
    for i in range(length): result.append("X")

    possible_charcters = []
    for num in og_num: possible_charcters.append(num)

    prev_index = 0
    for d in range(length):
        n -= int(prev_index) * math.factorial(length-d)
        digit = possible_charcters[math.floor((n-1)/(math.factorial(length-(d+1))))]
        prev_index = possible_charcters.index(digit)
        possible_charcters.remove(digit)
        result[d] = digit

    result_str = ""
    for letter in result: result_str += letter
    return (result_str)


number = "01234567"
n = 823

print(get_nth_permutation(number, n))

# number = "01234"
# for i in range(1,math.factorial(len(number))+1):
#     print(get_nth_permutation(number,i))
#     #get_nth_permutation("0123", i)
