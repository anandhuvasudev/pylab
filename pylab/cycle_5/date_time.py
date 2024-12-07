import datetime
now=datetime.datetime.now()

current_date_time=now
print(f"Current date and time :{current_date_time}")

current_year=now.year
print(f"Current year : {current_year}")

current_month=now.month
print(f"Month of the year :{current_month}")

week_number=now.isocalendar()[1]
print(f"Week number of the year :{week_number} ")

weekday=now.weekday()
print(f"Wednesday of the week (0=monday,6=sunday): {weekday}")

day_of_year = now.timetuple().tm_yday
print(f"day of the year:{day_of_year}")

day_of_month=now.day
print(f"Day of the Month: {day_of_month}")

day_of_week=now.strftime("%A")
print(f"Day of the week : {day_of_week} ")
