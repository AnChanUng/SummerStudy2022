# 9012  괄호

import sys
input = sys.stdin.readline
n = int(input()) # 명령의 수

for _ in range(n):
    com = input()
    cl = list(com) # 괄호를 리스트로
    sum=0
    for i in cl:
        if i =='(':
            sum+=1
        elif i ==')':
            sum-=1
        if sum<0: # ')'가 먼저오면 sum은 -1이 됨
            print("NO")
            break
    if sum==0:
        print("YES")
    elif sum>0 :
        print("NO")