input_string = input("Enter your transaction log here: \n")
#Splitting the components in the input string into a list
log = input_string.split(" ")
#Initializing the varaiable to keep track of the amount in the bank
money = 0
for i in log:
    #Obtaining the letter to determine if you need to withdraw or deposit
    action = i[0]
    #Obtaining the transaction amount
    amount = i[1:]
    if action == "D":
        #Incrementing the amount
        money += int(amount)
    elif action == "W":
        #Decrementing the amount
        money -= int(amount)
    else:
        print("Invalid Input")

print(money)