import sys
import math

vacation = int(sys.stdin.readline())
total_korean_page = int(sys.stdin.readline())
total_math_page = int(sys.stdin.readline())
per_korean_page = int(sys.stdin.readline())
per_math_page = int(sys.stdin.readline())

a = int(math.ceil(total_korean_page / per_korean_page))
b = int(math.ceil(total_math_page / per_math_page))

print(vacation - max([a, b]))