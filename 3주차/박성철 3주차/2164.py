# 2164 카드2

import sys
input = sys.stdin.readline
n = int(input()) # 카드의 수

queue = [] # 큐 생성
front = 0

for i in range(n): # n까지의 카드 배열 생성
    queue.append(i+1)
for _ in range(n-1): # 하나 남을때까지 수행하기 때문에 n-1번 반복
    front+=1 # front에 해당되는 값을 버렸다고 가정
    queue.append(queue[front]) # 새로운 front값을 append
    front+=1
print(queue[front])
