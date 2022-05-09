N, W, H, L = map(int, input().split())

A1 = W // L
A2 = H // L

answer = A1 * A2

if N < answer:
    print(N)
else:
    print(answer)