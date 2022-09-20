import sys


def solve(n):
    data = [int(sys.stdin.readline().strip()) for _ in range(n)]
    S = sum(data)

    if S > 0:
        print("+")
    elif S < 0:
        print("-")
    else:
        print("0")


solve(int(input()))
solve(int(input()))
solve(int(input()))
