#統計系116
#H24126078
#鄭雅云

year = int(input("Please input Year:"))
month = int(input("Please input Month:"))

t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
if month < 3:
	year -= 1
first_day = int((year + year//4 - year//100 + year//400 + t[month-1] + 1) % 7)

def days_in_month(year, month):
	if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
		return 31
	elif month == 2 and year == leap_year(year):
		return 29
	elif month == 2:
		return 28
	else :
		return 30
num = days_in_month(year, month)

day = 1
print("%-4s" * 7 % ("Sun","Mon","Tue","Wed","Thu","Fri","Sat"))
print(("    " * (first_day)), end ="")
for i in range(1, num+1):
	print("%02d" % (day) + "%2s" % '', end = "")
	if (first_day+day)%7 == 0:
		print("\n", end="")
	day = day+1