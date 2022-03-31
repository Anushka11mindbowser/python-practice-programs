#Approach One: Using pop method
lst = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23, 1 ]
list1 = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23, 1 ]
list2 = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23, 1 ]
def remove_items(listt):
    (listt.pop(0))
    (listt.pop(3))
    (listt.pop(3))
    return listt

print(remove_items(lst))

#Approach Two: Deleting by accessing the values

def items_removed(listt):
    del listt[0:1]
    del listt[3:5]
    return listt

print(items_removed(list1))

def del_items(listt):
    listt.remove(12)
    listt.remove(88)
    listt.remove(120)
    return listt
print(del_items(list2))


