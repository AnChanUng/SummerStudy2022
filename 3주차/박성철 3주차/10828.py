import sys
input = sys.stdin.readline
n = int(input()) # 명령의 수

stack = [] # 스택생성

for _ in range(n):
    com = input().split() # 명령 입력

    if com[0]=="push":
        stack.append(com[1])
    elif com[0] == "pop":
        if len(stack) ==0:
            print(-1)
        else :
            top = stack[-1] # 스택의 탑에 해당하는 값을 top변수에 저장
            stack.pop()
            print(top)
    elif com[0] == "size":
        print(len(stack))
    elif com[0] == "empty":
        if len(stack) == 0:
            print(1)
        else :
            print(0)
    elif com[0] == "top":
        if len(stack)==0:
            print(-1)
        else :
            print(stack[-1])