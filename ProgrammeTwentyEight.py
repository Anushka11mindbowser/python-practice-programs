#Approach One
try:
    #Defining the list to append all indivisual words to the list
    lst = []
    input_string = input("Enter the list of words by seperating them with commas: \n")

    #Divinding the elemets in strings into a list
    lst = input_string.split(",")
    print(lst)
    #Sorting the list
    updated_list = sorted(lst)
    print("Sorted List: ")
    print(updated_list)
except:
    print("Did you enter the input in correct format?\n")