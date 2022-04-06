#Creating a list with all values that occur in a digit
num = ['1','2','3','4', '5', '6', '7', '8', '9', '.', ',']
#Creating an empty list to append the results
lst = []
input_char = input("Enter the char\n")
for i in input_char:
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
    b = int(input_char)
    print(type(b))
