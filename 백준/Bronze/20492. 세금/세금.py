import sys

N = int(sys.stdin.readline())

n_tax = N * 78 // 100
an_tax = N - ((N * 20 // 100) * 22 // 100)

print(f"{n_tax} {an_tax}")