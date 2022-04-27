import sys

a1, a2, a3, a4, a5, a6 = map(int, sys.stdin.readline().split())
b1, b2, b3, b4, b5, b6 = map(int, sys.stdin.readline().split())
c1, c2, c3, c4, c5, c6 = map(int, sys.stdin.readline().split())


def get_work_hours(ch, cm, cs, hh, hm, hs):
    total_sec = (hh * 3600 + hm * 60 + hs) - (ch * 3600 + cm * 60 + cs)
    work_hour = total_sec // 3600
    work_min = (total_sec % 3600) // 60
    work_sec = (total_sec % 3600) % 60

    return f"{work_hour} {work_min} {work_sec}"


print(get_work_hours(a1, a2, a3, a4, a5, a6))
print(get_work_hours(b1, b2, b3, b4, b5, b6))
print(get_work_hours(c1, c2, c3, c4, c5, c6))