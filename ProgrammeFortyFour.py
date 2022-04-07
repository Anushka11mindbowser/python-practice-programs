#Programme to append the elemets at odd  numbered indexes from two different lists

#Appproach One: Using index method
lst =[]
new_lst = []
lst1 = [2,4,6,8,10]
lst2 = [4,8,12,16,20]

def odd_even_list(para1, para2):
    for i in lst1:
        if lst1.index(i) % 2 != 0:
            lst.append(i)

    for j in lst2:
        if lst2.index(j) % 2 == 0:
            lst.append(j)
    return lst
print(odd_even_list(lst1,lst2))


#Approach two: Using range method
def even_odd_list(p1,p2):
    for i in range(0,len(p1)):
        if i % 2 != 0:
            new_lst.append(p1[i])


    for j in range(0,len(p2)):
        if j % 2 == 0:
            new_lst.append(p2[j])

    return new_lst

print(even_odd_list(lst1,lst2))