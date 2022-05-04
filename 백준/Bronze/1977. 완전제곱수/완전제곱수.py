M = int(input())
N = int(input())

data_list = []
index = 1
value = index**2

while value <= N:
    if M <= value <= N:
        data_list.append(value)

    index += 1
    value = index**2


if len(data_list) == 0:
    print("-1")
else:
    print(sum(data_list))
    print(min(data_list))