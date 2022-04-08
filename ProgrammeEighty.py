# Function to return a string in camel case format
def camel_case_string(strng):
    # Converting a string into list
    lst = strng.split(" ")
    # Defining an empty list
    res_lst = []
    #Traversing through the list
    for i in lst:
    #Capitalizing the first letter of every word and then joining them into a string
        i = i[0].upper() + i[1:]
        res_lst.append(i)
        #Joining the letters in the list and turning them into one string
    resulting_string = "".join(res_lst)
    #Converting the first letter of the string into lowercase
    resulting_string = resulting_string[0].lower() + resulting_string[1:]

    return resulting_string


print("Camel Case String : " + camel_case_string("Anushka pawar lives In Pune") + ".\n")