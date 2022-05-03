import datetime

sy, sm, sd = map(int, input().split())
dy, dm, dd = map(int, input().split())

datetime_today = datetime.date(sy, sm, sd)
datetime_d_day = datetime.date(dy, dm, dd)

diff = str(datetime_d_day - datetime_today).split()[0]

if int(diff) >= 365243:
    print("gg")
else:
    print(f"D-{diff}")