# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


#work:
#indexes of spiral: 0, 2, 4, 6, 8, 12, 16, 21, 25
#length of layers: 1, 9, 25, 47 : 1^2, 3^2, 5^2, 7^2
#differences of corners per layer: 2, 4, 

sum  = 0
diags = [1]
interval = 0
last = 1
while last < 1002001:
    interval = interval+2
    for n in range(0,4):
        last = last + interval
        diags.append(last)

print(diags)

for diag in diags: sum += diag
print(sum)

