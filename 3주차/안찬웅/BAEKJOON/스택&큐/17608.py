# [백준 17608번] - 막대기 - (브론즈2, 스택)
import sys
input = sys.stdin.readline

N = int(input())               # 막대기의 개수
stack = []

for _ in range(N):
    stack.append(N)

last = stack[-1]
count = 1

for i in reversed(range(N)):
    if stack[i] > last:
         count += 1
         last = stack[i]

print(count)