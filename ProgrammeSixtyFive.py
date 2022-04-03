#Approach One: Using codecs library

import codecs
def ascii_to_hex(char):
    hex = codecs.encode(b"char", "hex")
    return hex
print(ascii_to_hex(97))

#Approach Two: Using hex function

def ascii_hex(c):
    ans = hex(c)
    return ans
print(ascii_hex(7667))