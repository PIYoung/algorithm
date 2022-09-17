N = int(input())

answer = -1
for _ in range(N):
    a, d, g = map(int, input().split())
    temp = a * (d + g)
    
    if a == d + g:
        temp *= 2
        
    if temp > answer:
        answer = temp
    
print(answer)