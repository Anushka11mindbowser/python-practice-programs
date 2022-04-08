#Approach One: Basic Approach
a = "76768"
b = int(a)
print(type(b))

#Approach Two: Using function
#We use int()to convert any object into integer
def convert_string(strng):
    return int(strng)

print(type(convert_string("76587679")))

input_string = input("Enter a string: \n")
#Verifying if the given number is in numeric form
if input_string.isdigit():
    #Converting that string into int
    integer_string = int(input_string)
    print(type(integer_string))
else:
    print("Enter numeric value")