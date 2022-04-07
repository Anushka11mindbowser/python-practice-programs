from collections import Counter
lst = [2,4,6,8,10,12,14,16,18,20,4,8,12,16,20,24,28,32,2,6,40]
def occurances(parameter):
    count = 0
    n = int(input("Enter the element you want to count:\n"))
    #traversing the list using for loop
    if n in parameter:
        for i in parameter:
            if i == n:
                count = count + 1
        return count

    else:
        return "Element does not exist"


print(occurances(lst))


def count_occurances(param):
    e = int(input("Enter the element whose occurances you want to count: \n"))
    if e in param:
        return param.count(e)
    else:
        return "Elements does not exist\n"

print(count_occurances(lst))

#Approach Three :
item = int(input("Element: \n"))
counter = Counter(lst)
print(item,counter[item])