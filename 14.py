
def is_even(number):
    if number % 2 == 0:
        return(True)
    else: return(False)


chains = []
i = 13
for i in range(13, 1000000):
    if i % 10000 == 0:
        print(i)
    length = 0
    chain = [i]
    while chain[-1] != 1:
        if is_even(chain[-1]) == True:
            chain.append(int(chain[-1]/2))
        else:
            chain.append(3*chain[-1]+1)
    chains.append(chain)
    #print(chain)
    i = i +1

longest_chain = 0
longest_length = 0
for chain in chains:
    if len(chain) > longest_length:
        longest_length = len(chain)
        longest_chain = chain[0]

print(longest_chain)


#837799