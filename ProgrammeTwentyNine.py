s = int(input("Enter the starting range: \n"))
e = int(input("Enter the ending range: \n"))
number = ""
lst = []
for i in range(s,e+1):
    a = str(i)
    for j in a:
        if int(j) % 2 == 0:
            lst.append(i)
print(i)








