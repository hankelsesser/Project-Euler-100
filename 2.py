
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

even_fib_num = []
fibnumbers = [1, 2]
for i in range(2,1000):
    fibnumbers.append(fibnumbers[i-1]+fibnumbers[i-2])
    if fibnumbers[-1] > 4000000:
        break
for num in fibnumbers:
    if even(num) == True:
        even_fib_num.append(num)
value = 0
for num in even_fib_num:
    value = value + num

print(value)


