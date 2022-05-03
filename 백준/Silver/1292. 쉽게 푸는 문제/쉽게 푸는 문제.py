A, B = map(int, input().split())

arr = []
answer = 0

for i in range(1, B + 1):
    for j in range(1, i + 1):
        arr.append(i)

for i in range(A - 1, B):
    answer += arr[i]


print(answer)