#Approach One: Using for loop

lst = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23, 1, 12,88,7,6,2]
#Defining an empty list to store the result
dupli_lst = []

def find_duplicates(element):
    for i in element:
        if element.count(i) > 1:
            dupli_lst.append(i)
    return list(set(dupli_lst))
print(find_duplicates(lst))

