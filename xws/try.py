import calendar as cal
import datetime
n = 12
today = datetime.datetime.today()
year = today.year
m = today.month - n
if m == 0:
    m = 12
    year -= 1
last_day = cal.monthrange(year, m)[1]
month_first = datetime.date(year, m, 1)
month_last = datetime.date(year, m, last_day)
print(month_first, month_last)