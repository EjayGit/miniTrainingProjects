import datetime as dt

now = dt.datetime.now()
print(now)
datetimeObj2 = dt.datetime(2024,3,4,12,16,18,345665)
print(datetimeObj2)
dateObj = dt.date(2025,9,13)
print(dateObj)
print(type(dateObj))
customDate = '2024-9-13'
dateObj = dt.date.today()
print(dateObj)
print(f"Year: {dateObj.year}")
print(f"Month: {dateObj.month}")
print(f"Day: {dateObj.day}")
timeObj = dt.time(11,15,12,344)
print(timeObj)
print(timeObj.hour)
print(timeObj.minute)
print(timeObj.second)
print(timeObj.microsecond)
print(type(timeObj))
date1 = dt.date(2017,5,21)
date2 = dt.date(1986,10,15)
date3 = date1-date2
print(date3)
nowFormatted = now.strftime("%d-%m-%Y H%H:M%M:S%S")
nowFormatted2 = now.strftime("S%S;H%H;M%M")
print(nowFormatted)
print(nowFormatted2)
dateStr = "11/April/2024"
dateObj2 = dt.datetime.strptime(dateStr, "%d/%B/%Y") # / is same as str separator
print(dateObj2)