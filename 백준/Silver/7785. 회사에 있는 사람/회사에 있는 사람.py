from sys import stdin

n = int(stdin.readline())
dict = {}

for _ in range(n):
    name, state = stdin.readline().split()

    if state == "enter":
        dict[name] = True
    else:
        del dict[name]


answer = sorted(dict.keys(), reverse=True)
print("\n".join(answer))