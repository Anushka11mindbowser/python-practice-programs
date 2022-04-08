#Turning a list into dictionary

#Approach One: Using zip and iter objects

#Defining a list
lst = [89, 'milk', True, 65.5, 55, 'Tom']

def convert_dict(param):
    #Using an iterator to traverse the list
    i = iter(param)
    # Appending two elements togather using zip(), and then converting it into dict
    res_dict = dict(zip(i,i))
    return res_dict
print(convert_dict(lst))


#Approach Two: Using dictionary comprehension
def dict_convert(param):
    #Appending two consecutive items in the list
    res_dict = {param[i]:param[i+1] for i in range(0,len(lst),2)}
    return res_dict
print(dict_convert(lst))

#Replacing a key
#Approach One : Using predefined variable

#Defining a dictionary
dict = {'a': 1, 'b':4, 'c' : 7, 'd' : 9}
new_key = 'f'
old_key = 'd'
#Replacing the old key with new key
dict[new_key] = dict.pop(old_key)
print(dict)

#Approach Two: directly specifying the key
new1_key = 'g'

dict[new1_key] = dict.pop('c')
print(dict)
