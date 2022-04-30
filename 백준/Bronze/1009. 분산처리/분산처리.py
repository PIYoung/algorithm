n = int(input())

answer = []
arr = []

for i in range(n):
    a, b = map(int, input().split())
    a = str(a)
    a = int(a[len(a) - 1])

    if a == 1:
        arr = [1]
    elif a == 2:
        arr = [2, 4, 8, 6]
    elif a == 3:
        arr = [3, 9, 7, 1]
    elif a == 4:
        arr = [4, 6]
    elif a == 5:
        arr = [5]
    elif a == 6:
        arr = [6]
    elif a == 7:
        arr = [7, 9, 3, 1]
    elif a == 8:
        arr = [8, 4, 2, 6]
    elif a == 9:
        arr = [9, 1]
    else:
        arr = [10]

    answer.append(arr[b % len(arr) - 1])


print("\n".join(str(e) for e in answer))