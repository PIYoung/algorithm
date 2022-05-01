N, m_count = map(int, input().split())
input_list = [input() for _ in range(N - 1)]

tree = {}
answer = []

for i in input_list:
    from_node, to_node, distance = map(int, i.split())

    if not from_node in tree:
        tree[from_node] = {}

    if not to_node in tree:
        tree[to_node] = {}

    tree[from_node][to_node] = distance
    tree[to_node][from_node] = distance


def dfs(start, goal):
    visited = []
    stack = [start]
    distances = [0] * (N + 1)

    while stack:
        node = stack.pop()

        if node == goal:
            return distances[node]

        for next_node, distance in tree[node].items():
            if next_node not in visited:
                distances[next_node] = distances[node] + distance
                stack.append(next_node)
                visited.append(next_node)


for i in range(m_count):
    reach_end = 0
    start, goal = map(int, input().split())

    answer.append(dfs(start, goal))

print("\n".join(str(e) for e in answer))