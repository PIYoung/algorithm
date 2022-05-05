A = input()
B = input()
C = input()
D = input()
E = input()

answer = ""

for i in range(15):
    if len(A) > i:
        answer += A[i]

    if len(B) > i:
        answer += B[i]

    if len(C) > i:
        answer += C[i]

    if len(D) > i:
        answer += D[i]

    if len(E) > i:
        answer += E[i]


print(answer)