answer = []

while True:
    n = input()

    if int(n) == 0:
        break

    for i in range(len(n) // 2):
        if n[i] != n[-i - 1]:
            answer.append("no")
            break
    else:
        answer.append("yes")


print("\n".join(answer))