#Approach One: Using int()

input1 = input("Enter a string to convert it into an int\n")
int(input1)
print(type(input1))

distance = 45
print(type(distance))
str(distance)
print(type(distance))

#Approach Two: Using f-string

sample_number = 67576
print(type(f'{sample_number}'))

#Approach using "%s"

number1 = 878767
updated_number1 = "%s" %number1
print(type(updated_number1))

#Approach using format function
number2 = 8743698547
updated_number2 = '{}'.format(number2)
print(type(updated_number2))
