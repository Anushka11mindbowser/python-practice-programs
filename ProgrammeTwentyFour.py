#Approach One: Using math library: remainder()
import math
def divide_lib():
    num1 = int(input("Dividend:"))
    num2 = int(input("Divisor:"))
    if num2 != 0:
        if (math.remainder(num1, num2) == 0):
            return True
        else:
            return False
    else:
        return "Divisor cannot be zero!"
print(divide_lib())


#Approach One: Using function

def divide_evenly(a,b):
    if (a%b == 0):
        return True
    else:
        return False

print(divide_evenly(50,4))

