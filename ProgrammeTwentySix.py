#Approach One: Simple Approach
#Defining a list to append the result
lst = []
for i in range(7,71 ):
    #Checking if the number in the list is divisible by 7 and not divisible by 5 and appending it to the resulting list accordingly
    if (i % 7 == 0 and i % 5 != 0):
        lst.append(i)
print(lst)

#Approach Two: Accepting the range from user

list1 = []
def multiples_of_seven():
        try:
            #Accepting the range from the user
            s = int(input("Enter the starting range\n"))
            e = int(input("Enter the ending range\n"))
            for j in range(s, e +1):
                if (j % 7 == 0 and j % 5 != 0):
                    list1.append(j)
            return list1
        except:
            return "Enter input correctly"
print(multiples_of_seven())