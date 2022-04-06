#Approach One: Using libraries
from datetime import date

def age_in_days(bday):
    today = date.today()
    age = today.year - bday.year -((today.month, today.day ) < (bday.month, bday.day))
    return age * 365

print(age_in_days(date(2005,12,22)))

#Approach Two: Basic way
age = (input("Enter the age in years\n"))
if age.isdigit():
    print("The age in days would be : \n" + str(int(age)*365))
else:
    print("Invalid Input")

#Approach Three: Using class
class calculateAge:
    def __init__(self,bdate):
        self.bdate = bdate

    def convert(self):
        today = date.today()
        result = today.year - self.bdate.year - ((today.month, today.day) < (self.bdate.month, self.bdate.day))
        return "The age in days would be " + str(result * 365)


new_age = calculateAge(date(2005,12,22))
print(new_age.convert())


