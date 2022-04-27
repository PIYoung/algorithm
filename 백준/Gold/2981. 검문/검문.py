import math

n = int(input())
input_list = sorted([int(input()) for _ in range(n)])
diff_list = []
answer = []

for i in range(1, n):
    diff_list.append(input_list[i] - input_list[i - 1])

prev = diff_list[0]
for i in range(1, len(diff_list)):
    prev = math.gcd(prev, diff_list[i])

for i in range(2, int(math.sqrt(prev)) + 1):
    if prev % i == 0:
        answer.append(i)
        answer.append(prev // i)

answer.append(prev)
answer = sorted(set(answer))
print(*answer)