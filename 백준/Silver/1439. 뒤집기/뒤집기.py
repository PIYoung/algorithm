S = input()

one_sequence = 0
zero_sequence = 0

if len(set(S)) == 1:
    print(0)
else:
    prev = "-1"
    for i in S:
        if prev == i:
            continue
        else:
            prev = i
            if i == "0":
                zero_sequence += 1
            else:
                one_sequence += 1

    print(min(one_sequence, zero_sequence))