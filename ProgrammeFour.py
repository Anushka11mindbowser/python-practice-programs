#Approach One: Using Math library
import math
def remainder_lib(x,y):
    if y !=0:
        m = math.remainder(27,4)
    return "The remainder is: " + str(m)

print(remainder_lib(27,4))


#Approach Two: Using a function by passing parameters
def remainder(n1, n2):
    if n2 != 0:
        rmndr =  n1 % n2;
        return rmndr
    else:
        return "Cannot divide by zero"

print(remainder(11,2))

#Approach Three: Bssic Approach
try:
    dividend = int(input("Enter the Dividend: \n"))
    divisor = int(input("Enter the divisor: \n"))
    remainder1 = dividend % divisor
except:
    print("Divisor cannot be zero")
print(remainder1)
