import sys

input = sys.stdin.readline
k = int(input())
stk = [] # 빈 배열

for i in range(k): # k번 반복
    case = int(input()) # 수 입력받기
    if case == 0 and len(stk) != 0: # 수가 0이면서 stk 배열에 요소가 들어있는 경우  
        stk.pop() # 가장 마지막 요소를 pop한다
    else:
        stk.append(case) # 수를 stk 배열에 추가한다

print(sum(stk)) # stk 배열 내 모든 수를 더한다
