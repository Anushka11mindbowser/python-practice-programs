#Approach One: Using insert method
lst = [[2,4,6,8,10],[3,6,9,12,15], [4,8,1,2,16,20], [5,10,15,20,25]]
lst[0].insert(1,1)
print(lst)
#Approach Two: Using append method on list
lst.append([1,2,3,4,5])
print(lst)
#Approach Three: Using append in sublist
lst[4].append(6)
print(lst)
#Approach Four: Using insert on overall list
lst.insert(2,8)
print(lst)
#Approach Five: Accepting input from the user
i = int(input("Enter the index at which you have to insert the element: \n"))
si = int(input("Enter the subindex at which you have to insert the element:\n"))
ele = int(input("Enter the element you want to insert: \n"))
# lst[i].append(ele)
lst[i].insert(si,ele)
print(lst)