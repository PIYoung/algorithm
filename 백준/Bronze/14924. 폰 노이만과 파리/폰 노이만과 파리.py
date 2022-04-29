S, T, D = map(int, input().split())

answer = 0

meet_time = D // (S * 2)
answer = meet_time * T

print(answer)