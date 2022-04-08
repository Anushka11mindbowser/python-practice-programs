#programme to calculate the length of the string

def string_length():
    #Initializing the counter to keep count of the characters in the string
    count = 0
    #taking user input from the console
    strng = input("Enter a string: \n")
    #Traversing the string with the help of for loop
    for i in strng:
        #Incremeting the count whenever a character is encountered
        count += 1
    return count
print("The length of string is: " + str(string_length()))


