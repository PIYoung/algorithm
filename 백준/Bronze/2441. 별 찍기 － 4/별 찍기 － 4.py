N = int(input())

answer = []

for i in reversed(range(N)):
    answer.append(" " * (N - i - 1) + "*" * (i + 1))

print("\n".join(answer))