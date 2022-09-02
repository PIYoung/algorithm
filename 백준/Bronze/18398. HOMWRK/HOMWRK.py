T = int(input())
for _ in range(T):
    P = int(input())
    for __ in range(P):
        N = list(map(int, input().split()))

        print(N[0] + N[1], N[0] * N[1])