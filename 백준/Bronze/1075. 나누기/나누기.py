n = input()
f = int(input())

last = 1
answer = "00"

n = n[:-2] + answer

while int(n) % f != 0:
    if last < 10:
        answer = "0" + str(last)
    else:
        answer = str(last)

    n = n[:-2] + answer
    last += 1

print(answer)