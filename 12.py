
import math

def get_factors(num):
    factors = 0
    for i in range(1,int(math.sqrt(math.floor(num))+1)):
        if num%i == 0:
            factors += 2
    if math.sqrt(num) == int(math.sqrt(num)):
        factors -= 1

    return factors


# for i in range(1, 26):
#     factors = get_factors(i)
#     print(i, factors)

value = 0
i = 0
while True:
    i = i +1
    value = value + i
 #   print(i, " : ",value)
    factors = get_factors(value)
    if factors >= 500:
        print(value)
        break
    else: print(value, "only has", factors,"factors!")
    





#76576500