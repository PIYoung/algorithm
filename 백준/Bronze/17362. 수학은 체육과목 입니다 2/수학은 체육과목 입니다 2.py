n = int(input())

answer = n % 8

if answer == 0:
    answer = 2
elif answer == 7:
    answer = 3
elif answer == 6:
    answer = 4
else:
    pass

print(answer)