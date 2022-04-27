import sys

A = int(sys.stdin.readline())
B = sys.stdin.readline()

first = A * int(B[2])
second = A * int(B[1])
third = A * int(B[0])
total = A * int(B)

print(first)
print(second)
print(third)
print(total)