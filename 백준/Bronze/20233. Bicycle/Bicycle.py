a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

A = a + max(T - 30, 0) * x * 21
B = b + max(T - 45, 0) * y * 21

print(A, B)