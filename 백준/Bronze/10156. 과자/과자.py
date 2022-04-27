price, count, have = map(int, input().split())

if price * count > have:
    print(price * count - have)
else:
    print(0)