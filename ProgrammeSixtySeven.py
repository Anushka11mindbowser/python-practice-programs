#Approach One direct comparison
import datetime
#Getting the values of day,month and year by using strptime() and comparing the value obtained by weekday()
try:
    month, year = input('Enter the month & year: ').split()
    print('Yes' if datetime.datetime.strptime('13 '+' '+month+' '+year, '%d %m %Y').weekday()==4 else 'No')
except:
    print("Invalid Input")

#Approch 2 : Using the logic of Sunday, the 1
# The logic for Friday, the  13 is that the 1st of that month always falls on Sunday
try:
    month1, year1 = input("Enter the month and year").split()
    print('Yes, this month has Friday, the 13' if datetime.datetime.strptime('1' + ' ' + month1 + ' ' + year1, '%d %m %Y').weekday() == 6 else 'No, this month does not have Friday, the 13')
except:
    print("Invalid Input")