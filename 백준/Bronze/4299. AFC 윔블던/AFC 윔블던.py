import sys

summary, diff = map(int, sys.stdin.readline().split())

a = (summary + diff) // 2
b = summary - a

if b >= 0 and a >= 0 and a + b == summary and abs(a - b) == diff:
    print(f"{max([a, b])} {min([a, b])}")
else:
    print(-1)