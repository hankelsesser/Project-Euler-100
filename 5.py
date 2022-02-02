# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

import math
for i in range(20, math.factorial(20), 20):
    possible = True
    for n in [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]:
        if possible == True:
            if i%n != 0:
                possible = False
                print(i, ":      false")
    if possible == True:
        print(i)
        break


#232792560