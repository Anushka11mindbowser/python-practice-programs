def lcm():
    n1 = int(input("Enter the first number:\n"))
    n2 = int(input("Enter the second number: \n"))
    lst1 = []
    lst2 = []
    for i in range(1,10):
        lst1.append(i * n1)
    for j in range(1,10):
        lst2.append(j * n2)

    a = set(lst1).intersection(set(lst2))
    if len(a) == 0:
        return n1*n2
    else:
       return min(a)
print(lcm())