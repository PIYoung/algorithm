x, y = map(int, input().split())

answer = -1
if x > y:
    answer = x + y
elif x == y:
    answer = 0
else:
    answer = y - x
    
print(answer)