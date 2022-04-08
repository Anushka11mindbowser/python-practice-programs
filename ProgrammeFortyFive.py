#Approach One

#Defining two different lists for two different approaches used to solve this programming problem
sample_list = [54, 44, 27, 79, 91, 41]
sample_list2 = [56, 78, 23, 12, 90, 34, 21]


def modify_list():
    #Removing third element in the list, thus passing 2 as argument
    sample_list.pop(2)
    #After removing an element in the list, all elements index gets shifted to the left, hence 5th element comes at index 3
    sample_list.pop(3)
    print(sample_list)
    #Insering 11 at index 2
    sample_list.insert(2,11)
    #Inserting element at the end of the list
    sample_list.append(11)
    return sample_list
print(modify_list())

def list_modified():
    try:
        a = int(input("Enter the index position from where you want to remove an element\n"))
        sample_list2.pop(a)
        #Since an element is removed from in betweeen the list, all the indices will shift tom right, hence b-1
        b = int(input("Enter the index of next element you wish to remove:\n"))
        sample_list2.pop(b-1)
        c = int(input("Enter the element you want to add\n"))
        d = int(input("Specify the index where you want to add\n"))
        sample_list2.insert(d,c)
        e = int(input("Enter another elemnt you wish to add at the end of list\n"))
        sample_list2.append(e)
        return sample_list2
    except:
        return "Incorrect Input"
print(list_modified())
