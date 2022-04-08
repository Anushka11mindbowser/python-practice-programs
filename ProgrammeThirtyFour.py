#Approach One: Using inbuilt list function
lst = [887, 656, 887, 935, 938]
def sort_lst(listt):
    #Sorting the list
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
    liist = console_input.split(' ')
    sorted_liist = []
    max_value = 0
    for i in liist:
        if i > max_value:
            i = max_value
            sorted_liist.append(i)
            print(sorted_liist)

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
