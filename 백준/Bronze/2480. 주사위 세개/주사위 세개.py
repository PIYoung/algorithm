import sys

A, B, C = map(int, sys.stdin.readline().split())

answer = 0

if A == B and B == C:
    answer = 10000 + A * 1000
elif A == B and B != C:
    answer = 1000 + A * 100
elif A == C and C != B:
    answer = 1000 + A * 100
elif B == C and C != A:
    answer = 1000 + B * 100
else:
    answer = max(A, B, C) * 100

print(answer)