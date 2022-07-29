A, B, C = map(int, input().split())

candy = max(A, B, C)
print((candy - A) + (candy - B) + (candy - C))