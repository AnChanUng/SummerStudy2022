import sys
from collections import deque # 큐 모듈

input = sys.stdin.readline
N = int(input()) # 입력 받기

que = deque([]) # 큐 배열
for i in range(1, N+1): # 1 ~ N 까지 입력받아 인큐
    que.append(i) 

while len(que) != 1: # 한 개가 남으면 반복을 멈춤
    que.popleft() # 첫 번째 데이터는 팝
    que.append(que.popleft()) # 두 번째 데이터는 팝하여 맨 뒤 배열에 추가

print(que[0]) # 마지막 남은 원소를 출력
