given_tuple = (('a', 23),('b', 37),('c', 11), ('d',29))

def getKey(item):
    return item[1]

result = sorted(given_tuple, key=getKey)
result = tuple(result)
print(result)