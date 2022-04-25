import sys

A, B, C, D, E = map(int, sys.stdin.readline().split())

print((A * A + B * B + C * C + D * D + E * E) % 10)