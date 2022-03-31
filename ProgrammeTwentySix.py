#Approach One: Simple Approach
lst = []
for i in range(7,71 ):
    if (i % 7 == 0 and i % 5 != 0):
        lst.append(i)
print(lst)

#Approach Two: Accepting the range from user

list1 = []
def multiples_of_seven():
    s = int(input("Enter the starting range\n"))
    e = int(input("Enter the ending range\n"))
    for j in range(s, e +1):
        if (j % 7 == 0 and j % 5 != 0):
            list1.append(j)
    print(list1)
print(multiples_of_seven())