N = int(input())

for _ in range(N):
    UD = input()
    result = 0

    for adam in UD:
        if adam == "D":
            break

        result += 1

    print(result)