data = input()

answer = []

while data:
    answer.append(data[:10])
    data = data[10:]

print("\n".join(answer))