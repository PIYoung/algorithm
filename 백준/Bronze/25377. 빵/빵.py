N = int(input())

result = 999999
for _ in range(N):
    A, B = map(int, input().split())
    
    if A > B:
        continue
        
    if B < result:
        result = B
        
if result == 999999:
    print(-1)
else:
    print(result)