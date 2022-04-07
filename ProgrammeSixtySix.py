def string_length():
    count = 0
    strng = input("Enter a string: \n")
    for i in strng:
        count += 1
    return count
print("The length of string is: " + str(string_length()))


