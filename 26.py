# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def check_recusion(float):
    found = False
    digits = []
    digits = get_more_digits(float, digits, 5)
    while found == False:
        first = digits[0]
        for d in range(1, len(digits)):
            if digits[d] == first:
                if len(digits) < 2*d: digits = get_more_digits(float, digits, 2*d - len(digits))
                for i in range(0, 4):pass


            

                

def get_more_digits(float, digits, num):
    pass

longest = 0
longest_length = 0
for d in range(1000):
    pass

