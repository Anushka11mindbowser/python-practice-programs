input_string = input("Enter a string: \n")
res_lst = []
input_words = input_string.split(" ")
for i in input_words:
    if len(i) % 2 != 0:
        k = i[::-1]
        res_lst.append(k)
    else:
        res_lst.append(i)
res_string = " ".join(res_lst)
print("Result:" + res_string + ".\n")

