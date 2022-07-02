width, height = map(int, input().split())

result = width + height - (width**2 + height**2)**0.5

print(result)