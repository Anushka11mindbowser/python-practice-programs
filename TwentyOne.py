#Approach One: Using math libraries and remainder()
import math
def divisible_by_five(num):
    if(math.remainder(num,5) == 0):
        return True
    else:
        return False
print(divisible_by_five(67))

#Approach Two: Using module operator
def divisible():
    number = int(input("Enter a number:"))
    if(number % 5 == 0):
        return True
    else:
        return False

print(divisible())