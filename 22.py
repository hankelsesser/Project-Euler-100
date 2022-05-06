#from string import ascii_letters
import time
start = time.time()
string_ = open("22_names.txt").read()
names = string_.split('","')
names[0], names[-1] = names[0][1::], names[-1][0:-1]

alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_dict = {}
for i in range(1,len(alphabet)+1):
    alpha_dict[alphabet[i-1]] = i

names = sorted(names)

sum = 0

for n in range(len(names)):
    name_sum = 0
    for l in range(len(names[n])):
        name_sum += alpha_dict[names[n][l].lower()]
    sum += name_sum*(n+1)

print(sum)
print(time.time()-start)

