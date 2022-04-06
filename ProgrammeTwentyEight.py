#Approach One
try:
    lst = []
    input_string = input("Enter the list of words by seperating them with commas: \n")

    lst = input_string.split(",")
    print(lst)
    updated_list = sorted(lst)
    print("Sorted List: ")
    print(updated_list)
except:
    print("Did you enter the input in correct format?\n")