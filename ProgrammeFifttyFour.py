given_tuple = (('a', 23),('b', 37),('c', 11), ('d',29))
#Sorting the elements of a tuple by the second index
#Function to get the index key
def getKey(item):
    return item[1]


result = sorted(given_tuple, key=getKey)
result = tuple(result)
print(result)