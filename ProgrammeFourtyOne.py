#Approach One: Using slice method
strng = input("Enter a string of your choice:\n")


print(strng[::-1])
#Approach Two: Using join and reversed method
def reverse_function(string3):
    string3 = "".join(reversed(string3))
    return string3
print(reverse_function("Anushka"))

#Approach Three: Using for loop
def reversing(string4):
    stringg = ""
    for i in string4:
        stringg = i + stringg
    return stringg

print(reversing("Paris"))