answer = []

for i in range(int(input())):
    temp = {}
    for j in range(int(input())):
        stuff, kind = map(str, input().split())
        if kind not in temp:
            temp[kind] = [stuff]
        else:
            temp[kind].append(stuff)

    dress_case = 1
    for key, value in temp.items():
        dress_case *= len(value) + 1

    answer.append(dress_case - 1)

print("\n".join(str(e) for e in answer))