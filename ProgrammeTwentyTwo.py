#Approach One:

lst = [7, 9, 34, 56, 100]

def lst_sum(listt):
    count = 0
    for i in listt:
        count += i
    return count

print(lst_sum(lst))

#Approach Two: Using inbuilt list method

def func_three(liist):
    total = sum(liist)
    return total
print(func_three(lst))


#Approach Three: Using while loop
def sum_lst(llist):
    counter = 0
    k = 0
    while (k < len(llist)):
        counter = counter + llist[k]
        k += 1
    return counter

print(sum_lst(lst))
