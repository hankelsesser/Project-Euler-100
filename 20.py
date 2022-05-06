num = 100
fact = num
for i in range(1,num):
    fact *= i

print(fact)
fact = list(str(fact))
num2 = 0
for i in fact:
    num2 += int(i)

print(num2)
