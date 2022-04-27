sD, sH, sM = map(int, input().split())

total_min = (sD * 60 * 24) + (sH * 60) + sM - ((11 * 60 * 24) + 11 * 60 + 11)

if total_min < 0:
    total_min = -1

print(total_min)