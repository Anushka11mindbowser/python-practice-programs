#Programme to count uppercase, lowercase, alphabets, digits in a phrase/string
#Initializing variables to count each components
digit = 0
alphabet = 0
upper = 0
lower = 0
input_string = input("Enter a phrase/string\n")

for i in input_string:
    #Checking if the character in string is alphabetic
    if i.isalpha():
        alphabet += 1
        #Checking if the alphabet in the string is in Uppercase
        if i.isupper():
            upper += 1
        #Checking if the alphabet in the string is in lowercase
        elif i.islower():
            lower += 1
    #Checking if the character in the string is numeric
    elif i.isdigit():
        digit += 1
    else:
        pass
print("Digits:" + str(digit))
print("Alphabets: " + str(alphabet))
print("Upper: " + str(upper))
print("Lower: " + str(lower))
