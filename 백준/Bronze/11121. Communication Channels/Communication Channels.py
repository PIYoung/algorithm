N = int(input())

for _ in range(N):
    a, b = map(str, input().split())
    flag = True

    for i in range(len(a)):
        if a[i] != b[i]:
            print("ERROR")
            flag = False
            break

    if flag:
        print("OK")