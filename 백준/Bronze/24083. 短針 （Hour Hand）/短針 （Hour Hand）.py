a = int(input())
b = int(input())

answer = (a + b) % 12
if not answer: 
    answer = 12
print(answer)