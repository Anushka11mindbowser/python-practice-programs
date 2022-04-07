#prograame to modify a tuple
sample_tuple = ('oranges', 'apples', 'watermelons', 'guavas', 'pomogranates')
#Turning a tuple into a list
modify_tuple = list(sample_tuple)
print(modify_tuple)
modify_tuple.append("chickoo")
modify_tuple.append("jackfruit")
modify_tuple.append("mangoes")
modify_tuple.append("grapes")
print(modify_tuple)
#Changing the list back to a tuple
tupled = tuple(modify_tuple)
print(tupled)
