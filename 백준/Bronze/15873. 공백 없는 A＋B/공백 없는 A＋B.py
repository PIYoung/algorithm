n = input()

answer = 0
if len(n) == 2:
    A = int(n[:1])
    B = int(n[1:])
    
    answer = A + B
elif len(n) == 3:
    if int(n[:2]) == 10:
        A = int(n[:2])
        B = int(n[2:])
        
        answer = A + B
    else:
        A = int(n[:1])
        B = int(n[1:])
        
        answer = A + B
else:
    A = int(n[:2])
    B = int(n[2:])
    answer = A + B

print(answer)