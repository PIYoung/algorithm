n = int(input())

answer = []

for i in reversed(range(n)):
    answer.append(" " * (n - i - 1) + "*" * (i + 1) + "*" * i)

for i in range(n):
    if i == 0:
        continue

    answer.append(" " * (n - i - 1) + "*" * (i + 1) + "*" * i)

print("\n".join(answer))