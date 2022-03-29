#Approach One: Using itertools library

import itertools


list_a = ['paris', 'tokyo', 'london', 'berlin', 'new york']
list_b = ['austin', 'jakarta', 'jaipur', 'oslo', 'pune']

def combine_with_libs(lst1, lst2):
    result_list = list(itertools.chain(lst1, lst2))
    return result_list
print(combine_with_libs(list_a,list_b))


#Approach Two: Using + operator


def combine_list(lst1, lst2):
    return lst1 + lst2

print(combine_list(list_a, list_b))

#Approach Three: Using slice method
def combined_list(lst1, lst2):
    list1 = lst1[0:]
    list2 = lst2[0:]
    return list1 + list2
print(combined_list(list_a, list_b))

#Approach Four: Using extend

def using_extend(lst1, lst2):
    lst1.extend(lst2)
    return lst1
print(using_extend(list_a, list_b))

#Approach Five: using append function

def using_append(lst1, lst2):
    lst1.append(lst2)
    return lst1
print(using_append(list_a, list_b))

#Approach Six: Using * operator

def using_star(lst1, lst2):
    resulting_list = [*lst1,*lst2]
    return resulting_list
print(using_star(list_a,list_b))

#Approach Seven: Using list comprehension
def list_comprehded(lst1, lst2):
     res = [y for x in [lst1, lst2] for y in x]
     return res
print(list_a, list_b)