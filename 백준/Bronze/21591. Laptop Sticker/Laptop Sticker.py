wc, hc, ws, hs = map(int, input().split())

result = 0
if wc - ws >= 2 and hc - hs >= 2:
    result = 1

print(result)
