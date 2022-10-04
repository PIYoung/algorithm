import sys

N = int(sys.stdin.readline())

sum = 0
for i in range(N):
    sum += int(sys.stdin.readline())
    
print(sum - (N - 1))