#Approach One: Using min() value
lst = [9, 65, 383, 43534, 76]

def min_value(list1):
    return min(list1)
print(min_value(lst))

#Approach Two: Using sort function

def using_sort(list1):
    #Sorting the list first and accessing the first element
    list1.sort()
    return list1[0]
print(using_sort(lst))

#Approach Three: Using comparison

def compare_min(list1):
    #Initialize a variable and assign the values of the first element to it
    min = list1[0]
    for i in list1:
        #if any element in the list is less than min, reassign min's value to that element
        if i < min:
            min = i
    return min
print(compare_min(lst))

