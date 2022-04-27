import math

height, width, cctv = map(int, input().split())

print(int(math.ceil(height / cctv)) * int(math.ceil(width / cctv)))