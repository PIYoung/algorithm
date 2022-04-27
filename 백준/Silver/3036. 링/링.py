from fractions import Fraction
from math import gcd

n = int(input())
input_list = list(map(int, input().split()))

answer = []
for i in range(1, len(input_list)):
    result = Fraction(input_list[0], input_list[i])
    answer.append(f"{result.numerator}/{result.denominator}")

print(*answer, sep="\n")