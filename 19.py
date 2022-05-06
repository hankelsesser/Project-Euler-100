
def febu(year):
    if year % 4 == 0:
        if year/100 == round(year/100):
            if year %400 == 0: 
                #print("TRUE", year)
                return(29)
        #print("TRUE", year)
        return(29)
    #print("FALSE", year)
    return(28)
def get_months(year):
    months = {
        1: 31,
        2: febu(year),
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return (months)

sundays = 0
year = 1901
day = 366 # day%7 == 6

while year < 2001:
    #print(day, year)
    #print(year, day)
    months = get_months(year)
    for i in range(1, 13):
        print(i, year, day%7)
        if day%7 == 0: 
            sundays += 1
            #print(year, day)
        day += months[i]
    year += 1

print(year)
print(sundays)



