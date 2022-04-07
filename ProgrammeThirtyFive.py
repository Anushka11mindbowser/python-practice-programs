#Approach One: Using inbuilt function
#using len method
def compare_string(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str2) > len(str1):
        return str2
    else:
       return str1, str2

print(compare_string('Anushka', 'Pushkar'))

#Using for loop and counting the number of characters in each string and then comparing the counts
def string_compare(str1, str2):
    count1 = 0
    count2 = 0
    for i in str1:
        count1 += 1
    for j in str2:
        count2 += 1
    if count1 > count2:
        return str1
    elif count2> count1:
        return str2
    else:
        return str1, str2

print(string_compare('Anushka', 'Pawar'))