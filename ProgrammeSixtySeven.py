#Approach One direct comparison
import datetime
try:
    month, year = input('Enter the month & year: ').split()
    print('Yes' if datetime.datetime.strptime('13 '+' '+month+' '+year, '%d %m %Y').weekday()==4 else 'No')
except:
    print("Invalid Input")

#Approch 2 : Using the logic of Sunday, the 1
try:
    month1, year1 = input("Enter the month and year").split()
    print('Yes, this month has Friday, the 13' if datetime.datetime.strptime('1' + ' ' + month1 + ' ' + year1, '%d %m %Y').weekday() == 6 else 'No, this month does not have Friday, the 13')
except:
    print("Invalid Input")