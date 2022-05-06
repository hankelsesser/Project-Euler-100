import math, time
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number 
# that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def abundant_nums():
    numbers = []
    for x in range(1, 28124):
        #if x%1000==0:print(x) 
        divisors = []
        if x%2==0:
            for i in range(1,math.ceil(x/2)+1):
                if x%i == 0: divisors.append(i)
            
        else:
            for i in range(1,math.floor(x/2)+1, 2):
                if x%i == 0: divisors.append(i)
        sum = 0
        for num in divisors: sum += num
        if sum > x: numbers.append(x)

    return(numbers)

print("getting abundant numbers...")
abundant_numbers = abundant_nums()
print(abundant_numbers)

print("getting abundant sums...")
abundant_sums = []
for i in range(len(abundant_numbers)):
    print(100*(i/len(abundant_numbers)))
    last = 0
    for n in range(len(abundant_numbers)):
        last = n
        sum = abundant_numbers[i]+abundant_numbers[n]
        if sum > 28124:
            print("break:", n)
            break
        if sum not in abundant_sums:
            abundant_sums.append(sum)
    print("last n:", last)

print("getting final list of numbers...")
sum = 0
for x in range(1, 28124):
    if x not in abundant_sums: sum+=x


print("final_answer", sum)





print(abundant_numbers)
