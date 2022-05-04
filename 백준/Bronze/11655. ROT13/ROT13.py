data = input()

answer = ""

for s in data:
    if s == " ":
        answer += " "
        continue

    if "a" <= s <= "z":
        temp = ""
        if chr(ord(s) + 13) > "z":
            temp = chr(ord("a") + (ord(s) + 13) - ord("z") - 1)
        else:
            temp = chr(ord(s) + 13)
        answer += temp
    elif "A" <= s <= "Z":
        temp = ""
        if chr(ord(s) + 13) > "Z":
            temp = chr(ord("A") + (ord(s) + 13) - ord("Z") - 1)
        else:
            temp = chr(ord(s) + 13)
        answer += temp
    else:
        answer += s
        continue


print(answer)