#Programme to determine lcm of two integers
def lcm():
    try:
        n1 = int(input("Enter the first number:\n"))
        n2 = int(input("Enter the second number: \n"))

        #Initializing two empty lists to store multiples of the two integers
        lst1 = []
        lst2 = []

        #finding out first 10 multiples of the integers by using range() and appending them to the  respective lists
        for i in range(1,10):
            lst1.append(i * n1)
        for j in range(1,10):
            lst2.append(j * n2)

        #Converrting both the multiples list to set and apply intersection() on them to find common values in both of them
        a = set(lst1).intersection(set(lst2))
        #If there are no common multiples, lcm is product of both the integers
        if len(a) == 0:
            return n1*n2
        else:
            #the smallest common multiple is the lcm of the two integers
           return min(a)
    except:
        return "Please enter a numeric value"
print("The LCM is: " + str(lcm()) + ".\n")