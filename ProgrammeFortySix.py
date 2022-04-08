#Using list slicing and reverse function
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
def reverse_chunks(param):
#Dividing the lists into three parts using slicing
    list1 = sample_list[0:3]
    list2 = sample_list[3:6]
    list3 = sample_list[6:9]
#Reversing these chunks using slice method
    updated_list1 =  list1[::-1]
    updated_list2 = list2[::-1]
    updated_list3 = list3[::-1]

    return updated_list1, updated_list2, updated_list3

print(reverse_chunks(sample_list))

