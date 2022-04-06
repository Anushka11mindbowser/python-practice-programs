#Approach One: Using inbuilt list function
lst = [887, 656, 887, 935, 938]
def sort_lst(listt):
    listt.sort()
    return listt
print(sort_lst(lst))

def sort_lst_reverse(listt):
    listt.reverse()
    return listt
print(sort_lst_reverse(lst))

#Approach Two: Using split function
try:
    console_input = input("Enter the elements by seperating them by space\n")
    if console_input.isdigit():
        liist = console_input.split(' ')
        print(liist)
    else:
        print("Invalid Input")
except:
    print("Wrong input")

def input_lst(lllist):
    updated_l = sorted(lllist)
    return updated_l
print(input_lst(lst))

def lst_input(lllist):
    updated_l = sorted(lllist)
    return updated_l
print(input(lst))
