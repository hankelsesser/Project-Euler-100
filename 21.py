import math
def d(x):
    print("loading...")
    divisors = []
    if x%2==0:
        for i in range(1,math.ceil(x/2)+1):
            if x%i == 0: divisors.append(i)
        
    else:
        for i in range(1,math.floor(x/2)+1, 2):
            if x%i == 0: divisors.append(i)
    
    sum = 0
    for num in divisors: sum += num
    return(sum)
for i in range(10): print('')
print("creating...")
proper_divisors_dict = {}
for i in range(10001):
    proper_divisors_dict[i] = d(i)

for i in range(10): print('')
print("matching...")
pairs = []
for key in proper_divisors_dict:
    if proper_divisors_dict[key] in proper_divisors_dict and proper_divisors_dict[key] != key:
        if proper_divisors_dict[proper_divisors_dict[key]] == key: pairs.append([key, proper_divisors_dict[key]])

    # for each in proper_divisors_dict:
    #     if each != key and [key, each] not in pairs and [each, key] not in pairs:
    #         if proper_divisors_dict[key] == each and proper_divisors_dict[each] == key:
    #             pairs.append([key, each])
        
        #     if proper_divisors_dict[each] == proper_divisors_dict[key]:
        #         pairs.append([key, each])

print(pairs)
sum = 0
for thing in pairs:
    for pair in thing:
        sum += pair
print(round(sum/2))
