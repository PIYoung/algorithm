import sys

K, Q, L, B, KN, P = map(int, sys.stdin.readline().split())

print(f"{1 - K} {1 - Q} {2 - L} {2 - B} {2 - KN} {8 - P}")