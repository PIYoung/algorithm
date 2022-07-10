N = int(input())

result = ["Gnomes:"]
for i in range(N):
    beard_0, beard_1, beard_2 = map(int, input().split(" "))
    if (beard_1 - beard_0) * (beard_2 - beard_1) > 0:
        result.append("Ordered")
    else:
        result.append("Unordered")

print("\n".join(result))