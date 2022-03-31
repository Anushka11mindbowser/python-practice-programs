#Approach One
lst = []
input_string = input("Enter the list of words by seperating them with commas: \n")
lst = input_string.split(",")
print(lst)
updated_list = sorted(lst)
print(updated_list)