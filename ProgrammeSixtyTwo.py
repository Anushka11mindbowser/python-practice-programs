#Approach One : Using inbuilt set functions
set1 = {2, 4, 6, 8, 10}
set2 = {5,10,15,20,25}
result = {}
result = set1.intersection(set2)
print(result)

#Approach Two: Using nested loops
answer = []
set3 = {1,3,5,7,9}
set4 = {2,3,5,7,11}
for i in set3:
    for j in set4:
        if i == j:
            answer.append(j)
print(set(answer))

