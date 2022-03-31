#Approach One: Using inbuilt function

def compare_string(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str2) > len(str1):
        return str2
    else:
       print(str1)
       print(str2)

print(compare_string('Anushka', 'Pushkar'))

