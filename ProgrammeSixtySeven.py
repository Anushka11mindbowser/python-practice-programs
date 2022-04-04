#Approach One direct comparison
import datetime
month, year = input('Enter the month & year: ').split()
print('Yes' if datetime.datetime.strptime('13 '+' '+month+' '+year, '%d %m %Y').weekday()==4 else 'No')

#Approch 2 : Using the logic of Sunday, the 1
month1, year1 = input("Enter the month and year").split()
print('Yes, this month has Friday, the 13' if datetime.datetime.strptime('1' + ' ' + month1 + ' ' + year1, '%d %m %Y').weekday() == 6 else 'No, this month does not have Friday, the 13')
