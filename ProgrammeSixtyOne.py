#Approach One: Using set function
my_dict = {'name':'Anushka', 'age':23, 'address':'pune', 'name':'pushkar', 'nick_name':'Anushka'}
print(set(my_dict))

#Approach Two: Returning unique values on basis of values
print(set(my_dict.values()))

#Approach Three: Using loops
answer = []
for val in my_dict.values():
    if val in answer:
        continue
    else:
        answer.append(val)
print(set(answer))

#Using dictionary comprehensions


res = list(set(val for dic in my_dict for val in my_dict.values()))
print(str(res))