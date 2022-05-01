from collections import deque

N = int(input())

stack = deque()
answer = deque()

for _ in range(N):
    data = input()

    command = data
    value = 0

    if data.find(" ") != -1:
        split = data.split()
        command = split[0]
        value = int(split[1])

    if command == "push":
        stack.append(value)
    elif command == "pop":
        if len(stack) > 0:
            answer.append(stack.pop())
        else:
            answer.append(-1)
    elif command == "size":
        answer.append(len(stack))
    elif command == "empty":
        if len(stack) > 0:
            answer.append(0)
        else:
            answer.append(1)
    else:
        if len(stack) > 0:
            answer.append(stack[-1])
        else:
            answer.append(-1)


print("\n".join(map(str, answer)))