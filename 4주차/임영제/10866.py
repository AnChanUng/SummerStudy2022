from collections import deque #collections.deque모듈을 사용할것이기때문에선언
import sys #여러줄을 입력받아야하기때문에 sys.stdin.readline()을통해값을 받아옴

d = deque() #deque는앞과뒤에서 데이터를 처리할수있는 양방향 자료형,따라서 스택이나 큐 편한대로 사용가능
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()  #변수 command로 split()으로 나눠서 리스트로 값을 받는다

    if command[0] == "push_front":
        d.appendleft(command[1])#push_front일때 appendleft함수사용
    elif command[0] == "push_back":
        d.append(command[1])
    elif command[0] == "pop_front":
        if d:
            print(d[0])    
            d.popleft()#pop_front일때 popleft함수사용
        else:
            print("-1")
    elif command[0] == "pop_back":
        if d:
            print(d[len(d) - 1])    
            d.pop()
        else:
            print("-1")
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        if d:
            print("0")
        else:
            print("1")
    elif command[0] == "front":
        if d:
            print(d[0])
        else:
            print("-1")
    elif command[0] == "back":
        if d:
            print(d[len(d) - 1])
        else:
            print("-1")