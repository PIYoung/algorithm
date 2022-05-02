answer = 0

for i in range(8):
    line = input()

    is_first_white = 0
    if i % 2 == 0:
        is_first_white = 1

    for j in range(8):
        if is_first_white == 1:
            if j % 2 == 0 and line[j] == "F":
                answer += 1
        else:
            if j % 2 != 0 and line[j] == "F":
                answer += 1

print(answer)