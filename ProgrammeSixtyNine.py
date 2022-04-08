# Using regular expression module
import re

#Initializing a variable that will keep the count of how many times a negative number appears
count = 0
strng = input("Enter the string: \n")


def negative_indices(parameter):
   #initializing the counter to keep track of calculations
   total = 0
   #Using re.findall() to detect a pattern
   for i in re.findall("-\d+",parameter):
      #If the pattern is encountered summing it up with other negative numbers
      total += int(i)
   return total

print(negative_indices(strng))


