n = int(input())

answer = []

for i in reversed(range(n)):
    answer.append(
        ("*" * (n - i) + " " * (i) + " " * i) + ("*" * (n - i))
    )

for i in range(n):
    if i == 0:
        continue

    answer.append(
        ("*" * (n - i) + " " * (i) + " " * i) + ("*" * (n - i))
    )

print("\n".join(answer))