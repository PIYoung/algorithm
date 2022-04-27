A, B = map(int, input().split())

# 최대공약수
G = 0
# 최소공배수
L = 0

big = A if A > B else B
small = B if A > B else A

while True:
    temp = big % small

    if temp == 0:
        G = small
        L = A * B // G
        break

    big = small
    small = temp


print(G)
print(L)