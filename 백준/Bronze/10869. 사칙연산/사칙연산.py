import sys
from math import floor

# 공백으로 구분된 2개 숫자 입력 받기
N, M = map(int, sys.stdin.readline().split())

print(N + M)
print(N - M)
print(N * M)
print(floor(N / M))
print(N % M)