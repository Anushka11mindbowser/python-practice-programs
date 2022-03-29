
#Approach Two
def hours_to_seconds(hours):
    seconds = hours * 3600;
    return str(hours)  + " hours are equivalent to " + str(seconds) + " seconds."

print(hours_to_seconds(11))

#Approach Three
hour = int(input("Enter the number of hours here:"))
print(hour * 3600)

#Approach Four
def hours_conversion():
    h = int(input("Number of hours: "))
    s = h * 3600
    statement =  str(h) + " hours are equivalent to " + str(s) + " seconds."
    return statement;
print(hours_conversion())

#Approach Five
new_hour= 5;
new_seconds = new_hour * 3600
print(new_seconds)


