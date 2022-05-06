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


    # for d in range(length):
    #     result[d] = og_num[math.floor((n-1)/math.factorial(length-d-1))]


    result[0]= og_num[math.floor((n-1)/(math.factorial(length-1)))]
    result[1]= og_num[math.floor((n-1)/(math.factorial(length-2)))]

    return (result)


# number = "0123456789"
# n = 1000000

for i in range(1,7):
    print(get_nth_permutation("012",i))