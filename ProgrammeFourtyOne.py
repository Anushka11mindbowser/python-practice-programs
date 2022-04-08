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
    #Declaring an empty string to concatenate our result to it
    stringg = ""
    #Using for loop
    for i in string4:
        stringg = i + stringg
    return stringg

print(reversing("Paris"))

#Approach Four: Using while loop
def reversify(s):
    #Defining an empty string to store the result
    s1 = ""
    #Determining the lenghth of the word to be reversed
    l = len(s) - 1
    #using while loop to check the length after every iteration
    while l >= 0:
        #Concatenantiong the element at a parrticular index to the resulting string
        s1 = s1 + s[l]
        l -= 1
    return s1
print(reversify("Anushka"))