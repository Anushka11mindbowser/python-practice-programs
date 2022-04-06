import string
strng = "fytfugjhbj"
start = strng[0]
end = strng[-1]
input_letters = strng
all_letters = string.ascii_letters

def missing_alphabets(all,input):
    a = range(ord(strng[0]), ord(strng[-1]))



print(missing_alphabets(input_letters, all_letters))
