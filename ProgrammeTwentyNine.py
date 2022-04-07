start = int(input("Enter the starting the range: \n"))
end = int(input("Enter the ending the range: \n"))
res_lst = []
def even_digits():
    for i in range(start,end+1):
        a = str(i)
        b = list(a)
        for j in b:
            if int(j) % 2 == 0:
                res_lst.append(i)
    print(res_lst)

print(even_digits())





