lst = []
s = int(input("Enter the starting range: \n"))
e = int(input("Enter the ending range: \n"))
for i in range(s, e+1):
    a = str(i)
    for j in range(0,len(str(i))):
        if j % 2 == 0:
         lst.append(j)
print(lst)










