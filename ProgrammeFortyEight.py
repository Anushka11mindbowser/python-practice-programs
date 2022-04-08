#Approach One: using list comprehensions and zip

#Defining two lists which we want to concatenate by same indexes
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

def two_lists(param1, param2):
   #zip(), appends elements from two different lists
   res = [i + j for i,j in zip(list1,list2)]
   #Converting list to string
   ans = str(res)
   return ans

print(two_lists(list1,list2))