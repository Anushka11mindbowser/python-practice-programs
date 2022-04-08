#Approach One:
#Programme to sum up all the elements in the list
lst = [7, 9, 34, 56, 100]

def lst_sum(list1):
    #Initializing count variable to store the sum of all elements
    count = 0
    for i in list1:
        count += i
    return count

print(lst_sum(lst))

#Approach Two: Using inbuilt list method: sum()

def func_three(list2):
    total = sum(list2)
    return total
print(func_three(lst))


#Approach Three: Using while loop
def sum_lst(list3):
    counter = 0
    k = 0
    while (k < len(list3)):
        counter = counter + list3[k]
        k += 1
    return counter

print(sum_lst(lst))
