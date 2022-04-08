#Approach One: Using datetime libraries and using strptime function

#importing datetime library
import datetime
def calculate_time():
    try:
        date1=input("Enter the first date (in DD/MM/YYYY) \n")
        date2 = input("Enter the second date (in DD/MM/YYY)\n")
        #Obtaining day, month, year using strptime()
        date1 = datetime.datetime.strptime(date1, "%d/%m/%Y").date()
        date2 = datetime.datetime.strptime(date2, "%d/%m/%Y").date()
        #Calculating the difference between two months and years
        month = date1.month - date2.month
        year = date1.year - date2.year
        result = (month * 30) + (year * 365) - (date1.day < date2.day)
        return result
    except:
        print("Invalid Input")
print(calculate_time())