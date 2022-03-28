#Approach One: Using Math library
import math
def remainder_lib(x,y):
  m = math.remainder(27,4)
  return "The remainder is: " + str(m)

print(remainder_lib(27,4))


#Approach Two: Using a function by passing parameters
def remainder(n1, n2):
    rmndr =  n1 % n2;
    return rmndr

print(remainder(11,2))

#Approach Three: Bssic Approach

dividend = int(input("Enter the Dividend: \n"))
divisor = int(input("Enter the divisor: \n"))
remainderr = dividend % divisor
print(remainderr)
