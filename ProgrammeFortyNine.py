#Approach One:
#Defining two lists to be concatenated
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
lst = []
#Traversing two lists simultaneously
def mismatch_lists(para1, para2):
    for i in para1:
        for j in para2:
            #Concatenating two elements from two different lists
            res = i + j
            #appending the result to the string
            lst.append(res)
    print(lst)
print(mismatch_lists(list1,list2))