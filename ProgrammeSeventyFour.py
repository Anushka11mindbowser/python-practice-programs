#Approach One:
#Creating a list of all digits
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#Creating an empty list to append the result strings
result_lst = []
#Accepting a list as input from the console
lst = []
try:
    n = int(input("Enter the number of elements you want to add: \n"))
    for i in range(0, n):
        element = input("Enter the element: \n")
        lst.append(element)
except:
    print("Enter a numeric value")

#Function to check if a string has a digit in it
def strings_with_digits(param):
    #First we traverse through the list
    for j in param:
    #Then we traverse through the indivisual elements
        for k in j:
            if k in num:
                result_lst.append(j)
                #Applying break to stop the loop as soon as a digit is encountered
                break
            else:
                pass

    return result_lst



print(strings_with_digits(lst))





