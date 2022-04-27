physics = int(input())
chemical = int(input())
biology = int(input())
earth = int(input())

history = int(input())
geography = int(input())

print(sum(sorted([physics, chemical, biology, earth])[1:]) + max(history, geography))