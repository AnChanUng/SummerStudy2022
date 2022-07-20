# 18258 큐2

import sys
input = sys.stdin.readline
n = int(input()) # 명령의 수

queue = [] # 큐 생성
front = 0
rear = 0
for _ in range(n):
    com = input().split() # 명령 입력

    if com[0]=="push":
        queue.append(com[1])
        rear+=1 # back 1씩 증가
    elif com[0] == "pop":
        if front>=rear:
            print(-1)
        else :
            o = queue[front] # 큐의 front에 해당하는 값을 o변수에 저장
            front+=1 # front 1씩 증가
            print(o) # pop된 값 출력
    elif com[0] == "size":
        print(rear-front) # rear와 front의 차이가 결국 큐에 들어있는 정수의 개수
    elif com[0] == "empty":
        if rear<=front:
            print(1)
        else :
            print(0)
    elif com[0] == "front":
        if rear<=front:
            print(-1)
        else :
            print(queue[front])
    elif com[0] =="back":
        if rear<=front:
            print(-1)
        else :
            print(queue[rear-1]) # rear-1에 해당하는 인덱스의 값이 마지막 값