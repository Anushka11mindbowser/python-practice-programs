#Approach One: Using list comprehensions
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = [i**2 for i in lst if i%2 != 0]
print(result)

#Approach using if-else
result_a = []
for i in lst:
    if i % 2 != 0:
        result_a.append(i**2)
print(result_a)

#Approach Three: Taking input from user
# creating an empty list
empty_lst = []
result_b = []

# number of elements as input
number = int(input("Enter the number of elements you need:\n"))


# iterating till the range
for i in range(0,number):
    item = int(input("Enter the elements"))
    empty_lst.append(item)

for j in empty_lst:
    if j % 2 != 0:
        result_b.append(i*i)
print(result_b)


