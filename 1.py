def multiplesOf3and5(number):
    numbers = []
    for i in range(1,number):
      if i % 3 == 0:
        numbers.append(i)
      elif i % 5 == 0:
        numbers.append(i)
    value = 0
    for number in numbers:
      print(number)
      value = value + number
  
    return value
  
print(multiplesOf3and5(1000))
