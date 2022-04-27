a_apple, a_orange = map(int, input().split())
b_apple, b_orange = map(int, input().split())

a = a_apple + b_orange
b = b_apple + a_orange

print(min(a, b))