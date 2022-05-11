
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?
import math
def prime(num):
    for i in range(2,int(math.sqrt(math.floor(num))+1)):
        if num%i == 0:
            return False
    if math.sqrt(num) == int(math.sqrt(num)):
        return False
    else: return True

def insert(string, index, character):
    return(string[0:index]+character+string[index::])

def get_permutations(n):
    nums = []
    n = str(n)
    for i in range(len(n)):
        insert
    current = n
    start = True
    while 1:
        if start == False and current == n: break
        start = False
        current = insert(current, 0, current[-1])
        current = current[:-1]
        nums.append(int(current))
    return(nums)

def circular(arrangements):
    for i in range(len(arrangements)-1):
        if prime(arrangements[i]) == False: return False
    return True


circlular_primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
#circlular_primes = []

for i in range(100, 1000000):
    if "2" not in str(i) and "4" not in str(i) and "6" not in str(i) and "8" not in str(i) and "0" not in str(i):
        if i not in circlular_primes:
            if prime(i) == True:
                arrangements = get_permutations(i)
                if circular(arrangements) == True: 
                    for num in arrangements: circlular_primes.append(num)


print(circlular_primes)
print(len(circlular_primes))
            
            
            