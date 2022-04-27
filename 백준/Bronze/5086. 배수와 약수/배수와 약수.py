answer = ""

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    if answer != "":
        answer += "\n"

    if b % a == 0:
        answer += "factor"
    elif a % b == 0:
        answer += "multiple"
    else:
        answer += "neither"

print(answer)