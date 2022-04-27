import sys

fix, produce, price = map(int, sys.stdin.readline().split())

answer = -1

if produce < price:
    answer = fix // (price - produce) + 1

print(answer)