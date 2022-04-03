#Approach One:
lst = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23, 1, 12,88,7,6,2]
dupli_lst = []

def find_duplicates(parameter):
    for i in parameter:
        if parameter.count(i) > 1:
            dupli_lst.append(i)
    return list(set(dupli_lst))
print(find_duplicates(lst))

