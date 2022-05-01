from collections import deque

N = int(input())

queue = deque()
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
        queue.append(value)
    elif command == "pop":
        if len(queue) > 0:
            answer.append(queue.popleft())
        else:
            answer.append(-1)
    elif command == "size":
        answer.append(len(queue))
    elif command == "empty":
        if len(queue) > 0:
            answer.append(0)
        else:
            answer.append(1)
    elif command == "front":
        if len(queue) > 0:
            answer.append(queue[0])
        else:
            answer.append(-1)
    else:
        if len(queue) > 0:
            answer.append(queue[-1])
        else:
            answer.append(-1)

print("\n".join(map(str, answer)))