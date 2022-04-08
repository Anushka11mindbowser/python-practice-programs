#Defining a list with elements
list1 = ['a','b','c','d','e','f','g','h','i','j']

#accepting an input from the list
input_string = input("Enter a string\n")
#Checking if the elements of string are present in the list
def cut_out_char(lst, str):
    for i in str:
        if i in lst:
            #Removing those lists from the elements
            lst.remove(i)
        else:
            print("Element not present in the list.\n")
            break
    return lst
print(cut_out_char(list1,input_string))

