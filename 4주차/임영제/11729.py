N=int(input())#N값입력받기
def move(N,x,y):#재귀함수를 이용하여 move함수정의
     if N==1:
         print(x,y)
         return

     move(N-1,x,6-x-y)#1단계

     print(x,y)#2단계
    
     move(N-1,6-x-y,y)#3단계  
print(2**N-1)   #총실행횟수
move(N,1,3)         #move함수실행