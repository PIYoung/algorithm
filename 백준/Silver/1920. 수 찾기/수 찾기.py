import sys
from collections import deque

N = int(sys.stdin.readline())
n = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())
m_deque = deque(sys.stdin.readline().split())

answer = deque()

while m_deque:
    m = m_deque.popleft()
    answer.append(1) if m in n else answer.append(0)


print("\n".join(map(str, answer)))