#Approach One: Using for loop

def repeat_string(strng, n):
    i=0
    for i in range(n):
        print(strng)
        i += 1
    return "Else."
print(repeat_string("Anushka", 5))

#Approach Two: using while loop

def use_while(strng, n):
    i = 0;
    while (i < n):
        print(strng)
        i += 1
    return "Done!"
print(use_while('Paris', 11))

#Approach Three: using * operator
def use_operator(strng,n):
    return strng * n
print(use_operator("Paris\n",5))

