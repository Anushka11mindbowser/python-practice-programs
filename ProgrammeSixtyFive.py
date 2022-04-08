#Approach One: Using codecs library
#USing codecs.encode methods to change our ascii input into hexadecimal

import codecs
def ascii_to_hex(char):
    try:
#The first parameter in the encode function is for the string that needs to be converted and second parameter is to denote what the string should be converted in
        hex = codecs.encode(b"char", "hex")
        return hex
    except:
        print("Enter a valid ascii value")
print(ascii_to_hex(97))

#Approach Two: Using hex function
#Using hex function

def ascii_hex(c):
    try:
        ans = hex(c)
        return ans
    except:
        print("Enter a valid value")
print(ascii_hex(7667))