alpha = "abcdefgh"
print(len(alpha))


string = ""

for l in range(len(alpha)):
    string += "+ "+str(alpha[l])+"* (domain[1])**"+str(len(alpha)-1-l)


print(string)

