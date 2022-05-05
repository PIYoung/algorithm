S = int(input())

answer = 0
temp = []
index = 1

while True:
    if S - index < 0:
        S = 0
        break
    else:
        S -= index

    answer += 1
    index += 1


print(answer)