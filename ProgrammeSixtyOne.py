#Approach One: Using set function

#Declaring dictionaries
my_dict = {'name':'Anushka', 'age':23, 'address':'pune', 'name':'pushkar', 'nick_name':'Anushka'}
print(set(my_dict))

#Approach Two: Returning unique values on basis of values
print(set(my_dict.values()))

#Approach Three: Using loops

#Initializing an empty list to append the results
answer = []
#Traversing the dictionaries using for loops
for val in my_dict.values():
    #Checking if that values is present in the list and if it is present skipping that function and appending unique values to the list
    if val in answer:
        continue
    else:
        answer.append(val)
    #Obtaining only unique value by using set()
print(set(answer))

#Using dictionary comprehensions


res = list(set(val for dic in my_dict for val in my_dict.values()))
print(str(res))