from collections import deque

N = int(input())


def dfs(graph: dict, visited: list[list[bool]], start_x: int, start_y: int):
    stack = deque([(start_x, start_y)])

    while stack:
        vertex = stack.pop()
        x, y = vertex

        if not visited[y][x]:
            visited[y][x] = True
            stack.extend(graph[str(x) + "," + str(y)])


answer = deque()
for _ in range(N):
    width, height, cabbages = map(int, input().split())

    graph = {}
    farm = [[0 for _ in range(width)] for _ in range(height)]

    for _ in range(cabbages):
        x, y = map(int, input().split())
        farm[y][x] = 1

        graph[str(x) + "," + str(y)] = []
        key = []
        value = []

        if y > 0:
            if farm[y - 1][x] == 1:
                key.append(str(x) + "," + str(y - 1))
                value.append((x, y - 1))

        if x > 0:
            if farm[y][x - 1] == 1:
                key.append(str(x - 1) + "," + str(y))
                value.append((x - 1, y))

        while key:
            k = key.pop()
            v = value.pop()

            graph[str(x) + "," + str(y)].append(v)
            graph[k].append((x, y))

    worm = 0
    visited = [[False] * len(farm[0]) for _ in range(len(farm))]
    for y in range(len(farm)):
        for x in range(len(farm[0])):
            if farm[y][x] == 1 and not visited[y][x]:
                worm += 1
                dfs(graph, visited, x, y)

    answer.append(worm)

print("\n".join(map(str, answer)))