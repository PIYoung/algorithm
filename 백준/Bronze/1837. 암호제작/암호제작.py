P, K = map(int, input().split())

tmp = True
for i in range(2, K):
    if P % i == 0:
        print('BAD', i)
        tmp = False
        break
        
if tmp:
    print('GOOD')