#Defining the list
lst = [1,2,3,4,5,7,9,11]
#Function to find the missing numbers in the list and return its sum
def missing_numbers(list1):
    #Assigning the starting and ending range
    start = lst[0]
    end = lst[-1]
    a = range(start,end+1)
    #Finding out the missing elements by using difference method, thus converting list into set
    result = set(a).difference(set(list1))
    return sum(result)
print(missing_numbers(lst))