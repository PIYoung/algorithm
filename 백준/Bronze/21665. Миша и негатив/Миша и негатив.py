N, M = map(int, input().split())

lst_0 = []
for i in range(N):
    lst_0.append(input())

input()

lst_1 = []
for i in range(N):
    lst_1.append(input())

count = 0
for x, y in zip(lst_0, lst_1):
    for i in range(M):
        if x[i] == y[i]:
            count += 1

print(count)