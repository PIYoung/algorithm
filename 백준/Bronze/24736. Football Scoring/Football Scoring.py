import sys

A1, B1, C1, D1, E1 = map(int, sys.stdin.readline().split())
A2, B2, C2, D2, E2 = map(int, sys.stdin.readline().split())

f_total = (A1 * 6) + (B1 * 3) + (C1 * 2) + (D1 * 1) + (E1 * 2)
s_total = (A2 * 6) + (B2 * 3) + (C2 * 2) + (D2 * 1) + (E2 * 2)

print(f"{f_total} {s_total}")