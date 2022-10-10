import sys
K, L = map(int, sys.stdin.readline().split())

for l in range(2, L):
    if K % l == 0:
        print("BAD", l)
        exit()
        
print("GOOD")