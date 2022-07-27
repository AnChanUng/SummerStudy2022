# [백준 2164번] - 카드2 - (실버4, 스택)
from collections import deque
import sys
input=sys.stdin.readline

N = int(input())

q = deque(range(1, N+1))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.popleft())