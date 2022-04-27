answer = ""

for i in range(int(input())):
    A, B = map(int, input().split())

    G = 0
    L = 0

    big = A if A > B else B
    small = B if A > B else A

    while True:
        temp = big % small

        if temp == 0:
            if answer != "":
                answer += "\n"

            G = small
            L = A * B // G
            answer += str(L)
            break

        big = small
        small = temp

print(answer)