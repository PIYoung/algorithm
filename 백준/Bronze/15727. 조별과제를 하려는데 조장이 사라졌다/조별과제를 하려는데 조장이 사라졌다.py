import sys

N = int(sys.stdin.readline())

result = N // 5
if N % 5 != 0:
    result += 1

print(result)