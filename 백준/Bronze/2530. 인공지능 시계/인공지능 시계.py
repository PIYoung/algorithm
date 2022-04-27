import sys

currentHour, currentMin, currentSec = map(int, sys.stdin.readline().split())
process = int(sys.stdin.readline())

second = currentSec + process
minute = currentMin + second // 60
hour = currentHour + minute // 60

second %= 60
minute %= 60

if hour >= 24:
    hour %= 24

print(f"{hour} {minute} {second}")