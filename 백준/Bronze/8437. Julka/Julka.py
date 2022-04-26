import sys

total = int(sys.stdin.readline())
diff = int(sys.stdin.readline())

a = (total - diff) // 2
print(a + diff)
print(a)