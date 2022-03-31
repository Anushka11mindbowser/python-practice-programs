digit = 0
letters = 0
sentence =  input("Enter a scentence below\n")
for i in sentence:
    if type(i) == int:
        digit += 1
    elif type(i) == str:
        letters += 1
    else:
        pass

print(digit)
print(letters)