#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.



#special triangle: 8:15:17, 8+15+17 = 40, 1000/40 = 25
for i in range(100): 
    a = 8
    b = 15
    c = 17
    a = a*i
    b = b*i
    c = c*i
    if a+b+c == 1000:
        print(a*b*c)
        break
