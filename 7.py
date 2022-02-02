#What is the 10 001st prime number?

def prime(number):
    for i in range(2, int(number/2)):
        if number % i ==0:
            return(False)
    return(True)

primes = []
n = 1
while len(primes) < 10003:
    if prime(n) == True:
        primes.append(n)
    n=n+1

print(primes)


#104743