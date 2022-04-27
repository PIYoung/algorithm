import sys

print(" ".join(str(e) for e in sorted(map(int, sys.stdin.readline().split()))))