#Approach One: using list comprehensions and zip
lst = []
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
def two_lists(param1, param2):
   res = [i + j for i,j in zip(list1,list2)]
   ans = str(res)
   return ans

print(two_lists(list1,list2))