import sys

print(
    max(
        sum(map(int, sys.stdin.readline().split())),
        sum(map(int, sys.stdin.readline().split())),
    )
)