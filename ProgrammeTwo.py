#Approach One
# Programme to add two numbers, a and b are two arguments that are passed into add function
def add(a, b):
    return a + b

print(add(5, 9))

#Approach Two

a = 5
b = 4
c = a + b;
print(c)

#Approach Three
# a and b are integers to be added
def addition():
    a = int(input("Enter the first number:\n"))
    b = int(input("Enter the second number:\n"))
    if type(a) and type(b) == int:
        c = a + b
        return "The Addition is: " + str(c) + "."
    else:
        return "Invalid Input"


print(addition())

#Approach Four


fnum = int(input("Enter the first number:\n"))
snum = int(input("Enter the second number:\n"))

print(fnum + snum)

