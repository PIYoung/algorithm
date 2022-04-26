import sys

total = 0
for i in range(4):
    total += int(sys.stdin.readline())
    
min = total // 60
sec = total % 60

print(min)
print(sec)