import sys

currentHour, currentMin = map(int, sys.stdin.readline().split())
process = int(sys.stdin.readline())

minute = currentMin + process
hour = currentHour + minute // 60

minute %= 60

if hour >= 24:
    hour -= 24

print(f"{hour} {minute}")