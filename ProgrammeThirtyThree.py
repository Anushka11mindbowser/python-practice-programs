#Approach One:
special_characters = ["!","@",'#','$','%','^','&','*','(',')']
alphabet = 0
digit = 0
whitespace = 0
upper = 0
sc = 0

input_string = input("Enter your password")
updated_password = input_string.split(",")
for j in updated_password:
    for i in j:
        if i.isalpha():
            alphabet += 1
            if i.isupper():
                upper += 1
        elif i.isdigit():
            digit += 1
        elif i in special_characters:
            sc += 1
        else:
            whitespace += 1

answer = []
a = "Password Accepted"
b = "Password Denied"
for k in updated_password:
    if (7 <= len(k)<=12 and digit > 0 and upper > 0 and alphabet > 0 and sc>0 and whitespace == 0):
        answer.append(a)
    else:
        answer.append(b)
print(answer)

