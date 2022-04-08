#Programme to extend nested sublist


#Approach One: Using insert method

#Defing a nested list with sublists
lst = [[2,4,6,8,10],[3,6,9,12,15], [4,8,1,2,16,20], [5,10,15,20,25]]

#Adding an element in the main list at index 1 with the help of insert()
lst[0].insert(1,1)
print(lst)

#Approach Two: Using append method on list

#Appending a sublist into the main list at the end using append()
lst.append([1,2,3,4,5])
print(lst)


#Approach Three: Using append in sublist
#Adding 6 to the end of a sublist that is present at index 4
lst[4].append(6)
print(lst)

#Approach Four: Using insert on overall list

#Adding integer 8 at index 2 of the list
lst.insert(2,8)
print(lst)

#Approach Five: Accepting input from the user
try:
    i = int(input("Enter the index at which you have to insert the element: \n"))
    si = int(input("Enter the subindex at which you have to insert the element:\n"))
    ele = int(input("Enter the element you want to insert: \n"))
    # lst[i].append(ele)
    lst[i].insert(si,ele)
    print(lst)
except:
    print("Incorrect Input")