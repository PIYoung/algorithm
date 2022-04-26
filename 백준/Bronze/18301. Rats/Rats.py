import sys

A, B, C = map(int, sys.stdin.readline().split())

print((A + 1) * (B + 1) // (C + 1) - 1)