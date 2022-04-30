destination = int(input())
n = str(destination)

temp = 0
answer = 0

if len(n) == 1:
    n += "0"

while destination != temp:
    answer += 1

    sum = int(n[0]) + int(n[1])
    origin_last = str(destination)[-1] if answer == 1 else n[-1]
    sum_last = str(sum)[-1]
    n = (origin_last) + (sum_last)
    temp = int(n)


if destination == 0:
    answer = 1

print(answer)