def get_digit(digit):
    if digit == 0:
        return""
    elif digit == 1:
        return "one" 
    elif digit == 2:
        return "two"
    elif digit == 3:
        return "three"
    elif digit == 4:
        return "four"
    elif digit == 5:
        return "five"
    elif digit == 6:
        return "six"
    elif digit == 7:
        return "seven"
    elif digit == 8:
        return "eight"
    elif digit == 9:
        return "nine"

def get_teens(teen):
    if teen == 10:
        return "ten"
    elif teen == 11:
        return "eleven"
    elif teen == 12:
        return "tweleve"
    elif teen == 13:
        return "thirteen"
    elif teen == 14:
        return "fourteen"
    elif teen == 15:
        return "fifteen"
    elif teen == 16:
        return "sixteen"
    elif teen == 17:
        return "seventeen"
    elif teen == 18:
        return "eighteen"
    elif teen == 19:
        return "nineteen"

def get_tens(digit):
    if digit == 0:
        return ""
    elif digit == 2:
        return "twenty"
    elif digit == 3:
        return "thirty"
    elif digit == 4:
        return "forty"
    elif digit == 5:
        return "fifty"
    elif digit == 6:
        return "sixty"
    elif digit == 7:
        return "seventy"
    elif digit == 8:
        return "eighty"
    elif digit == 9:
        return "ninety"
   


numbers = ""
for i in range(1, 1001):
    i = str(i)
    number = ""
    if len(i)>3:
        number += "onethousand"
    if len(i)>2:
        number+=get_digit(int(i[-3]))
        if i[-3] != "0":
            if i[-2:] =="00":
                number+="hundred"
            else:
                number+="hundredand"
    if len(i)>1:
        if i[-2] == "1":
            number+=get_teens(int(i[-2:]))
        else:
            number+=get_tens(int(i[-2]))
            number+=get_digit(int(i[-1]))
    if len(i)==1:
        number+=get_digit(int(i))
    numbers+=number

print(numbers)
print(len(numbers)-10)


