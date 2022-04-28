n = int(input())
input_list = list(map(int, input().split()))
target = int(input())

input_list.append(0)
input_list.sort()

answer = 0

for i in range(len(input_list) - 1):
    if input_list[i] == target or input_list[i + 1] == target:
        answer = 0
        break
    elif input_list[i] < target and target < input_list[i + 1]:
        answer = (target - input_list[i]) * (input_list[i + 1] - target) - 1
        break

print(answer)