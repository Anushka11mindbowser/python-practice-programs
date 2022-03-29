#Approach One: Using negative indexing

lst = [76, 98, 244, 64, 33]

lstt= ['milk', 'honey', 'key', 'ghee', 'sugar']
def last_item(sample_list):
    return sample_list[-1]

print(last_item(lst))

#Approach Two: Using len function
def item_last(list1):
    n = len(list1)
    return list1[n-1]
print(item_last(lst))

#Approach Three: Using pop

def using_pop(list2):
  return list2.pop()
print(using_pop(lst))

#Approach Four: Using reverse() method
def using_reverse(list3):
  list3.reverse()
  return list3[0]

print(using_reverse(lstt))



