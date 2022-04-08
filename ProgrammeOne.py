
#Approach Two
def hours_to_seconds(hours):
    #One hour is 60 minutes and 1 minutes is 60 seconds, thus 1 hour is 3600 seconds
    seconds = hours * 3600;
    return str(hours) + " hours are equivalent to " + str(seconds) + " seconds."

print(hours_to_seconds(11))

#Approach Three
try:
    hour = int(input("Enter the number of hours here:"))
    print(hour * 3600)
except:
    print("Only Numeric Values are accepted")


#Approach Four
def hours_conversion():
    try:
        # h is for hours, s is for seconds, statements is for result
        h = int(input("Number of hours: "))
        s = h * 3600
        statement = str(h) + " hours are equivalent to " + str(s) + " seconds."
        return statement;
    except:
        print("Only Numeric Values are accepted")
print(hours_conversion())

#Approach Five
new_hour= 5;
new_seconds = new_hour * 3600
print(new_seconds)


