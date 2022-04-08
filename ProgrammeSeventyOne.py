#Program to determine if a given string is a digit or not

#Creating a list with all values that occur in a digit
num = ['1','2','3','4', '5', '6', '7', '8', '9', '.', ',']
#Creating an empty list to append the results
lst = []
#Accepting input from the user
input_char = input("Enter the char\n")
#Using for loop to traverse the string
for i in input_char:
#If that char is present in num
      if i in num:
          lst.append("Digit")
      else:
          lst.append("No Digit")
a = "No Digit"
#Verifying that all values in a list are Digit and if they are not, that string is not a pure digit
if a in lst:
    print("This char is not a digit")
else:
    print("This char is a digit")
    #Converting the string back int
    b = int(input_char)
    print(type(b))
