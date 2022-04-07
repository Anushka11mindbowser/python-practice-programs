import string
alphabets_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

input_string = input("Enter a string: \n")




def missing_alphabets(strng):
    if strng.islower():

        res_set = set(alphabets_list).difference(set(strng))
        if len(res_set) == 0:
            return "No Missing Alphabets"
        else:
            res_lst = list(res_set)
            return sorted(res_lst)
    else:
        return "Enter a string in lower case"


print(missing_alphabets(input_string))

def alphabets_missing(strng):
    res_lst = []
    for i in alphabets_list:
        if i not in strng:
            res_lst.append(i)
    return sorted(res_lst)
print(alphabets_missing(input_string))