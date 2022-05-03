N = int(input())

answer = []
for _ in range(N):
    data_list = list(input().split())

    temp = ""
    for s in data_list:
        s_list = list(s)
        s_list.reverse()
        temp += "".join(s_list) + " "

    answer.append(temp.rstrip())

print("\n".join(answer))