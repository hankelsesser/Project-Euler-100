
def seq_len(n):
    count = 1
    while n != 1:
        count += 1
        if n in cache:
            return count + cache[n]
        n = n//2 if n%2 ==0 else 3*n+1
    return count

longest = {'val':0,'length':0 }
cache = {}
for i in range(3, 1000000):
    print(i)
    chain_len = seq_len(i)
    cache[i] = chain_len
    if chain_len > longest['length']:
        longest["val"]= i
        longest["length"]= chain_len
        print("new longest!")

print(longest)


#{'val': 837799, 'length': 585}
