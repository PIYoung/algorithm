word = input()

answer = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        first = list(word[:i])
        first.reverse()
        first = "".join(first)

        second = list(word[i:j])
        second.reverse()
        second = "".join(second)

        last = list(word[j:])
        last.reverse()
        last = "".join(last)

        answer.append(first + second + last)

answer.sort()
print(answer[0])