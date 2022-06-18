n = int(input())
k = int(input())

x = min(k + 60, n)
result = x * 1500 + (n - x) * 3000

print(result)