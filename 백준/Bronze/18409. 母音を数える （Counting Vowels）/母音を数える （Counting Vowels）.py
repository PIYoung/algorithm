N = int(input())
S = input()

answer = 0
for s in S:
    if s in 'aeiou':
        answer += 1

print(answer)
