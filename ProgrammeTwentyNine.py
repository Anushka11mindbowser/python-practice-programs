start = int(input("Enter the starting the range: \n"))
end = int(input("Enter the ending the range: \n"))
#initializing an empty list to append resulting values
res_lst = []
def even_digits():
    for i in range(start,end+1):
        #Converting int to str
        a = str(i)
        #Converting a string to list
        b = list(a)
        #Traversing the list and checking if the indivisual digit is even or not
        for j in b:
            if int(j) % 2 == 0:
                #Appending the the entire number to the list
                res_lst.append(i)
            else:
                pass
    print(res_lst)

print(even_digits())





