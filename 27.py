import math
import numbers

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

def is_prime(num):
    num = abs(num)
    for i in range(2,int(math.sqrt(math.floor(num))+1)):
        if num%i == 0:
            return False
    if math.sqrt(num) == int(math.sqrt(num)):
        return False
    else: return True


primes = primes_sieve(1000)

negative_primes = []
for prime in primes:
    print(prime)
    negative_primes.append(prime*-1)

for prime in negative_primes:
    primes.append(prime)

primes = sorted(primes)

#print(primes)

ab_dict = {}

for a in primes:
    print("calculating",(a+1000)/2000)
    for b in primes:
        n = -1
        prime = True
        num = 0
        while prime == True:
            n+=1
            quad = int(n**2 + a*n + b)
            if quad not in primes and is_prime(quad) == False:
                prime = False
            else: num +=1
        else:
            
            ab_dict[str(a*b)] = num

highest = ""
highest_value = 0
for key in ab_dict:
    if abs(ab_dict[key]) > highest_value:
        highest = key
        highest_value = abs(ab_dict[key])

print(highest, highest_value)

# ab_dict = sorted(ab_dict.items(), key=lambda x:x[1])
# print(ab_dict)
