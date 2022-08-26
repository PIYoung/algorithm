N = int(input())

for i in range(N):
    ships, speed, days = map(int, input().split())

    result = 0
    for j in range(ships):
        distance, ducats = map(int, input().split())

        if days * speed >= distance:
            result += ducats

    print(f"Data Set {i+1}:")
    print(result)
    print()