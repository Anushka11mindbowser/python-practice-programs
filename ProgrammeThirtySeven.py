#Approach One:
#Creating a list to append all the digits in the phrase
lst1 = []
#Creating a list to append all the alphabets in the phrase
lst2 = []
input_string = input("Enter a phrase: \n")
#Spliting up the words in a phrase into a list
updated_string = input_string.split(" ")
for i in updated_string:
    if i.isdigit():
        lst1.append(i)
    elif i.isalpha():
        lst2.append(i)
    else:
        pass

print(lst1)
print(lst2)

list1 = []
list2 = []
#Same function on strings
def recognize_digits():
    strng = input("Enter a string\n")
    updated_strng = strng.split(" ")
    for i in updated_strng:
        if i.isdigit():
            list1.append(i)

        elif i.isalpha():
            list2.append(i)
        else:
            pass

    return list1,list2
print(recognize_digits())