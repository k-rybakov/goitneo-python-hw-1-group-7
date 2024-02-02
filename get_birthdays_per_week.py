from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    # first day to collect birthdays is Saturday of the current week
    # "today" is not the best day for start since we can run the script on Sunday of the current week and lose weekend birthdays
    this_week_saturday = today + timedelta(days=(5 - today.weekday()))

    result = defaultdict(list)
    
    for user in users:
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < this_week_saturday:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta_days = (birthday_this_year - this_week_saturday).days

        if delta_days < 7:
            day_name = birthday_this_year.strftime('%A')
            if day_name in ('Saturday', 'Sunday'):
                day_name = 'Monday'
            result[day_name].append(user["name"])
            
    for day, names in result.items():
        print(f"{day}: {', '.join(names)}")
