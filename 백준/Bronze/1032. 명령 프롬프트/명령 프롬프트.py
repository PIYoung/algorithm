n = int(input())
input_list = [input() for i in range(n)]

answer = ""

for i in range(len(input_list[0])):
    if len(input_list) == 1:
        answer = input_list[0]
        break

    for j in range(len(input_list) - 1):
        if input_list[j][i] != input_list[j + 1][i]:
            answer += "?"
            break

        if j == len(input_list) - 2:
            answer += input_list[j][i]


print(answer)