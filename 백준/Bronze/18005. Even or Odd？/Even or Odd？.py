N = int(input())

answer = 0
if N % 2 == 1:
    answer = 0
elif N // 2 % 2 == 0:
    answer = 2
else:
    answer = 1
    
print(answer)