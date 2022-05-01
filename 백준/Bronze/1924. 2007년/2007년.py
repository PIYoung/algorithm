from datetime import datetime

month, day = map(int, input().split())

date = f"2007-{month}-{day}"
datetime_date = datetime.strptime(date, "%Y-%m-%d").weekday()
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

print(days[datetime_date])