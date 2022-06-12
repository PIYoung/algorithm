temp = list(map(int, input().split()))
temp.sort()
A, B, C = temp

if A == B or B == C or A + B == C:
    print("S")
else:
    print("N")