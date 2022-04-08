#Programme to count occurances of an element in the list

#Importing Counter library
from collections import Counter

#Defining a list
lst = [2,4,6,8,10,12,14,16,18,20,4,8,12,16,20,24,28,32,2,6,40]

#Approach One: Using count variable
def occurances(parameter):
    #Initializing a variable which will keep count of a particular variable
    count = 0

    #Taking input from user
    n = int(input("Enter the element you want to count:\n"))
    #Checking if the input element exists in the list
    if n in parameter:
#Using for loop to travrse the list, compare the value with input, and increment counter by one whenever that elements occurs in the list
        for i in parameter:
            if i == n:
                count = count + 1
        return count

    else:
        return "Element does not exist"


print(occurances(lst))

#Approach Two: Using count()
def count_occurances(param):
    #Taking input from the user
    e = int(input("Enter the element whose occurances you want to count: \n"))
    #Using count(), whenver the element occurs in the list
    if e in param:
        return param.count(e)
    else:
        return "Elements does not exist\n"

print(count_occurances(lst))

#Approach Three : Using Counter module
item = int(input("Element: \n"))
#Counter method determines which object to look into for counting an element
counter = Counter(lst)
#Specifying the item to be counted
print(item,counter[item])