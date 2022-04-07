import string
alphabets_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

input_string = input("Enter a string: \n")



#Approach One: Converting the list into set to find the difference
def missing_alphabets(strng):
    if strng.islower():
        #applying difference methods on sets to find the missing alphabets
        res_set = set(alphabets_list).difference(set(strng))
        if len(res_set) == 0:
            return "No Missing Alphabets"
        else:
            res_lst = list(res_set)
            return sorted(res_lst)
    else:
        return "Enter a string in lower case"


print(missing_alphabets(input_string))

#Approach Two: Using for loop and traversing both the lists
def alphabets_missing(strng):
    #Initializing an empty list to append the missing alphabets
    res_lst = []
    for i in alphabets_list:
        if i not in strng:
            res_lst.append(i)
        return sorted(res_lst)
    else:
        return "No Missing Alphabets"
print(alphabets_missing(input_string))