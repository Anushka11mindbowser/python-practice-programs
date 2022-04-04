input_string = input("Enter your transaction log here: \n")
log = input_string.split(" ")
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