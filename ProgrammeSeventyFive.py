#Program to reverse odd numbered words in a phrase/sentence

#Accepting input from the user
input_string = input("Enter a string: \n")
#Initializing an empty list to store the results
res_lst = []

#Spliting the sentences into words
input_words = input_string.split(" ")

#traveresing through the words in the list
for i in input_words:
    #checking if the length of these word is even or odd, if even we reverse the word and append it to the resulting list
    if len(i) % 2 != 0:
        k = i[::-1]
        res_lst.append(k)
    else:
        #else we just append the original word to the resulting string
        res_lst.append(i)
        #joining all the words in the resulting list and turning it into a string
res_string = " ".join(res_lst)
print("Result:" + res_string + ".\n")

