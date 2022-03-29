#Approach One: Using min() value
lst = [9, 65, 383, 43534, 76]

def min_value(list1):
    return min(list1)
print(min_value(lst))

#Approach Two: Using sort function

def using_sort(list1):
    list1.sort()
    return list1[0]
print(using_sort(lst))

#Approach Three: Using comparison

def compare_min(list1):
    min = list1[0]
    for i in list1:
        if i < min:
            min = i
    return min
print(compare_min(lst))

