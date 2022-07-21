# 10773 제로

import sys
input = sys.stdin.readline
n = int(input()) # 명령의 수

stack = [] # 스택생성

for _ in range(n):
    com = int(input()) # 명령 입력

    if com>0:
        stack.append(com)
    elif com == 0:
        if len(stack) ==0:
            pass
        else :
            stack.pop()

    elif com <0 :
        pass

sum =0
for i in stack:
    sum+=i
print(sum)