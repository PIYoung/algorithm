N = int(input())
S = list(map(int, input().split()))
Y = 0
M = 0

for s in S:
    Y += s // 30 * 10 + 10
    M += s // 60 * 15 + 15

if Y < M:
    print('Y %d' % Y)
elif Y > M:
    print('M %d' % M)
else:
    print('Y M %d' % Y)