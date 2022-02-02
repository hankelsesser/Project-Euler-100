#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import math
def prime(num):
    for i in range(2,int(math.sqrt(math.floor(num))+1)):
        if num%i == 0:
            return False
    if math.sqrt(num) == int(math.sqrt(num)):
        return False
    else: return True



primes = [2]
n = 1
while n < 2000000:
    print(n)
    if prime(n)==True:
        primes.append(n)
    n = n + 2


value=0
for prime in primes:
    value = value +prime

print(value)
print(primes[0:10])