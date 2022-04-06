#Approach One:
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result_lst = []
lst = []
n = int(input("Enter the number of elements you want to add: \n"))
for i in range(0, n):
    element = input("Enter the element: \n")
    lst.append(element)
def strings_with_digits(param):
    for j in param:
        for k in j:
            if k in num:
                result_lst.append(j)
                break
            else:
                pass

    return result_lst



print(strings_with_digits(lst))





