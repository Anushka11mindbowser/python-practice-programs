#Approach One: Basic Approach
a = "76768"
b = int(a)
print(type(b))

#Approach Two: Using function
def convert_string(strng):
    return int(strng)

print(type(convert_string("76587679")))

input_string = input("Enter a string: \n")
if input_string.isdigit():
    integer_string = int(input_string)
    print(type(integer_string))
else:
    print("Enter numeric value")