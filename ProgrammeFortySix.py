#Using list slicing and reverse function
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
def reverse_chunks(param):

    list1 = sample_list[0:3]
    list2 = sample_list[3:6]
    list3 = sample_list[6:9]
    list1.reverse()
    list2.reverse()
    list3.reverse()
    return list1,list2,list3

print(reverse_chunks(sample_list))

