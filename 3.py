# largest prime factor of 600,851,475,143

def get_factor(number):
    i = 2
    while True:
        if number % i ==0:
            return i, number/i
        else: i=i+1

def prime(number):
    for i in range(2, int(number/2)):
        if number % i ==0:
            return(False)
    return(True)

prime_fact =[]
factors = [600851475143]
#factors = [13195]
for i in range(1000):
    for i in range(len(factors)):
        if prime(factors[i]) == False:
            factor1, factor2 = get_factor(factors[i])
            factors.remove(factors[i])
            factors.append(factor1)
            factors.append(factor2)
        else: 
            prime_fact.append(factors[i])
print(factors)

