_list = [list(map(int, input().split())) for _ in range(int(input()))]

for n, m in _list:
    print(n * m // 2)