# Approach One: Using max() function
lst = [5, 98, 64576, 9986]
lst1 = ['zebra', 'giraffe', 'camel', 'buffalo', 'horse']


def max_value(llist):
    return max(llist)


print(max_value(lst))
print(max_value(lst1))

# Approach Two: Using sort() function
def using_sort(list1):
   list1.sort()
   return list1[-1]

print(using_sort(lst))
print(using_sort(lst1))

#Approach Three: Using comparison

def using_comparison(list1):
    max = 0
    for i in list1:
        if i > max:
            max = i
    return max
print(using_comparison(lst))
