#Merging two dictionaries
#Approach One: Uisng pipeline operator

#Defining two different dictionaries
my_dict ={'a':10,'b':20}
your_dict = {'c':30, 'd':40}
def merge_dict(para1, para2):
    result = para1|para2
    return result
print(merge_dict(my_dict,your_dict))

#Approach Two: Using ** operator
#Defining two different dictionaries
dict_1 = {'anushka': 'pawar', 'tom':'jerry'}
dict_2 = {'pushkar': 'pawar', 'oggy': 'cockroaches'}
#Appending the two dictionaries
result_dict = {**dict_1, **dict_2}
print(result_dict)

#Approach Three: Using update method
dict_1.update(dict_2)
print(dict_1)