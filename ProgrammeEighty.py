def camel_case_string(strng):
    lst = strng.split(" ")
    res_lst = []
    for i in lst:
        i = i[0].upper() + i[1:]
        res_lst.append(i)
    resulting_string = "".join(res_lst)
    resulting_string = resulting_string[0].lower() + resulting_string[1:]

    return resulting_string


print(camel_case_string("Anushka pawar lives In Pune"))