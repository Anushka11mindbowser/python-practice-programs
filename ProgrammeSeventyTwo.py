#Defining a list with all the vowels
vowels = ['a', 'e', 'i', 'o', 'u']
#Defining a list with all the consonants
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
input_char = input("Enter a char: \n")
if input_char.isalpha():
    if input_char.islower():
        if input_char in vowels:
            print(input_char + " is a vowel")
        elif input_char in consonants:
            print(input_char + " is a consonant")
    else:
        print("Enter an alphabet in lowercase")
else:
    print("It is neither a vowel nor a consonant. Please enter a singular alphabet in lowercase\n")



