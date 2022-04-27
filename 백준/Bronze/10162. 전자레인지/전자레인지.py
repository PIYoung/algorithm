target = int(input())

fm = 0
om = 0
ts = 0

if target >= 300:
    fm = target // 300
    target -= fm * 300

if target >= 60:
    om = target // 60
    target -= om * 60

if target >= 10:
    ts = target // 10
    target -= ts * 10

if target != 0:
    print(-1)
else:
    print(f"{fm} {om} {ts}")