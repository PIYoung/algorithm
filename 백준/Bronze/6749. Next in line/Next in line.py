import sys

youngest = int(sys.stdin.readline())
middle = int(sys.stdin.readline())

oldest = middle + (middle - youngest)

print(oldest)