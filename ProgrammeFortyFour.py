#Programme to pick number form odd indexed elements in list1 and evenly indexed elements from list2 and append them in one list

#Appproach One: Using index method


#Initializing empty list to store the result from first function
lst =[]

#Initializing empty list to store the result from second function
new_lst = []

#Defining two lists with elements in it
lst1 = [2,4,6,8,10]
lst2 = [4,8,12,16,20]

def odd_even_list(para1, para2):
    #Using for loop to traverse lst1
    for i in lst1:
        #Checking if the index is odd
        if lst1.index(i) % 2 != 0:
            #Appending the value to resulting list
            lst.append(i)

    #Using for loop to traverse the lst2
    for j in lst2:
        #Checking if the index is even
        if lst2.index(j) % 2 == 0:
            #Appending the element to resulting list
            lst.append(j)
    return lst
print(odd_even_list(lst1,lst2))


#Approach two: Using range method
def even_odd_list(p1,p2):
        #Traversing the lst1 using for loop and range()
    for i in range(0,len(p1)):
        #Checking if the index is odd
        if i % 2 != 0:
            #Appending the element to the resulting list
            new_lst.append(p1[i])

    #Traversing the list using for loop and range()
    for j in range(0,len(p2)):
        #Checking id=f the index is even
        if j % 2 == 0:
            #Appending the element to the resulting list
            new_lst.append(p2[j])

    return new_lst

print(even_odd_list(lst1,lst2))