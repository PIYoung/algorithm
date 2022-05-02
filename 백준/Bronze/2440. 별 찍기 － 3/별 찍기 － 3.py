N = int(input())

answer = []

for i in reversed(range(N)):
    answer.append("*" * (i + 1))

print("\n".join(answer))