import string

#Declaring  a list that contains all the elements that are valid to be considered as alphabetic letters
alphabets_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Accepting input from the user
input_string = input("Enter a string: \n")



#Approach One: Converting the list into set to find the difference
def missing_alphabets(strng):
    #verifying the letter in input string are in lowercase
    if strng.islower():
        #converting lists into sets to applying difference() to find the missing alphabets
        res_set = set(alphabets_list).difference(set(strng))
        #Incase there are no missing alphabets
        if len(res_set) == 0:
            return "No Missing Alphabets"
        else:
            #Incase there are missing alphabets
            res_lst = list(res_set)
            #Returning the result in sorted forat
            return sorted(res_lst)
    else:
        return "Enter a string in lower case"


print(missing_alphabets(input_string))

#Approach Two: Using for loop and traversing both the lists
def alphabets_missing(strng):
    #Initializing an empty list to append the missing alphabets
    res_lst = []
    #Traversing through alphabets list
    for i in alphabets_list:
      #Incase a letter from alphabet list is not present in the string
        if i not in strng:
            #Appenf that letter to the resulting list
            res_lst.append(i)
          #Return the sorted list
        return sorted(res_lst)
    else:
        return "No Missing Alphabets"
print(alphabets_missing(input_string))