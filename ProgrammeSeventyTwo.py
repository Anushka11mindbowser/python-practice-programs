vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
input_char = input("Enter a char: \n")
if type(input_char) == str:
    if input_char in vowels:
        print("It is a vowel")
    elif input_char in consonants:
        print("It is a consonant")
    else:
        print("It is neither a vowel nor a consonant")

