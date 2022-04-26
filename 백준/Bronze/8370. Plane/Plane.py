import sys

n1row, n1col, n2row, n2col = map(int, sys.stdin.readline().split())

print((n1row * n1col) + (n2row * n2col))