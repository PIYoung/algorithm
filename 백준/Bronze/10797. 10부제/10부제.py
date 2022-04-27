banned_number = int(input())
last_car_number_list = list(map(int, input().split()))

answer = 0
for i in last_car_number_list:
    if i == banned_number:
        answer += 1

print(answer)