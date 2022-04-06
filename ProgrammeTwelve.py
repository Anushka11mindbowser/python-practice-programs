#Approach One: Using libraries

from datetime import  datetime
def calculate_time():
    current = datetime.now()
    print(current)
    




#Approach Two: Basic Approach
try:
    hours = int(input("Enter the the hours: \n"))
    minutes = int(input("Enter the number of minutes: \n"))
    seconds = (hours * 3600) + (minutes * 60)
    print(seconds)
except:
    print("Enter correct values")

