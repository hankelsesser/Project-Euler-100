#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

val1= 0
val2 = 0
for i in range(1, 101):
    val1 = val1+i
    val2 = val2 + i*i

val1 = val1*val1

print(val1-val2 )