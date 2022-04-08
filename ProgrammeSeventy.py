#Programme to see if the given number is a palindrome or not

#Approach One: Using negative indexing
def check_palindrome(number):
    #Using slicing method to reverse the word
    reversed_word  = number[::-1]
    #Compairing to see if the original word is same as reversed word
    if number == reversed_word:
        return "Yes, this word is a palindrome!"
    else:
        return "No, this word is not palindrome!"

try:
    input_number = input("Enter a number: \n")
    print(check_palindrome(input_number))
except:
    print("Invalid Input")

#Approach Three: Using while loop
number = input("Enter a number: \n")
ans = ""
l = len(number)
#Using while lopp to reverse a string
while l > 0:
    ans = ans + number[l-1]
    l -= 1
if number == ans:
    print("This number is a Palindrome")
else:
    print("This number is not a Palindrome")