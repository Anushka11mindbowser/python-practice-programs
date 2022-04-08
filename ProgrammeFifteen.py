# Approach One: Using max() function

#Defining two lists
lst = [5, 98, 64576, 9986]
lst1 = ['zebra', 'giraffe', 'camel', 'buffalo', 'horse']


def max_value(llist):
    return max(llist)


print(max_value(lst))
print(max_value(lst1))

# Approach Two: Using sort() function
def using_sort(list1):
    #Sorting the list and accessing the last element
   list1.sort()
   return list1[-1]

print(using_sort(lst))
print(using_sort(lst1))

#Approach Three: Using comparison

def using_comparison(list1):
    #Initializing  a variable
    max = 0
    for i in list1:
        #If the values of an element in the list is greater than max, max gets reassigned to that element
        if i > max:
            max = i
    return max
print(using_comparison(lst))
