#Programme to convert hours and minutes into seconds

#Basic Approach
try:
    hours = int(input("Enter the the hours: \n"))
    minutes = int(input("Enter the number of minutes: \n"))
    seconds = (hours * 3600) + (minutes * 60)
    print(seconds)
except:
    print("Enter correct values")

