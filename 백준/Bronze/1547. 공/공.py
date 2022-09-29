N = int(input())

cups = [1, 2, 3]
for _ in range(N):
    x, y = map(int, input().split())
    
    x_idx = cups.index(x)
    y_idx = cups.index(y)
    
    cups[x_idx], cups[y_idx] = cups[y_idx], cups[x_idx]
    
print(cups[0])