amount = int(input())

result = amount * 0.01 + 25
if result < 100:
    print(100)
elif result > 2000:
    print(2000)
else:
    print(result)