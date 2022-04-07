# Using regular expression module
import re
count = 0
strng = input("Enter the string: \n")


def negative_indices(parameter):
   total = 0
   for i in re.findall("-\d+",parameter):
      total += int(i)
   return total

print(negative_indices(strng))


