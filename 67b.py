
pyramid = open("67_triangle.txt").readlines()

for s in range(len(pyramid)):
    if s != len(pyramid)-1: pyramid[s] = pyramid[s][0:-1] #get rid of /n
    pyramid[s] = pyramid[s].split(" ") #split into individual

for row in pyramid: 
    for num in range(len(row)): row[num] = int(row[num])

#print(pyramid)

for row in reversed(range(0, len(pyramid)-1)):
    for num in range(len(pyramid[row])):
        if pyramid[row][num] + pyramid[row+1][num] > pyramid[row][num] + pyramid[row+1][num+1]:
            pyramid[row][num] += pyramid[row+1][num]
        else:pyramid[row][num] += pyramid[row+1][num+1]
#print(pyramid)
print(pyramid[0])

    
