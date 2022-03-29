#Approach One: Using inbuilt method
def compare_strings(str1, str2):
    if (len(str1) == len(str2)):
        return True
    else:
        return False

print(compare_strings("Minakshi", "Pushkar"))

#Approach Two: Using for loop

def compare_with_loops():
    count1 = 0
    count2 = 0
    string1 = input("Enter a string: \n")
    string2 = input("Enter the second string: \n")
    for i in string1:
        count1 += 1

    for j in string2:
        count2 += 1

    if (count1 == count2):
        return True
    else:
        return False

print(compare_with_loops())

#Approach Three: Using while loop along with slice

def comparison(strng1, strng2):
    counter1 = 0
    while strng1[counter1:]:
        counter1 += 1

    counter2 = 0
    while strng2[counter2:]:
        counter2 += 1

    if (counter1 == counter2):
        return True
    else:
        return False

print(comparison('Paris', 'Hartford'))
