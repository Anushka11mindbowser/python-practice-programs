#Approch One: Using Datetime and Dateutil's relativedelta module and library


from datetime import datetime,timedelta
from dateutil.relativedelta import *

date = datetime.now()
print(date)
# 2018-09-24 13:24:04.007620

date = date + relativedelta(months=+6)
print(date)
# 2019-03-24 13:24:04.007620