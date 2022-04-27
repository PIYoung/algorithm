count = int(input())
measure_list = sorted(list(map(int, input().split())))


if count == 1:
    print(measure_list[0] ** 2)
else:
    print(measure_list[0] * measure_list[-1])