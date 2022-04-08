#Programme to convert an into into string

#Approach using f-string

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
