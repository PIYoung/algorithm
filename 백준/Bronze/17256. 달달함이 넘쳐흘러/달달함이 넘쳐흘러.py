import sys

X1, Y1, Z1 = map(int, sys.stdin.readline().split())
X3, Y3, Z3 = map(int, sys.stdin.readline().split())

print(f"{X3 - Z1} {Y3 // Y1} {Z3 - X1}")