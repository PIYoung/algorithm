from math import comb

n = int(input())

answer = []
for i in range(n):
    A, B = map(int, input().split())
    answer.append(comb(B, A))

print("\n".join(str(e) for e in answer))