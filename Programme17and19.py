#Approach One:
lst = [95798, 96798, 5454, 86765, 2445]
def difference(list1):
    s = min(list1)
    l = max(list1)
    diff = l - s
    return diff
print(difference(lst))

#Approach Two
def subtract(list1):
    list1.sort()
    s = list1[0]
    l = list1[-1]
    diff = l - s
    return diff
print(subtract(lst))