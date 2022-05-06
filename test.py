
nums = "1234567890"
nums2 = "0987654321"

help = []
help2 = []
for num in nums:
    print("num",num)
    for num2 in nums2:
        print("num2", num2)
        sum = int(num)+int(num2)
        help2.append(sum)
        if sum > 8: 
            print("break")
            break
        else: help.append(sum)
        


print(help)
print(help2)
