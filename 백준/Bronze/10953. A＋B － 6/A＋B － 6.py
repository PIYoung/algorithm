n = int(input())

answer = []

for _ in range(n):
    A, B = map(int, input().split(","))

    answer.append(A + B)

print("\n".join(map(str, answer)))