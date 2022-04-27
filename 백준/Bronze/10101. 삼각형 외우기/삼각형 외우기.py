A = int(input())
B = int(input())
C = int(input())

if A + B + C == 180:
    if A == B and B == C:
        print("Equilateral")
    elif A == B and B != C or A == C and C != B or B == C and C != A:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")