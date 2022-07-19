B = int(input())
P = 5 * B - 400
sea_level = 100

print(P)
if P < sea_level:
    print(1)
elif P > sea_level:
    print(-1)
else:
    print(0)