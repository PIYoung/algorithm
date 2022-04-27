n = int(input())

answer = 0
while n != 0:
    n //= 5
    answer += n

print(answer)