#Function to perform left rotation on a string

def left_rotation(strng):
    # Defining a list and appending the string to that list
    res_lst = [strng]
    #Appending the first letter of the string at the end of the string
    for i in range(0,len(strng)):
      resulting_string = strng[1:] + strng[0]
    res_lst.append(resulting_string)
    #Carrying out the rotation on the remaining string and appending it to the list
    for j in range(0, len(strng)-2):
        resulting_string = resulting_string[1:] + resulting_string[0]
        res_lst.append(resulting_string)

    return res_lst
print("Left Rotation for Pushkar: " + str(left_rotation("Pushkar")) + ".\n")

def right_rotation(strng):
    #Defining a list and appending the string to that list
    res_lst = [strng]
    #Appending the last letter of the string to the starting of the string
    resulting_string = strng[-1] + strng[0:-1]
    res_lst.append(resulting_string)
    #Carrying out the right rotation for the rest of the string
    for i in range(0,len(strng)-2):
        resulting_string = resulting_string[-1] + resulting_string[0:-1]
        res_lst.append(resulting_string)
    return res_lst
print("Right Rotation for Anushka: " + str(right_rotation("Anushka")) + ".\n")