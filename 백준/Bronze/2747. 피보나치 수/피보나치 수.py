n = int(input())

fibonacci = []
result = 0

for i in range(n + 1):
    if i == 0:
        result = 0
    elif i <= 2:
        result = 1
    else:
        result = fibonacci[i - 1] + fibonacci[i - 2]

    fibonacci.append(result)

print(fibonacci[n])