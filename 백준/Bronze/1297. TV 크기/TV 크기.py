import sys
import math

D, H, W = map(int, sys.stdin.readline().split())

height = D * H // math.sqrt(H**2 + W**2)
width = D * W // math.sqrt(H**2 + W**2)

print(f"{int(height)} {int(width)}")