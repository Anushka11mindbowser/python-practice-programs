input_string = input("Enter your transaction log here: \n")
#Splitting the components in the input string into a list
log = input_string.split(" ")
#Initializing the varaiable to keep track of the amount in the bank
money = 0
for i in log:
    action = i[0]
    amount = i[1:]
    if action == "D":
        money += int(amount)
    elif action == "W":
        money -= int(amount)
    else:
        print("Invalid Input")

print(money)