from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
data_list = [list(map(int, stdin.readline().split())) for _ in range(N)]
K = int(stdin.readline())

dynamic_programming_table = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dynamic_programming_table[i][j] = (
            data_list[i - 1][j - 1]
            + dynamic_programming_table[i - 1][j]
            + dynamic_programming_table[i][j - 1]
            - dynamic_programming_table[i - 1][j - 1]
        )


answer = deque()

for _ in range(K):
    i, j, x, y = map(int, stdin.readline().split())
    answer.append(
        dynamic_programming_table[x][y]
        - dynamic_programming_table[x][j - 1]
        - dynamic_programming_table[i - 1][y]
        + dynamic_programming_table[i - 1][j - 1]
    )

print("\n".join(map(str, answer)))