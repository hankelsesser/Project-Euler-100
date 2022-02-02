#largest palindrome made from the product of two 3-digit numbers
def palindrome(number):
    disect = [int(i) for i in str(number)]
    for i in range(len(disect)):
        if disect[i] != disect[-i-1]:
            #print(disect[i], disect[-i-1])
            return(False)
    return(True)


def get():
    _list = []
    for i in range(999,99, -1):
        for n in range(999, 99, -1):
            if palindrome(i*n)==True:
                _list.append(i*n)
    _list.sort()
    print(_list[-1])

get()