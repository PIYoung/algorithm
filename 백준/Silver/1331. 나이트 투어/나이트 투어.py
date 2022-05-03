move_list = [input() for _ in range(36)]

if len(set(move_list)) != 36:
    print("Invalid")
    exit()

for i in range(35):
    if (
        abs(
            (ord(move_list[i][0]) - ord(move_list[i + 1][0]))
            * (int(move_list[i][1]) - int(move_list[i + 1][1]))
        )
        != 2
    ):
        print("Invalid")
        break
else:
    arr = [[-2, -1], [-2, 1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2]]

    for a, b in arr:
        c = ord(move_list[-1][0]) + a
        n = int(move_list[-1][1]) + b

        if ord("A") <= c <= ord("Z") and 1 <= n <= 6:
            if chr(c) == move_list[0][0] and n == int(move_list[0][1]):
                print("Valid")
                break

    else:
        print("Invalid")