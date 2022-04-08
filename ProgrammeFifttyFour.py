#Defining a tuple that contains tuples
given_tuple = (('a', 23),('b', 37),('c', 11), ('d',29))
#Sorting the elements of a tuple by the second index

#Function to get the index key
#item specifies the tuples inside the main tuples here
def getKey(item):
    return item[1]

#Sorting the tuple by the index 1 i.e the second element in the tuple
result = sorted(given_tuple, key=getKey)
result = tuple(result)
print(result)