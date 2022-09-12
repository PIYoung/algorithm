x, y = map(int, input().split())
r = int(input())

xmr = x - r
xpr = x + r
ymr = y - r
ypr = y + r
print(f"{xmr} {ypr}")
print(f"{xpr} {ypr}")
print(f"{xpr} {ymr}")
print(f"{xmr} {ymr}")