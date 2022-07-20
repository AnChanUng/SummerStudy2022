from collections import deque  #deque사용하기위한 code

N=int(input())
deque=deque([i for i in range(1,N+1)])#N개의 수를 가진 덱을설정한다

while(len(deque)>1):    #덱의길이가 1초과인경우동안만
    deque.popleft()     #덱의 왼쪽을 팝하고
    move_num=deque.popleft()#그뒤의 덱의 왼쪽부분을 움직이는 숫자로설정하고
    deque.append(move_num)#아 움직이는 숫자를 뒤에 붙여준다

print(deque[0])    #덱의길이가 1일때의 deque[0]의 값을 출력한다
