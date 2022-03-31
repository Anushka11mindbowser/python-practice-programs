#Approach: Using slice method

sample_tuple = (8,4,20,16,12)
print(sample_tuple[::-1])

#Approach Two: Using reversed method

def reversed_tuple(parameter):
    rt = tuple(reversed(sample_tuple))
    return rt
print(reversed_tuple(sample_tuple))

#Approach 3: Accepting elements from console
lst = []
def tuple_reversed():
    en = int(input("Enter the number of elements in your tuple"))
    for i in range(0,en):
        ele = input("Enter the element:\n")
        lst.append(ele)
    my_tuple = tuple(lst[::-1])
    return my_tuple
print(tuple_reversed())
