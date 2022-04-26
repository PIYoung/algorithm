import sys

T, G, B, P = map(int, sys.stdin.readline().split())

print((T - 1) // G * B * P)