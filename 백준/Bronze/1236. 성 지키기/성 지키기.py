N, M = map(int, input().split())
board = [input() for _ in range(N)]

row = 0
col = 0

for i in range(N):
    if "X" not in board[i]:
        row += 1

for j in range(M):
    if "X" not in [board[i][j] for i in range(N)]:
        col += 1

print(max(row, col))