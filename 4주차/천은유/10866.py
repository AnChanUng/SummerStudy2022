import sys
from collections import deque # 큐 모듈

queue = deque([]) # 큐 배열 생성

input = sys.stdin.readline
n = int(input()) # 몇 개 입력 받을 지 저장
N = [input().strip() for _ in range(n)] # 명령을 입력받음

for i in range(n):
    if "push_front" in N[i]: # 앞 인큐
        queue.appendleft(N[i].split()[1])
    
    elif "push_back" in N[i]: # 뒤 인큐
        queue.append(N[i].split()[1])

    elif N[i] == "pop_front": # 앞 디큐
        if not queue: # 배열이 비었으면
            print(-1) # -1 출력
        else: # 배열이 채워있으면
            print(queue.popleft()) # 맨 앞 데이터 pop

    elif N[i] == "pop_back": # 뒤 디큐
        if not queue: # 배열이 비었으면
            print(-1) # -1 출력
        else: # 배열이 채워있으면
            print(queue.pop()) # 맨 뒤 데이터 pop

    elif N[i] == "size": # 사이즈 출력
        print(len(queue))

    elif N[i] == "empty": # 빈 배열 여부
        if not queue: # 빈 배열이면 1 출력
            print(1)
        else:
            print(0) # 0 출력

    elif N[i] == "front": # 프론트 값 출력
        if not queue: # 빈 배열이면 -1 출력
            print(-1)
        else:
            print(queue[0]) # 프론트 값 출력

    elif N[i] == "back": # 리어 값 출력
        if not queue: # 빈 배열이면 -1 출력
            print(-1)
        else:
            print(queue[-1]) # 프론트 값 출력
