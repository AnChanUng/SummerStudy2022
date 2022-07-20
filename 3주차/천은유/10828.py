import sys
stk = [] # 빈 리스트

def push(item): # 리스트 뒤에 데이터를 추가한다.
    stk.append(item)

def pop(): # 리스트 뒤에 있는 요소를 제거한다.
    if len(stk) == 0: # 스택이 비었으면 -1 반환
        print(-1) 
    else: 
        print(stk[-1]) # 맨 뒤에 있는 요소를 출력한다.
        stk.pop() # 제거
 
def size(stk): # 스택 크기 출력
    print(len(stk)) 

def empty(stk): # 스택이 빈 경우
    if len(stk) == 0 : # 스택 크기가 0이면
        print(1) # 1 출력
    else : # 스택이 비어있지 않으면
        print(0) # 0 출력
        
def top(stk): 
    if len(stk) > 0 : # 스택이 비어있지 않으면
        print(stk[-1]) # 맨 꼭대기 데이터를 출력
    else: # 비어있으면
        print(-1) # -1 출력

input = sys.stdin.readline
n = int(input()) # 입력 수
N = [input().rstrip() for _ in range(n)]  

for i in range(n):
    if "push" in N[i]: # push가 입력된 경우
        push(N[i].split()[1]) # push 다음 수를 잘라서 push 함수를 사용
        
    elif N[i] == "top":
        top(stk)
        
    elif N[i] == "size":
        size(stk)
        
    elif N[i] == "empty":
        empty(stk)
        
    elif N[i] == "pop":
        pop()
