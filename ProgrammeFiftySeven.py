#Approch One: Using Datetime and Dateutil's relativedelta module and library

#Importing datetime module
#Imorting relativedelta functiomnality
from datetime import datetime,timedelta
from dateutil.relativedelta import *

#Obtaining current date
date = datetime.now()
print(date)

#Adding six months to that date using relativedelta functionality
date = date + relativedelta(months=+6)
print(date)
