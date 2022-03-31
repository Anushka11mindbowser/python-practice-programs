#Approach One: Using set function and entering elements manually
input_string = input("Enter the list elements")
lst = input_string.split(" ")
updated_lst = set(lst)
print(updated_lst)

#Approach Two: Taking user from input
lst1 = []
def unique_list():
    #n = int(input("Enter the number of elements:\n"))
    for i in range(0,25):
        number = input("Enter the element: \n")
        lst1.append(number)
    return list(set(lst1))
print(unique_list())

#Approach Three: Using dict method
lst2 = []
def list_unique():
    for i in range(0,25):
        num = input("Enter an element")
        lst2.append(num)
    return list(dict.fromkeys(lst2))
print(list_unique())

#Approach Four: For Loops and If loops
lst3 = []
lst4 = []
def using_loop():
    for i in range(0,25):
        n = input("Enter element: \n")
        lst3.append(n)
    for j in lst3:
        if j in lst3:
            if j not in lst4:
                lst4.append(j)
    return lst4
print(using_loop())
