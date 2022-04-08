#Approach One:
lst = [95798, 96798, 5454, 86765, 2445]
def difference(list1):
    #Finding out minimum and maximum numbers from the list
    s = min(list1)
    l = max(list1)
    #Calculating the difference between minimum and maximum numbers
    diff = l - s
    return diff
print(difference(lst))

#Approach Two
def subtract(list1):
    #Sorting the list
    list1.sort()
    #In sorted list min number is at the first position and max number is at the last position
    s = list1[0]
    l = list1[-1]
    #Calculating the difference between the max and min
    diff = l - s
    return diff
print(subtract(lst))

#Approach Three: Findin max and min of a list without built-in list methods
def find_max(list):
    max = 0
    for i in list:
        if  i > max:
            max = i
    return max

def find_min(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

a = find_max(lst)
b = find_min(lst)
diff = a - b
print(diff)