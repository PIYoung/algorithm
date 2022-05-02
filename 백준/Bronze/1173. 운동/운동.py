N, m, M, T, R = map(int, input().split())

beat = m
answer = 0

if beat + T > M:
    answer = -1
else:
    while N != 0:
        if beat + T > M:
            if beat - R < m:
                beat = m
            else:
                beat -= R
        else:
            beat += T
            N -= 1

        answer += 1


print(answer)