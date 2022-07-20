import sys   #여러줄을 입력받아야하기때문에 sys.stdin.readline()을통해값을 받아옴
from collections import deque   #collections.deque모듈을 사용할것이기때문에선언
n=int(sys.stdin.readline())
q=deque([])     #deque는앞과뒤에서 데이터를 처리할수있는 양방향 자료형,따라서 스택이나 큐 편한대로 사용가능
for i in range(n):
    s=sys.stdin.readline().split()   #변수 s로 split()으로 나눠서 리스트로 값을 받는다
    if s[0]=='push':
       q.append(s[1])
    elif s[0]=='pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif s[0]=='size':
        print(len(q))
    elif s[0] =='empty':
        if not q:
            print(1)
        else:
            print(0) 
    elif s[0]=='front':
        if not q:
            print(-1)  
        else:
            print(q[0])
    elif s[0]=='back':
        if not q:
            print(-1)
        else:
            print(q[-1])                         
