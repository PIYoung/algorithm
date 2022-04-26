import sys

per, participant = map(int, sys.stdin.readline().split())
A, B, C, D, E = map(int, sys.stdin.readline().split())

total = per * participant

print(f"{A - total} {B - total} {C - total} {D - total} {E - total}")
