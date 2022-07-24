# [백준 10773번] - 제로 - (실버4, 스택)
import sys
input = sys.stdin.readline

k = int(input())         # 입력 개수
stack = []               

for i in range(k):
    N = int(input())
    if k == 0:           # 0이면 pop
      stack.pop()
    else:                # 0이 아니면 push=append
      stack.append(N)

print(sum(stack))        # 총합을 구하는 sum