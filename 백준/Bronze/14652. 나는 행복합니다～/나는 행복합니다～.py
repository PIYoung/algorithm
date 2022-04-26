import sys

N, M, K = map(int, sys.stdin.readline().split())

R = K // M
C = K - (M * R)

print(f"{R} {C}")