n = int(input())

dict = {}

for _ in range(n):
    data = input()
    first_name = data[0]

    if not first_name in dict:
        dict[first_name] = 0

    dict[first_name] += 1


answer = ""
for key, value in dict.items():
    if value >= 5:
        answer += key

print("".join(sorted(answer)) if answer else "PREDAJA")