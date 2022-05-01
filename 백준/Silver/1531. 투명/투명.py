N, M = map(int, input().split())
picture = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            picture[i - 1][j - 1] += 1

answer = 0
for i in range(100):
    for j in range(100):
        if picture[i][j] > M:
            answer += 1

print(answer)