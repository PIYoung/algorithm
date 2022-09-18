n = int(input())

answer = 0
if n <= 198:
    for i in range(1, 100):
        for j in range(1, 100):
            if i + j == n:
                answer += 1
                
print(answer)