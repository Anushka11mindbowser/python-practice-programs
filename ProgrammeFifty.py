#Approach One:
#Printing element of two lists by same index

lst1 = [4,8,12,16,20]
lst2 = [5,10,15,20,25]
#Traversing both strings at the same time
for i in lst1:
    for j in lst2:
        #Printing both indexes
        print(i,j)