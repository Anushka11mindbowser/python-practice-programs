#Approach One : Using inbuilt set functions
#Finding out common elements in two sets

#Defining two sets
set1 = {2, 4, 6, 8, 10}
set2 = {5,10,15,20,25}

#initializing an empty set to store the result
result = {}

#Finding common elements in two sets using intersection function
result = set1.intersection(set2)
print(result)


#Approach Two: Using nested loops

#Initializing an empty list to append the values
answer = []

#Defining two different sets
set3 = {1,3,5,7,9}
set4 = {2,3,5,7,11}

#Traversing both sets simultaneously using for loop
for i in set3:
    for j in set4:
        if i == j:
            #Appending the same values to the resulting list
            answer.append(j)
            #Converting that list to set using set() and printing it
print(set(answer))

