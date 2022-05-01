n = int(input())
dp = [0 for _ in range(n)]

children = []

for i in range(n):
    children.append(int(input()))

    for j in range(i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j])

    dp[i] += 1


print(n - max(dp))