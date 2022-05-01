from collections import deque

N = int(input())

answer = deque()

for _ in range(N):
    data = input()

    open = 0
    isBreak = 0
    for s in data:
        if s == "(":
            open += 1
        else:
            open -= 1

        if open < 0:
            answer.append("NO")
            isBreak = 1
            break

    if isBreak == 0:
        if open == 0:
            answer.append("YES")
        else:
            answer.append("NO")


print("\n".join(map(str, answer)))