X = int(input())

stick = [64]

while sum(stick) != X:
    min_stick = stick.pop(stick.index(min(stick)))
    half_stick = min_stick // 2

    if sum(stick) + half_stick >= X:
        stick.append(half_stick)
    else:
        stick.append(half_stick)
        stick.append(half_stick)


print(len(stick))