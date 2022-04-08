#Approach One:
#Creating a list to append all the digits in the phrase
lst1 = []
#Creating a list to append all the alphabets in the phrase
lst2 = []
input_string = input("Enter a phrase: \n")
#Spliting up the words in a phrase into a list
updated_string = input_string.split(" ")
for i in updated_string:
    #Checking if word is numeric
    if i.isdigit():
        lst1.append(i)
    #Checking if the word is alphabetic
    elif i.isalpha():
        lst2.append(i)
    else:
        pass

print(lst1)
print(lst2)

#Initializing two different listsu
list1 = []
list2 = []
#Same function on strings
def recognize_digits():
    strng = input("Enter a string\n")
    #Splitting up words in strings into a list
    updated_strng = strng.split(" ")
    for i in updated_strng:
    #Checking if the word is numeric
        if i.isdigit():
            list1.append(i)
    #Checking if the word is alphabetic
        elif i.isalpha():
            list2.append(i)
        else:
            pass

    return list1,list2
print(recognize_digits())