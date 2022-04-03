#Approach One:
lst1 = []
lst2 = []
input_string = input("Enter a phrase: \n")
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