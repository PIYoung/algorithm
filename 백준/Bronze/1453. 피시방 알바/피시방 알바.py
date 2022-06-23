N = int(input())
PC_Georgia = list(map(int, input().split()))        
PC_checkmate = [0] * 101 #PC방 자리
PC_refused = 0 #거절당한 사람

for i in PC_Georgia:
    if PC_checkmate[i] != 0:
        PC_refused += 1
    else:
        PC_checkmate[i] += 1

print(PC_refused)