def get_next_fibbonacci(list):
    list.append(list[-1]+list[-2])
    return(list)
fibbo = [1, 1]
while len(str(fibbo[-1])) < 1000:
    print(len(str(fibbo[-1])))
    fibbo = get_next_fibbonacci(fibbo)



print(len(fibbo))


