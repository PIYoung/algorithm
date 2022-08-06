import math

S = int(input())
A = int(input())
B = int(input())
price = 250

if S <= A:
    print(price)
else:
    print(price + 100 * math.ceil((S - A) / B))