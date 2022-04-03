list1 = ['a','b','c','d','e','f','g','h','i','j']
input_string = input("Enter a string\n")
def cut_out_char(lst, str):
    for i in str:
        if i in lst:
            lst.remove(i)
    return lst
print(cut_out_char(list1,input_string))

