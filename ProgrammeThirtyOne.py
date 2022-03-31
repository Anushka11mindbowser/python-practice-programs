#Approach One
console_input = input("Enter the elements by seperating them by commas\n")
lst = console_input.split(' ')
result_list = []
print(lst)
for i in lst:
   if i % 2 == 0:
       result_list.append(i*i)