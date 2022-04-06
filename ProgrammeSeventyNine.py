def left_rotation(strng):
    res_lst = [strng]
    for i in range(0,len(strng)):
      resulting_string = strng[1:] + strng[0]
    res_lst.append(resulting_string)
    for j in range(0, len(strng)-2):
        resulting_string = resulting_string[1:] + resulting_string[0]
        res_lst.append(resulting_string)

    return res_lst
print(left_rotation("Pushkar"))

def right_rotation(strng):
    res_lst = [strng]
    resulting_string = strng[-1] + strng[0:-1]
    res_lst.append(resulting_string)
    for i in range(0,len(strng)-2):
        resulting_string = resulting_string[-1] + resulting_string[0:-1]
        res_lst.append(resulting_string)
    return res_lst
print(right_rotation("Anushka"))