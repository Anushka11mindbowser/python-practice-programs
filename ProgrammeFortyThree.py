#Approach One: Using datetime library and weekday
import datetime
try:
    #obtaining day, month, year using strptime()
    day,month,year = input("Enter the date in DD MM YYYY format: \n").split()
    #Obtaining the code for each weekday using weekday() and then compairing
    week_code = datetime.datetime.strptime(day + " " + month + " " + year, '%d %m %Y').weekday()
    if week_code == 6:
        print("It is a Sunday")
    elif week_code == 0:
        print("It is a Monday")
    elif week_code == 1:
        print("It is a Tuesday")
    elif week_code == 2:
        print("It is a Wednesday")
    elif week_code == 3:
        print("It is a Thursday")
    elif week_code == 4:
        print("It is a Friday")
    elif week_code == 5:
        print("It is a Saturday")
except:
    print("Incorrect Input")


