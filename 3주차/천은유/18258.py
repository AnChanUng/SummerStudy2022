import sys
from collections import deque # 큐 모듈

queue = deque([]) # 큐 배열 생성

def push(x): # x를 인큐
    queue.append(x)
    
def pop(): # 디큐
    if not queue: # 배열이 비었으면
        print(-1) # -1 출력
    else: # 배열이 채워있으면
        print(queue.popleft()) # 맨 앞 데이터 pop

def size(queue): # 배열의 사이즈 출력
    print(len(queue))

def empty(queue): # 배열이 비었는지 
    if not queue: 
        print(1) # 빈 배열
    else:
        print(0) # 채워진 배열

def front(): # 프론트 찾기
    if not queue: # 빈 배열이면 -1 출력
        print(-1)
    else:
        print(queue[0]) # 프론트 값 출력

def back(): # 리어 찾기 
    if not queue: # 빈 배열이면 -1 출력
        print(-1)
    else:
        print(queue[-1]) # 리어 값 출력

input = sys.stdin.readline
n = int(input()) # 몇 개 입력 받을 지 저장
N = [input().strip() for _ in range(n)] # 명령울 입력받음

for i in range(n):
    if "push" in N[i]: 
        push(N[i].split()[1]) # 입력받은 문장에서 두 번째에 저장된 수만큼 푸시하기

    elif N[i] == "pop": # 디큐
        pop() 

    elif N[i] == "size": # 사이즈 출력
        size(queue)

    elif N[i] == "empty": # 빈 배열 여부
        empty(queue)

    elif N[i] == "front": # 프론트 값 출력
        front()

    elif N[i] == "back": # 리어 값 출력
        back()
