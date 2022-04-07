import re
#Approach One: Using replace method
#Programme to replace a word in a phrase

def replace_word():
    input_string = input("Enter a phrase:\n")
    input_word1 = input("Enter the word to be replaced:\n")
    input_word2 = input("Enter the word that you wan to replace with\n")
    if input_word1 in input_string:
        updated_string = input_string.replace(input_word1,input_word2)
        return updated_string
    else:
        return "The word does not exist in the input string\n"

print(replace_word())
#Programme to replace a letter from a word
def replace_alphabet():
    input_word = input("Enter a word\n")
    input_alphabet1 = input("Enter the alphabet you want to replace:\n")
    input_alphabet2 = input("Enter the alphabet you want to replace with:\n")
    if input_alphabet1 in input_word:
        updated_word = input_word.replace(input_alphabet1, input_alphabet2)
        return updated_word
    else:
        return "The letter does not exist!"
print(replace_alphabet())

#Approach 3: Using re library and using sub function

sample_phrase = "Rose for Lilies"
pattern = r'Rose'
replacement = r'Lilies'
updated = re.sub(pattern,replacement,sample_phrase)
print(updated)


